from typing import List, Any
import os
import fiona
import fiona.transform
import numpy as np
import rasterio
import rasterio.mask
import shapely.geometry
from tqdm import tqdm
import glob
import cv2
from rasterio.features import rasterize
import matplotlib.pyplot as plt

from blueness import module
from blue_objects import objects, file
from blue_objects.metadata import get_from_object, post_to_object
from blue_objects.logger.matrix import log_matrix
from blue_objects.graphics.signature import sign_filename
from blue_geo import fullname as blue_geo_fullname
from roofai import fullname as roofai_fullname

from palisades.host import signature
from palisades import env
from palisades import NAME
from palisades import fullname
from palisades.logger import logger

NAME = module.name(__file__, NAME)


# based on https://github.com/microsoft/building-damage-assessment/blob/main/merge_with_building_footprints.py
def analyze_buildings(
    object_name: str,
    buffer: float,
    verbose: bool = False,
    max_count: int = -1,
) -> bool:
    prediction_filename = get_from_object(
        object_name,
        "predict.output_filename",
        "",
    )
    if not prediction_filename:
        logger.error("predict.output_filename not found in metadata.")
        return False
    prediction_full_filename = objects.path_of(prediction_filename, object_name)

    datacube_id = get_from_object(
        object_name,
        "predict.datacube_id",
        "",
    )
    datacube_datetime = get_from_object(datacube_id, "item_info.properties.datetime")
    logger.info(f"📆  {datacube_datetime}")
    if not datacube_datetime:
        logger.error("datacube datetime not found.")
        return False

    reference_filename = get_from_object(
        object_name,
        "predict.reference_filename",
        "",
    )
    reference_full_filename = objects.path_of(reference_filename, datacube_id)

    footprint_filename_list = glob.glob(objects.path_of("*.gpkg", object_name))
    if not footprint_filename_list:
        logger.error(f"*.gpkg not found in {object_name}.")
        return False
    footprint_filename = footprint_filename_list[0]

    logger.info(
        "{}.analyze_buildings({:.0} m): {} / {} : {}".format(
            NAME,
            buffer,
            object_name,
            prediction_filename,
            file.name_and_extension(footprint_filename),
        )
    )

    with rasterio.open(prediction_full_filename, "r") as src:
        predictions_crs = src.crs.to_string()

    with fiona.open(footprint_filename, "r") as src:
        footprints_crs = src.crs.to_string()

    # Clip building footprints to image data mask
    logger.info(f"crs: {footprints_crs} -> {predictions_crs}")
    projected_building_geoms = []
    with fiona.open(footprint_filename) as f:
        for row in tqdm(f):
            projected_geom = fiona.transform.transform_geom(
                footprints_crs, predictions_crs, row["geometry"]
            )
            projected_building_geoms.append(projected_geom)

            if max_count != -1 and len(projected_building_geoms) >= max_count:
                break

    logger.info("analyzing {:,} building(s)".format(len(projected_building_geoms)))
    list_of_building_info: List[Any] = []

    with rasterio.open(
        prediction_full_filename,
    ) as prediction_raster, rasterio.open(
        reference_full_filename,
    ) as reference_raster:
        pixel_size = prediction_raster.res
        pixel_area = pixel_size[0] * pixel_size[1]
        logger.info(f"pixel size: {pixel_size} m = {pixel_area:.2f} m^2")

        for index, building_geom in tqdm(enumerate(projected_building_geoms)):
            building_info = {
                "id": index,
            }

            building_shape = shapely.geometry.shape(building_geom)
            building_shape_buffered = building_shape.buffer(buffer)

            centroid = shapely.geometry.shape(building_geom).centroid
            building_info["building_id"] = "-".join(
                [
                    "{:06.0f}".format(round(value / 10))
                    for value in [centroid.x, centroid.y]
                ]
            )

            prediction_mask, transform = rasterio.mask.mask(
                prediction_raster,
                [building_shape_buffered],
                crop=True,
                nodata=0,
                filled=True,
            )
            prediction_mask = prediction_mask[0].astype(np.float32) / 255
            building_info["damage"] = float(np.mean(prediction_mask))

            rasterized_shape = rasterize(
                [(building_shape, 1)],  # value 1 to all pixels inside the shape
                out_shape=prediction_mask.shape,
                transform=transform,
                fill=0,  # background
                dtype="uint8",
            )
            building_info["area"] = float(np.sum(rasterized_shape) * pixel_area)

            building_info["thumbnail"] = "thumbnail-{}-{:06}.png".format(
                file.name(prediction_filename),
                index,
            )

            building_halo = (rasterized_shape.astype(np.float32) + 1) / 2

            reference_mask, transform = rasterio.mask.mask(
                reference_raster,
                [building_shape_buffered],
                crop=True,
                nodata=0,
                filled=True,
            )
            reference_mask = np.transpose(reference_mask, (1, 2, 0))
            reference_mask = (
                reference_mask.astype(np.float32) * building_halo[:, :, np.newaxis]
            )

            if not log_matrix(
                matrix=prediction_mask * building_halo,
                suffix=[reference_mask],
                header=[
                    "{} / {}".format(
                        building_info["building_id"],
                        datacube_datetime,
                    )
                ]
                + objects.signature(
                    info=reference_filename,
                    object_name=datacube_id,
                )
                + [
                    object_name,
                    file.name_and_extension(footprint_filename),
                    "area: {:.1f} sq. m".format(building_info["area"]),
                    "damage: {:03.2f}%".format(
                        100 * building_info["damage"],
                    ),
                    "pixel_size: {}".format(
                        " x ".join(
                            ["{:.2f} cm".format(10 * value) for value in pixel_size]
                        )
                    ),
                    f"buffer: {buffer:.1f} m",
                ],
                footer=[
                    fullname(),
                    blue_geo_fullname(),
                    roofai_fullname(),
                ],
                colormap=cv2.COLORMAP_HOT,
                invert_color_map=False,
                invert_color_map_rgb=False,
                dynamic_range=[0, 1],
                filename=objects.path_of(
                    building_info["thumbnail"],
                    object_name,
                ),
                log=verbose,
            ):
                return False

            if verbose:
                logger.info("damage: {:03.2f}%".format(100 * building_info["damage"]))

            list_of_building_info += [building_info]

    schema = {
        "geometry": "MultiPolygon",
        "properties": {
            "id": "int",
            "area": "float",
            "building_id": "str",
            "damage": "float",
            "thumbnail": "str",
        },
    }

    output_filename = objects.path_of(
        "analysis.gpkg",
        object_name,
    )

    logger.info("saving...")
    with fiona.open(
        output_filename,
        "w",
        driver="GPKG",
        crs=predictions_crs,
        schema=schema,
    ) as f:
        for index, (geom, building_info) in enumerate(
            tqdm(
                zip(
                    projected_building_geoms,
                    list_of_building_info,
                )
            )
        ):
            shape = shapely.geometry.shape(geom)
            if geom["type"] == "Polygon":
                geom = shapely.geometry.mapping(shapely.geometry.MultiPolygon([shape]))

            row = {
                "type": "Feature",
                "geometry": geom,
                "properties": {
                    "id": index,
                    "area": building_info["area"],
                    "building_id": building_info["building_id"],
                    "damage": building_info["damage"],
                    "thumbnail": building_info["thumbnail"],
                },
            }
            f.write(row)

    logger.info(f"-> {output_filename}")

    if not post_to_object(
        object_name,
        "analysis",
        {
            "datetime": datacube_datetime,
            "building-count": len(list_of_building_info),
            "damaged-count": len(
                [
                    building_info
                    for building_info in list_of_building_info
                    if building_info["damage"] > 0
                ]
            ),
            "output_filename": file.name_and_extension(output_filename),
        },
    ):
        return False

    all_area = [building_info["area"] for building_info in list_of_building_info]
    all_area_hist, bin_edges = np.histogram(all_area, bins=10)
    damaged_area_hist = np.histogram(
        [
            building_info["area"]
            for building_info in list_of_building_info
            if building_info["damage"] > 0
        ],
        bins=bin_edges,
    )[0]
    non_damaged_area_hist = np.histogram(
        [
            building_info["area"]
            for building_info in list_of_building_info
            if building_info["damage"] == 0
        ],
        bins=bin_edges,
    )[0]

    plt.figure(figsize=(10, 5))
    bar_width = (bin_edges[1] - bin_edges[0]) / 5
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    plt.bar(
        bin_centers + bar_width,
        all_area_hist,
        width=bar_width,
        label="All",
        align="center",
        color="black",
        alpha=0.5,
    )
    plt.bar(
        bin_centers + 2 * bar_width,
        non_damaged_area_hist,
        width=bar_width,
        label="Not Damaged",
        align="center",
        color="green",
        alpha=0.5,
    )
    plt.bar(
        bin_centers + 3 * bar_width,
        damaged_area_hist,
        width=bar_width,
        label="Damaged",
        align="center",
        color="red",
        alpha=0.5,
    )
    plt.title("Distribution of Building Areas")
    plt.xlabel("Building Area (sq m)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.legend()
    filename = objects.path_of(
        "area-damage-histogram.png",
        object_name,
    )
    if not file.save_fig(filename):
        return False
    if not sign_filename(
        filename=filename,
        header=[datacube_datetime]
        + objects.signature(
            info=reference_filename,
            object_name=datacube_id,
        )
        + [
            f"{object_name}",
            file.name_and_extension(footprint_filename),
            "{} building(s)".format(len(list_of_building_info)),
        ],
        footer=signature(),
    ):
        return False

    plt.figure(figsize=(10, 5))
    colors = [
        "red" if building_info["damage"] > 0 else "green"
        for building_info in list_of_building_info
    ]
    plt.scatter(
        all_area,
        [building_info["damage"] for building_info in list_of_building_info],
        c=colors,
        alpha=0.5,
    )
    plt.title("Scatter Plot of Building Area vs Damage")
    plt.xlabel("Building Area (sq m)")
    plt.ylabel("Damage")
    plt.ylim(0, 1)
    plt.grid(True)
    filename = objects.path_of(
        "area-damage-scatter.png",
        object_name,
    )
    if not file.save_fig(filename):
        return False
    if not sign_filename(
        filename=filename,
        header=[datacube_datetime]
        + objects.signature(
            info=reference_filename,
            object_name=datacube_id,
        )
        + [
            f"{object_name}",
            file.name_and_extension(footprint_filename),
            "{} building(s)".format(len(list_of_building_info)),
        ],
        footer=signature(),
    ):
        return False

    return True

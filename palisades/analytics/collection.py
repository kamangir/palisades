from typing import Dict, Any, Tuple, List
import pandas as pd
from tqdm import tqdm
import geopandas as gpd
from collections import Counter
import numpy as np
from shapely.geometry import box

from blueness import module
from blue_objects import mlflow, objects, file
from blue_objects.mlflow.tags import create_filter_string
from blue_objects.metadata import get_from_object

from palisades import NAME
from palisades import env
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def collect_analytics(
    acq_count: int = -1,
    building_count: int = -1,
    damage_threshold: float = env.PALISADES_DAMAGE_THRESHOLD,
    log: bool = True,
    verbose: bool = False,
    building_id: str = "",
) -> Tuple[pd.DataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, Dict]:
    logger.info(
        "{}.collect_analytics: damage > {:.1f}: {}{}{}".format(
            NAME,
            damage_threshold,
            f"{acq_count} acq(s) " if acq_count != -1 else "",
            f"{building_count} buildings(s) " if building_count != -1 else "",
            f" for {building_id}" if building_id else "",
        )
    )

    # get list of prediction objects
    list_of_prediction_objects = mlflow.search(
        create_filter_string("contains=palisades.prediction,profile=FULL")
    )
    if acq_count != -1:
        list_of_prediction_objects = list_of_prediction_objects[:acq_count]
    logger.info(f"{len(list_of_prediction_objects)} acq(s) to process.")

    # collect df columns
    metadata: Dict[str, Any] = {
        "objects": {},
        "datetime": [],
        "prediction_datetime": {},
    }
    logger.info("collecting the predictions ...")
    for prediction_object_name in tqdm(list_of_prediction_objects):
        logger.info(f"processing {prediction_object_name} ...")

        metadata["objects"][prediction_object_name] = {"success": False}

        prediction_datetime = get_from_object(
            prediction_object_name,
            "analysis.datetime",
            download=True,
        )
        if not prediction_datetime:
            logger.warning("analysis.datetime not found.")
            continue

        if not objects.download(
            filename="analysis.gpkg",
            object_name=prediction_object_name,
        ):
            continue

        metadata["datetime"] += [prediction_datetime]
        metadata["prediction_datetime"][prediction_object_name] = prediction_datetime
        metadata["objects"][prediction_object_name]["success"] = True

    metadata["datetime"] = sorted(list(set(metadata["datetime"])))
    logger.info(
        "{} acquisitions(s): {}".format(
            len(metadata["datetime"]),
            ", ".join(metadata["datetime"]),
        )
    )

    # generate the df
    df_columns: Dict[str, str] = {
        "area": "float",
        "building_id": "str",
        "damage": "float",
        "damage_std": "float",
        "thumbnail": "str",
        "thumbnail_object": "str",
        "observation_count": "int",
    }
    for prediction_datetime in metadata["datetime"]:
        df_columns[prediction_datetime] = "float"
        df_columns[f"{prediction_datetime}-thumbnail"] = "str"
        df_columns[f"{prediction_datetime}-object_name"] = "str"
    logger.info(
        "{} df columns: {}".format(
            len(df_columns),
            ", ".join(
                f"{col_name}: {col_type}" for col_name, col_type in df_columns.items()
            ),
        )
    )
    df = pd.DataFrame(columns=df_columns.keys())
    df = df.astype(df_columns)

    # generate the gdf
    logger.info("ingesting...")
    list_of_polygons = []
    list_of_bboxes = []
    List_of_bbox_area: List[float] = []
    crs = ""
    total_building_count: int = 0
    for prediction_object_name in tqdm(list_of_prediction_objects):
        if not metadata["objects"][prediction_object_name]["success"]:
            continue

        prediction_datetime = metadata["prediction_datetime"][prediction_object_name]

        # for additional checks
        metadata["objects"][prediction_object_name]["success"] = False

        logger.info(f"processing {prediction_object_name} ...")

        success, gdf = file.load_geodataframe(
            objects.path_of(
                filename="analysis.gpkg",
                object_name=prediction_object_name,
            ),
            log=log,
        )
        if not success:
            continue
        if not crs:
            crs = gdf.crs
        if building_count != -1:
            gdf = gdf.head(building_count)
        total_building_count += len(gdf)

        if not gdf.geometry.is_empty.any():
            minx, miny, maxx, maxy = gdf.total_bounds
            list_of_bboxes.append(box(minx, miny, maxx, maxy))

            bbox_area = (maxx - minx) * (maxy - miny) / 1000 / 1000
            logger.info("+= {:,.1f} sq. km".format(bbox_area))
            List_of_bbox_area += [float(bbox_area)]

        if "building_id" not in gdf.columns:
            logger.warning("building_id not found.")
            continue

        collected_building_count = 0
        for _, row in tqdm(gdf.iterrows()):
            if building_id and row["building_id"] != building_id:
                continue

            if row["damage"] < damage_threshold:
                continue

            collected_building_count += 1

            if row["building_id"] not in df["building_id"].values:
                list_of_polygons.append(row["geometry"])

                df.loc[len(df)] = {
                    "building_id": row["building_id"],
                    "area": row["area"],
                    "thumbnail": row["thumbnail"],
                    "thumbnail_object": prediction_object_name,
                }

            df.loc[
                df["building_id"] == row["building_id"],
                prediction_datetime,
            ] = row["damage"]

            df.loc[
                df["building_id"] == row["building_id"],
                f"{prediction_datetime}-thumbnail",
            ] = row["thumbnail"]

            df.loc[
                df["building_id"] == row["building_id"],
                f"{prediction_datetime}-object_name",
            ] = prediction_object_name

        metadata["objects"][prediction_object_name] = {
            "success": True,
            "building_count": len(gdf),
            "collected_building_count": collected_building_count,
        }
        logger.info(f"ingested {len(df):,} building(s) so far...")

    df["observation_count"] = df[metadata["datetime"]].apply(
        lambda row: row.count(),
        axis=1,
    )
    df["damage"] = df[metadata["datetime"]].mean(axis=1, skipna=True)

    df["damage_std"] = df[metadata["datetime"]].std(axis=1, skipna=True)
    df["damage_std"] = df["damage_std"].fillna(0).astype(float)

    building_gdf = gpd.GeoDataFrame(
        data={
            "building_id": df["building_id"].values,
            "geometry": list_of_polygons,
            "area": df["area"].values,
            "damage": df["damage"].values,
            "damage_std": df["damage_std"].values,
            "thumbnail": df["thumbnail"].values,
            "thumbnail_object": df["thumbnail_object"].values,
            "observation_count": df["observation_count"].values,
        },
    )
    building_gdf.crs = crs

    successful_object_count = len(
        [
            object_metadata
            for object_metadata in metadata["objects"].values()
            if object_metadata["success"]
        ]
    )

    logger.info(
        "{} object(s) -> {} ingested {:,} building(s) -> {:,} buildings of interest".format(
            len(metadata["objects"]),
            successful_object_count,
            total_building_count,
            len(building_gdf),
        )
    )

    bbox_gdf = gpd.GeoDataFrame(geometry=list_of_bboxes, crs=crs)

    observation_count = {
        int(key): int(value)
        for key, value in Counter(df["observation_count"].values).items()
    }
    logger.info(
        "observation counts: {}".format(
            ", ".join(
                sorted(
                    [
                        f"{rounds}X: {count}"
                        for rounds, count in observation_count.items()
                    ]
                )
            )
        )
    )

    total_bbox_area = sum(List_of_bbox_area)
    logger.info("area processed: {:,.1f} sq. km".format(total_bbox_area))

    metadata["summary"] = {
        "building_counts": {
            "all_observed": total_building_count,
            "damaged_unique": len(building_gdf),
        },
        "damage_time_series_depth": observation_count,
        "datacube_count": successful_object_count,
        "sq_km_processed": round(total_bbox_area, 2),
    }

    return df, bbox_gdf, building_gdf, metadata

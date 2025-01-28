from typing import Dict, Any, Tuple, List
import pandas as pd
from tqdm import tqdm
import geopandas as gpd
from collections import Counter
import numpy as np

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
) -> Tuple[bool, pd.DataFrame, gpd.GeoDataFrame, Dict]:
    logger.info(
        "{}.collect_analytics: damage > {:.1f}: {}{}{}".format(
            NAME,
            damage_threshold,
            f"{acq_count} acq(s)-" if acq_count != -1 else "",
            f"{building_count} buildings(s)-" if building_count != -1 else "",
            f" for {building_id}" if building_id else "",
        )
    )

    list_of_prediction_objects = mlflow.search(
        create_filter_string("contains=palisades.prediction,profile=FULL")
    )
    if acq_count != -1:
        list_of_prediction_objects = list_of_prediction_objects[:acq_count]
    logger.info(f"{len(list_of_prediction_objects)} acq(s) to process.")

    metadata: Dict[str, Any] = {
        "objects": {},
        "datetime": [],
    }
    list_of_polygons = []
    df = pd.DataFrame(
        columns=[
            "area",
            "building_id",
            "damage",
            "damage_std",
            "thumbnail",
            "thumbnail_object",
            "observation_count",
        ]
    )
    crs = ""
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
        metadata["datetime"] += [prediction_datetime]

        if prediction_datetime not in df.columns:
            df[prediction_datetime] = pd.NA
            df[f"{prediction_datetime}-thumbnail"] = pd.Series(dtype="object")
            df[f"{prediction_datetime}-object_name"] = pd.Series(dtype="object")

        if not objects.download(
            filename="analysis.gpkg",
            object_name=prediction_object_name,
        ):
            continue

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

        if "building_id" not in gdf.columns:
            logger.warning("building_id not found.")
            continue

        for _, row in tqdm(gdf.iterrows()):
            if building_id and row["building_id"] != building_id:
                continue

            if row["damage"] < damage_threshold:
                continue

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
        }
        logger.info(f"ingested {len(df):,} buildings so far...")

    metadata["datetime"] = sorted(list(set(metadata["datetime"])))

    df["observation_count"] = df[metadata["datetime"]].apply(
        lambda row: row.count(),
        axis=1,
    )
    df["damage"] = df[metadata["datetime"]].mean(axis=1, skipna=True)

    df["damage_std"] = df[metadata["datetime"]].std(axis=1, skipna=True)
    df["damage_std"].fillna(0, inplace=True)

    metadata["observation_count"] = {
        int(key): int(value)
        for key, value in Counter(df["observation_count"].values).items()
    }
    logger.info(
        "observation counts: {}".format(
            ", ".join(
                sorted(
                    [
                        f"{rounds}X: {count}"
                        for rounds, count in metadata["observation_count"].items()
                    ]
                )
            )
        )
    )

    output_gdf = gpd.GeoDataFrame(
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
    output_gdf.crs = crs

    success_count = len(
        [
            object_metadata
            for object_metadata in metadata["objects"].values()
            if object_metadata["success"]
        ]
    )
    logger.info(
        "{} object(s) -> {} ingested -> {:,} buildings(s)".format(
            len(metadata["objects"]),
            success_count,
            len(output_gdf),
        )
    )

    return True, df, output_gdf, metadata

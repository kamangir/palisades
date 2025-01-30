from blueness import module
from blue_objects import objects, file
from blue_objects.metadata import post_to_object

from palisades import NAME
from palisades.analytics.collection import collect_analytics
from palisades.analytics.logging import log_analytics
from palisades import env
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def ingest_analytics(
    object_name: str,
    acq_count: int = -1,
    building_count: int = -1,
    damage_threshold: float = env.PALISADES_DAMAGE_THRESHOLD,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.ingest_analytics -> {}".format(
            NAME,
            object_name,
        )
    )

    df, bbox_gdf, building_gdf, metadata = collect_analytics(
        acq_count=acq_count,
        building_count=building_count,
        damage_threshold=damage_threshold,
        log=log,
        verbose=verbose,
    )

    if not log_analytics(
        df=df,
        metadata=metadata,
        object_name=object_name,
    ):
        return False

    for filename, gdf in {
        "analytics": building_gdf,
        "coverage": bbox_gdf,
    }.items():
        if not file.save_geojson(
            objects.path_of(
                f"{filename}.geojson",
                object_name,
            ),
            gdf,
            log=log,
        ):
            return False

    if not file.save_csv(
        objects.path_of(
            "analytics.csv",
            object_name,
        ),
        df,
        log=log,
    ):
        return False

    return post_to_object(
        object_name,
        "analytics",
        metadata,
    )

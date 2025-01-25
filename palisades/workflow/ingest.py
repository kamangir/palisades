from blueness import module
from blue_options import string
from blue_objects.metadata import get_from_object
from blueflow.workflow.generic import Workflow

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)


def generate_ingest_workflow(
    job_name: str,
    query_object_name: str,
    datacube_ingest_options: str,
    predict_options: str,
    model_object_name: str,
    buildings_query_options: str,
    analysis_options: str,
    count: int = -1,
    do_tag: bool = True,
) -> bool:
    list_of_datacube_id = get_from_object(
        query_object_name,
        "datacube_id",
    )
    if count != -1:
        list_of_datacube_id = list_of_datacube_id[:count]

    logger.info(
        "{}.generate_ingest_workflow: {} @ {} {} {} {} {} -{}> {}".format(
            NAME,
            query_object_name,
            datacube_ingest_options,
            predict_options,
            model_object_name,
            buildings_query_options,
            analysis_options,
            "tag-" if do_tag else "",
            job_name,
        )
    )

    workflow = Workflow(
        job_name,
        name="palisades.ingest",
        args={
            "query_object_name": query_object_name,
            "datacube_ingest_options": datacube_ingest_options,
            "predict_options": predict_options,
            "model_object_name": model_object_name,
            "buildings_query_options": buildings_query_options,
            "analysis_options": analysis_options,
            "list_of_datacube_id": list_of_datacube_id,
            "do_tag": do_tag,
        },
    )

    suffix = string.pretty_date(
        as_filename=True,
        include_time=False,
        unique=True,
    )
    for index, datacube_id in enumerate(list_of_datacube_id):
        node = f"{index:04d}"

        workflow.G.add_node(node)

        prediction_object_name = f"predict-{datacube_id}-{suffix}"

        workflow.G.nodes[node]["command_line"] = " ".join(
            [
                "blueflow_workflow monitor",
                f"node={node}",
                job_name,
                "palisades_predict",
                f"tag={int(do_tag)}",
                datacube_ingest_options,
                predict_options,
                model_object_name,
                datacube_id,
                prediction_object_name,
                buildings_query_options,
                analysis_options,
            ]
        )

    return workflow.save()

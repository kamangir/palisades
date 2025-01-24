# 🧑🏽‍🚒 `palisades`

🧑🏽‍🚒 Post-disaster land Cover classification using [Semantic Segmentation](https://github.com/kamangir/roofai) on [Maxar Open Data](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) acquisitions. 

```bash
pip install palisades
```

```mermaid
graph LR
    palisades_ingest_query_ingest["palisades ingest~~- <query-object-name> scope=<scope>"]

    palisades_ingest_target_ingest["palisades ingest~~- target=<target> scope=<scope>"]

    palisades_label["palisades label offset=<offset>~~- <query-object-name>"]

    palisades_train["palisades train~~- <query-object-name> count=<count> <dataset-object-name> epochs=<5> <model-object-name>"]

    palisades_predict["palisades predict~~ingest~~- <model-object-name> <datacube-id> <prediction-object-name> country_code=<iso-code>,source=microsoft|osm|google buffer=<buffer>"]

    palisades_buildings_download_footprints["palisades buildings download_footprints filename=<filename> <input-object-name> country_code=<iso-code>,source=microsoft|osm|google <output-object-name>"]

    palisades_buildings_analyze["palisades buildings analyze buffer=<buffer> <object-name>"]

    target["🎯 target"]:::folder
    query_object["📂 query object"]:::folder
    datacube_1["🧊 datacube 1"]:::folder
    datacube_2["🧊 datacube 2"]:::folder
    datacube_3["🧊 datacube 3"]:::folder
    dataset_object["🏛️ dataset object"]:::folder
    model_object["🏛️ model object"]:::folder
    prediction_object_1["📂 prediction object 1"]:::folder
    prediction_object_2["📂 prediction object 2"]:::folder
    prediction_object_3["📂 prediction object 3"]:::folder

    query_object --> datacube_1
    query_object --> datacube_2
    query_object --> datacube_3

    model_object --> palisades_ingest_query_ingest
    query_object --> palisades_ingest_query_ingest
    palisades_ingest_query_ingest --> datacube_1
    palisades_ingest_query_ingest --> datacube_2
    palisades_ingest_query_ingest --> datacube_3
    palisades_ingest_query_ingest --> prediction_object_1
    palisades_ingest_query_ingest --> prediction_object_2
    palisades_ingest_query_ingest --> prediction_object_3

    model_object --> palisades_ingest_target_ingest
    target --> palisades_ingest_target_ingest
    palisades_ingest_target_ingest --> query_object
    palisades_ingest_target_ingest --> datacube_1
    palisades_ingest_target_ingest --> datacube_2
    palisades_ingest_target_ingest --> datacube_3
    palisades_ingest_target_ingest --> prediction_object_1
    palisades_ingest_target_ingest --> prediction_object_2
    palisades_ingest_target_ingest --> prediction_object_3

    query_object --> palisades_label
    palisades_label --> datacube_1

    query_object --> palisades_train
    palisades_train --> dataset_object
    palisades_train --> model_object

    model_object --> palisades_predict
    datacube_1 --> palisades_predict
    palisades_predict --> prediction_object_1

    prediction_object_1 --> palisades_buildings_download_footprints
    palisades_buildings_download_footprints --> prediction_object_1

    prediction_object_1 --> palisades_buildings_analyze
    palisades_buildings_analyze --> prediction_object_1

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

<details>
<summary>palisades help</summary>

--help-- palisades ingest help
--help-- palisades label help
--help-- palisades train help
--help-- palisades predict help

</details>

--table--

---

This workflow is inspired by [microsoft/building-damage-assessment](https://github.com/microsoft/building-damage-assessment) and `palisades buildings download_footprints` calls `download_building_footprints.py` from the same repo - through [satellite-image-deep-learning](https://www.satellite-image-deep-learning.com/p/building-damage-assessment).

---

--signature--
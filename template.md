# 🧑🏽‍🚒 `palisades`

🧑🏽‍🚒 Post-disaster land Cover classification using [Semantic Segmentation](https://github.com/kamangir/roofai) on [Maxar Open Data](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) acquisitions. 

```bash
pip install palisades
```

```mermaid
graph LR
    palisades_ingest_target["palisades ingest~~- target=<target>~~- predict~~-~~-~~-~~- to=<runner>"]

    palisades_ingest_query["palisades ingest~~- <query-object-name>~~- predict~~-~~-~~-~~- to=<runner>"]

    palisades_label["palisades label offset=<offset>~~- <query-object-name>"]

    palisades_train["palisades train~~- <query-object-name>~~- <dataset-object-name>~~- <model-object-name>"]

    palisades_predict["palisades predict~~-~~-~~- <model-object-name> <datacube-id> <prediction-object-name>"]

    palisades_buildings_download_footprints["palisades buildings download_footprints~~- <input-object-name>~~- <output-object-name>"]

    palisades_buildings_analyze["palisades buildings analyze~~- <prediction-object-name>"]

    palisades_analytics_ingest["palisades analytics ingest~~- <analytics-object-name>"]

    palisades_analytics_ingest_building["palisades analytics ingest_building building=<building-id> <analytics-object-name>"]

    target["🎯 target"]:::folder
    query_object["📂 query object"]:::folder
    datacube["🧊 datacube"]:::folder
    dataset_object["🏛️ dataset object"]:::folder
    model_object["🏛️ model object"]:::folder
    prediction_object["📂 prediction object"]:::folder
    analytics_object["📂 analytics object"]:::folder

    query_object --> datacube

    target --> palisades_ingest_target
    palisades_ingest_target --> palisades_ingest_query
    palisades_ingest_target --> query_object

    query_object --> palisades_ingest_query
    palisades_ingest_query --> palisades_predict

    query_object --> palisades_label
    palisades_label --> datacube

    datacube --> palisades_train
    query_object --> palisades_train
    palisades_train --> dataset_object
    palisades_train --> model_object

    model_object --> palisades_predict
    datacube --> palisades_predict
    palisades_predict --> palisades_buildings_download_footprints
    palisades_predict --> palisades_buildings_analyze
    palisades_predict --> prediction_object

    prediction_object --> palisades_buildings_download_footprints
    palisades_buildings_download_footprints --> prediction_object

    datacube --> palisades_buildings_analyze
    prediction_object --> palisades_buildings_analyze
    palisades_buildings_analyze --> prediction_object

    prediction_object --> palisades_analytics_ingest
    palisades_analytics_ingest --> analytics_object

    analytics_object --> palisades_analytics_ingest_building
    palisades_analytics_ingest_building --> analytics_object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

<details>
<summary>palisades help</summary>

--help-- palisades ingest
--help-- palisades label
--help-- palisades train
--help-- palisades predict
--help-- palisades analytics

</details>

--table--

## Acknowledgments
 
1. The concept and workflow of this tool is heavily affected by [microsoft/building-damage-assessment](https://github.com/microsoft/building-damage-assessment).
2. `palisades buildings download_footprints` calls [`download_building_footprints.py`](https://github.com/microsoft/building-damage-assessment/blob/main/download_building_footprints.py).
3. `palisades buildings analyze` is based on [`merge_with_building_footprints.py`](https://github.com/microsoft/building-damage-assessment/blob/main/merge_with_building_footprints.py).
4. Through [satellite-image-deep-learning](https://www.satellite-image-deep-learning.com/p/building-damage-assessment).

---

--signature--
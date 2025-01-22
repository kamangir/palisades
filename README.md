# 🧑🏽‍🚒 `palisades`: Post-Disaster Land Cover Classification

[Semantic Segmentation](https://github.com/kamangir/roofai) on [Maxar Open Data](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) acquisitions. 

```mermaid
graph LR
    palisades_ingest_query_ingest["palisades<br>ingest -<br>&lt;query-object-name&gt;<br>scope=&lt;scope&gt;"]

    palisades_ingest_target["palisades<br>ingest -<br>target=&lt;target&gt;<br>~ingest_datacubes"]

    palisades_ingest_target_ingest["palisades<br>ingest -<br>target=&lt;target&gt;<br>scope=&lt;scope&gt;"]

    palisades_label["palisades<br>label<br>offset=&lt;offset&gt; -<br>&lt;query-object-name&gt;"]

    palisades_train["palisades<br>train -<br>&lt;query-object-name&gt;<br>count=&lt;count&gt;<br>&lt;dataset-object-name&gt;<br>epochs=&lt;5&gt;<br>&lt;model-object-name&gt;"]

    palisades_predict["palisades<br>predict ingest -<br>&lt;model-object-name&gt;<br>&lt;datacube-id&gt;<br>&lt;prediction-object-name&gt;"]

    target["🎯 target"]:::folder
    query_object["📂 query object"]:::folder
    datacube_1["🧊 datacube 1"]:::folder
    datacube_2["🧊 datacube 2"]:::folder
    datacube_3["🧊 datacube 3"]:::folder
    dataset_object["🏛️ dataset object"]:::folder
    model_object["🏛️ model object"]:::folder
    prediction_object["📂 prediction object"]:::folder

    query_object --> datacube_1
    query_object --> datacube_2
    query_object --> datacube_3

    query_object --> palisades_ingest_query_ingest
    palisades_ingest_query_ingest --> datacube_1
    palisades_ingest_query_ingest --> datacube_2
    palisades_ingest_query_ingest --> datacube_3

    target --> palisades_ingest_target
    palisades_ingest_target --> query_object

    target --> palisades_ingest_target_ingest
    palisades_ingest_target_ingest --> query_object
    palisades_ingest_target_ingest --> datacube_1
    palisades_ingest_target_ingest --> datacube_2
    palisades_ingest_target_ingest --> datacube_3

    query_object --> palisades_label
    palisades_label --> datacube_1

    query_object --> palisades_train
    palisades_train --> dataset_object
    palisades_train --> model_object

    model_object --> palisades_predict
    datacube_1 --> palisades_predict
    palisades_predict --> prediction_object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

<details>
<summary>palisades help</summary>

--help-- palisades ingest help
--help-- palisades label help
--help-- palisades train help
--help-- palisades predict help

</details>

|   |   |
| --- | --- |
| 🌐[`STAC Catalog: Maxar Open Data`](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) [![image](https://github.com/kamangir/assets/blob/main/blue-geo/Maxar-Open-Datacube.png?raw=true)](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) ["Satellite imagery for select sudden onset major crisis events"](https://www.maxar.com/open-data/) | 🏛️[`Algo: Semantic Segmentation`](https://github.com/kamangir/palisades/blob/main/palisades/docs/step-by-step.md) [![image](https://github.com/kamangir/assets/raw/main/palisades/prediction.png?raw=true)](https://github.com/kamangir/palisades/blob/main/palisades/docs/step-by-step.md) [segmentation_models.pytorch](https://github.com/qubvel-org/segmentation_models.pytorch) |

---


[![pylint](https://github.com/kamangir/palisades/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/palisades/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/palisades/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/palisades/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/palisades/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/palisades/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/palisades.svg)](https://pypi.org/project/palisades/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/palisades)](https://pypistats.org/packages/palisades)

built by 🌀 [`blue_options-4.192.1`](https://github.com/kamangir/awesome-bash-cli), based on 🧑🏽‍🚒 [`palisades-4.21.1`](https://github.com/kamangir/palisades).

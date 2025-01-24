# 🧑🏽‍🚒 `palisades`

🧑🏽‍🚒 Post-disaster land Cover classification using [Semantic Segmentation](https://github.com/kamangir/roofai) on [Maxar Open Data](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) acquisitions. 

```bash
pip install palisades
```

```mermaid
graph LR
    palisades_ingest_query_ingest["palisades<br>ingest -<br>&lt;query-object-name&gt;<br>scope=&lt;scope&gt;"]

    palisades_ingest_target_ingest["palisades<br>ingest -<br>target=&lt;target&gt;<br>scope=&lt;scope&gt;"]

    palisades_label["palisades<br>label<br>offset=&lt;offset&gt; -<br>&lt;query-object-name&gt;"]

    palisades_train["palisades<br>train -<br>&lt;query-object-name&gt;<br>count=&lt;count&gt;<br>&lt;dataset-object-name&gt;<br>epochs=&lt;5&gt;<br>&lt;model-object-name&gt;"]

    palisades_predict["palisades<br>predict ingest -<br>&lt;model-object-name&gt;<br>&lt;datacube-id&gt;<br>&lt;prediction-object-name&gt;<br>country_code=&lt;iso-code&gt;,source=microsoft|osm|google<br>buffer=&lt;buffer&gt;"]

    palisades_buildings_download_footprints["palisades<br>buildings<br>download_footprints<br>filename=&lt;filename&gt;<br>&lt;input-object-name&gt;<br>country_code=&lt;iso-code&gt;,source=microsoft|osm|google<br>&lt;output-object-name&gt;"]

    palisades_buildings_analyze["palisades<br>buildings<br>analyze<br>buffer=&lt;buffer&gt;<br>&lt;object-name&gt;"]

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

    prediction_object --> palisades_buildings_download_footprints
    palisades_buildings_download_footprints --> prediction_object

    prediction_object --> palisades_buildings_analyze
    palisades_buildings_analyze --> prediction_object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

<details>
<summary>palisades help</summary>

```bash
palisades \
	ingest \
	[~download,dryrun] \
	[target=<target> | <query-object-name>] \
	[~ingest_datacubes | ~copy_template,dryrun,overwrite,scope=<scope>,upload]
 . ingest <target>.
   target: Brown-Mountain-Truck-Trail | Brown-Mountain-Truck-Trail-all | Brown-Mountain-Truck-Trail-test | Palisades-Maxar | Palisades-Maxar-test
   scope: all + metadata + raster + rgb + rgbx + <.jp2> + <.tif> + <.tiff>
      all: ALL files.
      metadata (default): any < 1 MB.
      raster: all raster.
      rgb: rgb.
      rgbx: rgb and what is needed to build rgb.
      <suffix>: any *<suffix>.
```
```bash
palisades \
	label \
	[download,offset=<offset>] \
	[~download,dryrun,~QGIS,~rasterize,~sync,upload] \
	[.|<query-object-name>]
 . label <query-object-name>.
```
```bash
palisades \
	train \
	[dryrun,~download,review] \
	[.|<query-object-name>] \
	[count=<10000>,dryrun,upload] \
	[-|<dataset-object-name>] \
	[device=<device>,dryrun,profile=<profile>,upload,epochs=<5>] \
	[-|<model-object-name>]
 . train palisades.
   device: cpu | cuda
   profile: FULL | DECENT | QUICK | DEBUG | VALIDATION
```
```bash
palisades \
	predict \
	[ingest,~tag] \
	[device=<device>,~download,dryrun,profile=<profile>,upload] \
	[-|<model-object-name>] \
	[.|<datacube-id>] \
	[-|<prediction-object-name>] \
	[~download_footprints | country_code=<iso-code>,country_name=<country-name>,overwrite,source=<source>] \
	[~analyze | buffer=<buffer>]
 . <datacube-id> -<model-object-name>-> <prediction-object-name>
   device: cpu | cuda
   profile: FULL | DECENT | QUICK | DEBUG | VALIDATION
   country-name: for Microsoft, optional, overrides <iso-code>.
   iso-code: Country Alpha2 ISO code: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
      Canada: CA
      US: US
   source: microsoft | osm | google
   calls: https://github.com/microsoft/building-damage-assessment/blob/main/download_building_footprints.py
   buffer: in meters.
```

</details>

|   |   |   |
| --- | --- | --- |
| 🌐[`STAC Catalog: Maxar Open Data`](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) [![image](https://github.com/kamangir/assets/blob/main/blue-geo/Maxar-Open-Datacube.png?raw=true)](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) ["Satellite imagery for select sudden onset major crisis events"](https://www.maxar.com/open-data/) | 🏛️[`Vision Algo: Semantic Segmentation`](https://github.com/kamangir/palisades/blob/main/palisades/docs/step-by-step.md) [![image](https://github.com/kamangir/assets/raw/main/palisades/prediction-lres.png?raw=true)](https://github.com/kamangir/palisades/blob/main/palisades/docs/step-by-step.md) [segmentation_models.pytorch](https://github.com/qubvel-org/segmentation_models.pytorch) | 🧑🏽‍🚒[`Analytics: Building Damage`](https://github.com/kamangir/palisades/blob/main/palisades/docs/building-analysis.md) [![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2.png?raw=true)](https://github.com/kamangir/palisades/blob/main/palisades/docs/building-analysis.md) Microsoft, OSM, and Google footprints through [microsoft/building-damage-assessment](https://github.com/microsoft/building-damage-assessment) |

---

This workflow is inspired by [microsoft/building-damage-assessment](https://github.com/microsoft/building-damage-assessment) and `palisades buildings download_footprints` calls `download_building_footprints.py` from the same repo - through [satellite-image-deep-learning](https://www.satellite-image-deep-learning.com/p/building-damage-assessment).

---


[![pylint](https://github.com/kamangir/palisades/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/palisades/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/palisades/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/palisades/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/palisades/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/palisades/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/palisades.svg)](https://pypi.org/project/palisades/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/palisades)](https://pypistats.org/packages/palisades)

built by 🌀 [`blue_options-4.197.1`](https://github.com/kamangir/awesome-bash-cli), based on 🧑🏽‍🚒 [`palisades-4.82.1`](https://github.com/kamangir/palisades).

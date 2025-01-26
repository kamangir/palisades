# Damage Analytics

<details>
<summary>🎯 target: Altadena</summary>

```yaml
Altadena:
  catalog: maxar_open_data
  collection: collection
  params:
    height: 0.025
    width: 0.05
  query_args:
    count: 10
    collection_id: WildFires-LosAngeles-Jan-2025
    lat: 34.188611
    lon: -118.134722
    start_date: 2025-01-01
    end_date: 2025-02-01
  urls:
    wikipedia: https://en.wikipedia.org/wiki/Altadena,_California
  versions:
    test:
      query_args:
        count: 2
```

</details>


```bash
palisades ingest - target=Altadena
```

<details>
<summary>🧊 10 datacubes</summary>

```yaml
datacube_id:
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010B698000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010C487900
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-103001010C487900
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-10400100A07CE400
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-10400100A07CE400
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-10400100A17E8600
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-10400100A17E8600
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-10400100A26E9900
kind: distributed
module_name: blue_geo.catalog.maxar_open_data.collection
source: catalog_query
```

</details>

---

```bash
@select datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010B698000
@datacube ingest scope=rgb .
@open QGIS .
```

![image](https://github.com/kamangir/assets/blob/main/palisades/analytics-3.png?raw=true)

---

```bash
palisades ingest analytics ~upload
```

[palisades-analytics-2025-01-25-23-23-42-i35w48](https://kamangir-public.s3.ca-central-1.amazonaws.com/palisades-analytics-2025-01-25-23-23-42-i35w48.tar.gz)

```yaml
'2025-01-14T18:30:58Z':
  area: 404.2871296405792
  damage: 0.0
  object_name: predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C7D2D00-2025-01-24-3w93qm
  thumbnail: thumbnail-11-031311102213-103001010C7D2D00-103001010C7D2D00-visual-prediction-000836.png
'2025-01-14T18:36:40Z':
  area: 404.2871296405792
  damage: 0.0
  object_name: predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-10400100A06B8000-2025-01-24-kj6wsu
  thumbnail: thumbnail-11-031311102213-10400100A06B8000-10400100A06B8000-visual-prediction-000836.png
'2025-01-16T18:58:02Z':
  area: 404.2871296405792
  damage: 0.0
  object_name: predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C12B000-2025-01-24-511jt9
  thumbnail: thumbnail-11-031311102213-103001010C12B000-103001010C12B000-visual-prediction-000836.png
```

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-25-23-23-42-i35w48/thumbnail-035511-377166-palisades-analytics-2025-01-25-23-23-42-i35w48.gif?raw=true)

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-25-23-23-42-i35w48/thumbnail-035584-377098-palisades-analytics-2025-01-25-23-23-42-i35w48.gif?raw=true)

🔥

---

🚧


```bash
@batch eval - \
  palisades ingest - \
  target=Altadena \
  scope=rgb \
  predict,count=3 \
  profile=FULL,upload - - - \
  to=aws_batch
```

🚧

---

also see: [round one](./damage-analytics-round-one.md)

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

🔥

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

```bash
palisades ingest analytics \
    TBA
```

---

also see: [round one](./damage-analytics-round-one.md)
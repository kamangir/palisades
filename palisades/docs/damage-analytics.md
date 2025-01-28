# Damage Analytics

- [round one](./damage-analytics-round-one.md)
- [round two](./damage-analytics-round-two.md)
- [round three](./damage-analytics-round-three.md)
- [round four](./damage-analytics-round-four.md)


## 1️⃣ adding the 🎯 target: LA,

```yaml
LA:
  catalog: maxar_open_data
  collection: collection
  params:
    height: 0.5
    width: 1
  query_args:
    count: 100
    collection_id: WildFires-LosAngeles-Jan-2025
    lat: 34.0549
    lon: -118.2426
    radius: 1
    start_date: 2025-01-01
    end_date: 2025-02-01
  urls:
    wikipedia: https://en.wikipedia.org/wiki/January_2025_Southern_California_wildfires, January 2025 Southern California wildfires
    calfire: https://www.fire.ca.gov/incidents/2025/1/7/palisades-fire
    "3d map": https://calfire-forestry.maps.arcgis.com/home/webscene/viewer.html?webscene=0a7381c8b46b4e26a057383424f32c06
  versions:
    test:
      query_args:
        count: 2
```

## 2️⃣ reviewing the target,

```bash
palisades ingest - target=LA
```

<details>
<summary>🧊 100 datacubes</summary>

```yaml
datacube_id:
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010B698000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100221-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100223-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100230-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100231-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100232-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100233-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100320-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100322-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102001-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102003-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102010-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102011-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102012-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102013-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102021-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102023-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102030-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102031-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102032-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102033-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102100-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102102-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102120-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102122-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102201-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102203-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102210-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102211-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102221-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102230-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102231-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102232-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102233-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102300-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102302-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102320-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102322-103001010B9A1B00
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100223-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100230-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100231-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100232-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100233-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100320-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100322-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100323-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100332-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102001-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102003-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102010-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102011-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102012-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102013-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102021-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102023-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102030-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102031-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102032-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102033-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102100-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102101-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102102-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102103-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102110-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102112-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102120-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102121-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102122-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102123-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102130-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102201-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102203-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102210-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102211-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102221-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102230-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102231-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102300-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102301-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102302-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102303-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102320-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102321-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102322-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102323-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311120101-103001010C12B000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103030-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103031-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103120-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103122-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103210-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103211-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103300-103001010C360000
- datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103030-103001010C487900
kind: distributed
module_name: blue_geo.catalog.maxar_open_data.collection
source: catalog_query
```

</details>

## 3️⃣ ingesting from the target,

```bash
@batch eval - \
  palisades ingest - \
  target=LA \
  scope=rgb \
  predict \
  profile=FULL,upload - - - \
  to=aws_batch
```

🎰

## 4️⃣ ingesting analytics,

🚧

```bash
palisades analytics ingest upload
```

:::TBA

## 5️⃣ ingesting one building,

🚧

```bash
palisades analytics ingest_building \
  building=<...>,~download \
  <...>
```

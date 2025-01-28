# Damage Analytics

- [round one](./damage-analytics-round-one.md)
- [round two](./damage-analytics-round-two.md)
- [round three](./damage-analytics-round-three.md)
- [round four](./damage-analytics-round-four.md)


## 1️⃣ 🎯 adding the target: LA,

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

## 4️⃣ reviewing the predicts,

```bash
@mlflow tags search \
  contains=palisades.prediction,model=$PALISADES_DEFAULT_FIRE_MODEL,profile=FULL
```

<details>
<summary>🌀  113 object(s)</summary>

```
🌀  #   1 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102323-103001010C12B000-2025-01-27-6k9ypd
🌀  #   2 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103211-103001010C360000-2025-01-27-6k9ypd
🌀  #   3 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103300-103001010C360000-2025-01-27-6k9ypd
🌀  #   4 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102321-103001010C12B000-2025-01-27-6k9ypd
🌀  #   5 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103210-103001010C360000-2025-01-27-6k9ypd
🌀  #   6 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102123-103001010C12B000-2025-01-27-6k9ypd
🌀  #   7 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102320-103001010C12B000-2025-01-27-6k9ypd
🌀  #   8 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103122-103001010C360000-2025-01-27-6k9ypd
🌀  #   9 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102121-103001010C12B000-2025-01-27-6k9ypd
🌀  #  10 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311120101-103001010C12B000-2025-01-27-6k9ypd
🌀  #  11 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103030-103001010C487900-2025-01-27-6k9ypd
🌀  #  12 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102322-103001010C12B000-2025-01-27-6k9ypd
🌀  #  13 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103120-103001010C360000-2025-01-27-6k9ypd
🌀  #  14 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102102-103001010C12B000-2025-01-27-6k9ypd
🌀  #  15 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102130-103001010C12B000-2025-01-27-6k9ypd
🌀  #  16 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103030-103001010C360000-2025-01-27-6k9ypd
🌀  #  17 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102122-103001010C12B000-2025-01-27-6k9ypd
🌀  #  18 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102033-103001010C12B000-2025-01-27-6k9ypd
🌀  #  19 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102103-103001010C12B000-2025-01-27-6k9ypd
🌀  #  20 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102030-103001010C12B000-2025-01-27-6k9ypd
🌀  #  21 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102120-103001010C12B000-2025-01-27-6k9ypd
🌀  #  22 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102301-103001010C12B000-2025-01-27-6k9ypd
🌀  #  23 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102302-103001010C12B000-2025-01-27-6k9ypd
🌀  #  24 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102303-103001010C12B000-2025-01-27-6k9ypd
🌀  #  25 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102032-103001010C12B000-2025-01-27-6k9ypd
🌀  #  26 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102031-103001010C12B000-2025-01-27-6k9ypd
🌀  #  27 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102101-103001010C12B000-2025-01-27-6k9ypd
🌀  #  28 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102300-103001010C12B000-2025-01-27-6k9ypd
🌀  #  29 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102231-103001010C12B000-2025-01-27-6k9ypd
🌀  #  30 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102210-103001010C12B000-2025-01-27-6k9ypd
🌀  #  31 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102201-103001010C12B000-2025-01-27-6k9ypd
🌀  #  32 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102211-103001010C12B000-2025-01-27-6k9ypd
🌀  #  33 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102112-103001010C12B000-2025-01-27-6k9ypd
🌀  #  34 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103031-103001010C360000-2025-01-27-6k9ypd
🌀  #  35 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102221-103001010C12B000-2025-01-27-6k9ypd
🌀  #  36 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102230-103001010C12B000-2025-01-27-6k9ypd
🌀  #  37 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102320-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  38 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102013-103001010C12B000-2025-01-27-6k9ypd
🌀  #  39 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102012-103001010C12B000-2025-01-27-6k9ypd
🌀  #  40 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102023-103001010C12B000-2025-01-27-6k9ypd
🌀  #  41 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102100-103001010C12B000-2025-01-27-6k9ypd
🌀  #  42 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102203-103001010C12B000-2025-01-27-6k9ypd
🌀  #  43 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102110-103001010C12B000-2025-01-27-6k9ypd
🌀  #  44 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102021-103001010C12B000-2025-01-27-6k9ypd
🌀  #  45 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102011-103001010C12B000-2025-01-27-6k9ypd
🌀  #  46 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100320-103001010C12B000-2025-01-27-6k9ypd
🌀  #  47 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102322-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  48 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102003-103001010C12B000-2025-01-27-6k9ypd
🌀  #  49 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100231-103001010C12B000-2025-01-27-6k9ypd
🌀  #  50 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100233-103001010C12B000-2025-01-27-6k9ypd
🌀  #  51 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102300-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  52 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102001-103001010C12B000-2025-01-27-6k9ypd
🌀  #  53 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100230-103001010C12B000-2025-01-27-6k9ypd
🌀  #  54 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102302-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  55 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100332-103001010C12B000-2025-01-27-6k9ypd
🌀  #  56 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102031-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  57 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102010-103001010C12B000-2025-01-27-6k9ypd
🌀  #  58 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102032-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  59 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100322-103001010C12B000-2025-01-27-6k9ypd
🌀  #  60 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100323-103001010C12B000-2025-01-27-6k9ypd
🌀  #  61 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100232-103001010C12B000-2025-01-27-6k9ypd
🌀  #  62 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102102-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  63 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102013-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  64 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102033-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  65 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102120-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  66 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102030-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  67 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102122-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  68 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102012-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  69 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102231-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  70 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102023-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  71 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100231-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  72 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102021-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  73 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100320-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  74 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102210-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  75 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102230-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  76 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102100-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  77 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100223-103001010C12B000-2025-01-27-6k9ypd
🌀  #  78 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102211-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  79 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102003-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  80 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102203-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  81 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102221-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  82 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102201-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  83 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102233-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  84 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100232-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  85 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100230-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  86 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102011-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  87 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100233-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  88 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100221-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  89 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102010-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  90 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102001-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  91 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100322-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  92 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102232-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  93 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311100223-103001010B9A1B00-2025-01-27-6k9ypd
🌀  #  94 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-103001010C487900-2025-01-26-280h2r
🌀  #  95 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-10400100A17E8600-2025-01-26-280h2r
🌀  #  96 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-10400100A26E9900-2025-01-26-280h2r
🌀  #  97 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-10400100A07CE400-2025-01-26-280h2r
🌀  #  98 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010C487900-2025-01-26-280h2r
🌀  #  99 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-10400100A17E8600-2025-01-26-280h2r
🌀  # 100 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-10400100A07CE400-2025-01-26-280h2r
🌀  # 101 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-10400100A0B73800-2025-01-26-2asv6z
🌀  # 102 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00-2025-01-26-2asv6z
🌀  # 103 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103033-103001010C360000-2025-01-26-wziu43
🌀  # 104 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010B698000-2025-01-26-wziu43
🌀  # 105 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103032-103001010C360000-2025-01-26-wziu43
🌀  # 106 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C7D2D00-2025-01-24-3zydh4
🌀  # 107 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C12B000-2025-01-24-511jt9
🌀  # 108 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C7D2D00-2025-01-24-3w93qm
🌀  # 109 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C12B000-2025-01-24-j9xcil
🌀  # 110 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-10400100A06B8000-2025-01-24-mo3sod
🌀  # 111 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-10400100A06B8000-2025-01-24-kj6wsu
🌀  # 112 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010B9A1B00-2025-01-24-k0mdhu
🌀  # 113 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C7DD700-2025-01-24-5ferpu
```

</details>

## 5️⃣ ingesting analytics,

🔥

```bash
palisades analytics ingest upload
```

:::palisades-analytics-2025-01-27-20-55-12-6qykkv

🔥

## 6️⃣ ingesting one building,

🚧

```bash
palisades analytics ingest_building \
  building=<...>,deep,~download \
  <...>
```

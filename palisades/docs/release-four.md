# release four

```bash
@batch eval - \
  palisades ingest - \
  target=LA-250 \
  scope=rgb \
  predict \
  profile=FULL,upload - - - \
  to=aws_batch
```

```bash
@select palisades-release-four-$(@@timestamp)

palisades analytics ingest upload .

@open QGIS .

@assets publish push .
@publish tar .
```


[palisades-release-four-2025-01-30-uglnpq](https://kamangir-public.s3.ca-central-1.amazonaws.com/palisades-release-four-2025-01-30-uglnpq.tar.gz)

coverage: [coverage.geojson](https://github.com/kamangir/assets/blob/main/palisades-release-four-2025-01-30-uglnpq/coverage.geojson)

![image](https://github.com/kamangir/assets/blob/main/palisades-release-four-2025-01-30-uglnpq/QGIS.png?raw=true)

```yaml
building_counts:
  all_observed: 2406272
  damaged_unique: 10797
damage_time_series_depth:
  1: 1706
  2: 1477
  3: 2417
  4: 800
  5: 1657
  6: 2370
  7: 348
  8: 22
datacube_count: 239
sq_km_processed: 5858.57

```

![image](https://github.com/kamangir/assets/blob/main/palisades-release-four-2025-01-30-uglnpq/damage-history.png?raw=true)

---

🎯 Target List: [blue-geo-target-list-v1](https://kamangir-public.s3.ca-central-1.amazonaws.com/blue-geo-target-list-v1.tar.gz)

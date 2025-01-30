# release four 🎰

```bash
@batch eval - \
  palisades ingest - \
  target=LA-250 \
  scope=rgb \
  predict \
  profile=FULL,upload - - - \
  to=aws_batch
```

🎰

```bash
@select palisades-release-four-$(@@timestamp)

palisades analytics ingest upload .

@open QGIS .

@assets publish push .
@publish tar .
```


[palisades-release-four-2025-01-30-jqnc4l](https://kamangir-public.s3.ca-central-1.amazonaws.com/palisades-release-four-2025-01-30-jqnc4l.tar.gz)

coverage: [coverage.geojson](https://github.com/kamangir/assets/blob/main/palisades-release-four-2025-01-30-jqnc4l/coverage.geojson)

```yaml
building_counts:
  all_observed: 1501023
  damaged_unique: 10594
damaged_building_observation_count:
  1: 1863
  2: 1605
  3: 3325
  4: 3212
  5: 474
  6: 25
  7: 75
  8: 15
datacube_count: 156
sq_km_processed: 3774.18

```

![image](https://github.com/kamangir/assets/blob/main/palisades-release-four-2025-01-30-jqnc4l/damage-history.png?raw=true)

---

🎯 Target List: [blue-geo-target-list-v1](https://kamangir-public.s3.ca-central-1.amazonaws.com/blue-geo-target-list-v1.tar.gz)

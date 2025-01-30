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


[palisades-release-four-2025-01-30-1mgq3d](https://kamangir-public.s3.ca-central-1.amazonaws.com/palisades-release-four-2025-01-30-1mgq3d.tar.gz)

coverage: [coverage.geojson](https://github.com/kamangir/assets/blob/main/palisades-release-four-2025-01-30-1mgq3d/coverage.geojson)

```yaml
building_counts:
  all_observed: 1148351
  damaged_unique: 10133
damaged_building_observation_count:
  1: 1864
  2: 5799
  3: 1722
  4: 294
  5: 339
  6: 25
  7: 90
datacube_count: 108
sq_km_processed: 2685.88

```

![image](https://github.com/kamangir/assets/blob/main/palisades-release-four-2025-01-30-1mgq3d/damage-history.png?raw=true)

---

🎯 Target List: [blue-geo-target-list-v1](https://kamangir-public.s3.ca-central-1.amazonaws.com/blue-geo-target-list-v1.tar.gz)

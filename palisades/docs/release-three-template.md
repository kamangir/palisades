# release three

```bash
@select palisades-release-three-$(@@timestamp)

palisades analytics ingest upload .

@open QGIS .
code metadata.yaml

@assets publish push .
@publish tar .
```

set:::object_name palisades-release-three-2025-01-29-k3drbd

object:::get:::object_name

coverage: assets:::get:::object_name/coverage.geojson

```yaml
damaged_building_count: 10133
datacube_count: 108
observation_count:
    1: 1864
    2: 5799
    3: 1722
    4: 294
    5: 339
    6: 25
    7: 90
total_building_count: 1148351
```

assets:::get:::object_name/damage-history.png

---

🎯 Target List: object:::blue-geo-target-list-v1
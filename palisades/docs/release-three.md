# release three

```bash
@select palisades-release-three-$(@@timestamp)

palisades analytics ingest upload .

@open QGIS .
code metadata.yaml

@assets publish push .
@publish tar .
```


[palisades-release-three-2025-01-29-k3drbd](https://kamangir-public.s3.ca-central-1.amazonaws.com/palisades-release-three-2025-01-29-k3drbd.tar.gz)

coverage: [coverage.geojson](https://github.com/kamangir/assets/blob/main/palisades-release-three-2025-01-29-k3drbd/coverage.geojson)

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

![image](https://github.com/kamangir/assets/blob/main/palisades-release-three-2025-01-29-k3drbd/damage-history.png?raw=true)

---

🎯 Target List: [blue-geo-target-list-v1](https://kamangir-public.s3.ca-central-1.amazonaws.com/blue-geo-target-list-v1.tar.gz)

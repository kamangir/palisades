# building analysis

🔥

```bash
@select building-analysis-$(@@timestamp)

palisades predict ingest \
    profile=FULL,~upload - \
    $PALISADES_TEST_DATACUBE . \
    country_code=US,source=microsoft

@open QGIS .
```

🚧

copy, give credit, and refactor merge_with_building_footprints.py

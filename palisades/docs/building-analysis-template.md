# building analysis

🔥

```bash
@select building-analysis-$(@@timestamp)

palisades predict ingest \
	profile=VALIDATION,~upload - \
	datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00 . \
	country_code=US,source=microsoft

@open QGIS .
```

🚧

copy, give credit, and refactor merge_with_building_footprints.py
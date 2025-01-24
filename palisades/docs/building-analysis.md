# building analysis: dev

```bash
@select building-analysis-$(@@timestamp)

palisades predict ingest \
    profile=FULL,~upload - \
    $PALISADES_TEST_DATACUBE . \
    country_code=US,source=microsoft
```

```bash
@select building-analysis-2025-01-23-mdtggz
@download - . open,QGIS
```

```python
palisades.load
```

![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2.png?raw=true)


[building-analysis-2025-01-23-mdtggz](https://kamangir-public.s3.ca-central-1.amazonaws.com/building-analysis-2025-01-23-mdtggz.tar.gz)
🔥

```bash
palisades buildings analyze - .
```


🚧

copy, give credit, and refactor merge_with_building_footprints.py


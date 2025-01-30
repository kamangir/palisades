# Building Damage Analysis

```bash
@select building-analysis-$(@@timestamp)

palisades predict ingest \
    profile=FULL - \
    $PALISADES_TEST_DATACUBE .
```

```bash
@select building-analysis-2025-01-23-mdtggz
@download - . open,QGIS
```

```python
palisades.load
```

assets:::palisades/building-analysis-4.png

| Damaged | Not Damaged |
|-|-|
| assets:::palisades/building-analysis-2025-01-23-mdtggz/thumbnail-11-031311102213-103001010B9A1B00-103001010B9A1B00-visual-prediction000289.png | assets:::palisades/building-analysis-2025-01-23-mdtggz/thumbnail-11-031311102213-103001010B9A1B00-103001010B9A1B00-visual-prediction000339.png |


| | |
|-|-|
| assets:::palisades/building-analysis-2025-01-23-mdtggz/area-damage-histogram.png | assets:::palisades/building-analysis-2025-01-23-mdtggz/area-damage-scatter.png |


object:::building-analysis-2025-01-23-mdtggz

assets:::palisades/building-analysis-3.png

✅
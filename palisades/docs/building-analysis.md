# building analysis

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

![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-4.png?raw=true)

| Damaged | Not Damaged |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/thumbnail-11-031311102213-103001010B9A1B00-103001010B9A1B00-visual-prediction000289.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/thumbnail-11-031311102213-103001010B9A1B00-103001010B9A1B00-visual-prediction000339.png?raw=true) |


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/area-damage-histogram.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/area-damage-scatter.png?raw=true) |


[building-analysis-2025-01-23-mdtggz](https://kamangir-public.s3.ca-central-1.amazonaws.com/building-analysis-2025-01-23-mdtggz.tar.gz)

![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-3.png?raw=true)

✅

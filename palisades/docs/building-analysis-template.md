# building analysis: dev

```bash
@select building-analysis-$(@@timestamp)

palisades predict ingest \
    profile=FULL - \
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

| Damaged | Not Damaged |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/thumbnail-11-031311102213-103001010B9A1B00-103001010B9A1B00-visual-prediction000075.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/thumbnail-11-031311102213-103001010B9A1B00-103001010B9A1B00-visual-prediction000255.png?raw=true) |


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/area-damage-histogram.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/palisades/building-analysis-2025-01-23-mdtggz/area-damage-scatter.png?raw=true) |


object:::building-analysis-2025-01-23-mdtggz

🔥

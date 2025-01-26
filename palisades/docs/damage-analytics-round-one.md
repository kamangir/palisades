# Damage Analytics - Round One

## 1️⃣ ingesting a few datacubes from a target,

```bash
palisades ingest - \
    target=Palisades-Maxar \
    scope=rgb \
    predict \
    profile=FULL,upload
```

## 2️⃣ finding the predictions in mlflow,

```bash
@mlflow tags search \
    contains=palisades.prediction,profile=FULL
```
```bash
🌀  12 object(s).
🌀  #   1 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C7DD700-2025-01-24-5ferpu
🌀  #   2 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-10400100A06B8000-2025-01-24-kj6wsu
🌀  #   3 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010B9A1B00-2025-01-24-k0mdhu
🌀  #   4 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-10400100A06B8000-2025-01-24-mo3sod
🌀  #   5 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C12B000-2025-01-24-j9xcil
🌀  #   6 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C7D2D00-2025-01-24-3w93qm
🌀  #   7 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C7D2D00-2025-01-24-3zydh4
🌀  #   8 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C12B000-2025-01-24-511jt9
🌀  #   9 - building-analysis-2025-01-23-mdtggz
🌀  #  10 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-10400100A0B73800-2025-01-21-jeko6i
🌀  #  11 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00-2025-01-21-lhnxrc
🌀  #  12 - predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00-2025-01-21-za5ba5
```

## 3️⃣ reviewing one prediction,

```bash
@download - \
    predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C7D2D00-2025-01-24-3zydh4 \
    open,QGIS
```

```python
palisades.load
```

![image](https://github.com/kamangir/assets/blob/main/palisades/analytics-1.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/palisades/analytics-2.png?raw=true)

[predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C7D2D00-2025-01-24-3zydh4](https://kamangir-public.s3.ca-central-1.amazonaws.com/predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-103001010C7D2D00-2025-01-24-3zydh4.tar.gz)

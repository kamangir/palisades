# Damage Analytics

- [round one](./damage-analytics-round-one.md)
- [round two](./damage-analytics-round-two.md)
- [round two](./damage-analytics-round-three.md)

## 1️⃣ ingesting from the target,

```bash
@batch eval - \
  palisades ingest - \
  target=Altadena \
  scope=rgb \
  predict,count=3 \
  profile=FULL,upload - - - \
  to=aws_batch
```

🎰

## 2️⃣  ingesting analytics,

🔥

```bash
palisades analytics ingest upload
```

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-26-18-10-00-b4q5wj/damage-history.png?raw=true)


```bash
@download - \
  palisades-analytics-2025-01-26-17-13-55-jl0par \
  open,QGIS
```

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-26-17-13-55-jl0par/QGIS.png?raw=true)


```yaml
    035521-377202:
      '2025-01-14T18:30:58Z':
        area: 570.9007382392883
        damage: 0.31322067975997925
        object_name: predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C7D2D00-2025-01-24-3w93qm
        thumbnail: thumbnail-11-031311102213-103001010C7D2D00-103001010C7D2D00-visual-prediction-000690.png
      '2025-01-14T18:36:40Z':
        area: 570.9007382392883
        damage: 0.18017107248306274
        object_name: predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-10400100A06B8000-2025-01-24-kj6wsu
        thumbnail: thumbnail-11-031311102213-10400100A06B8000-10400100A06B8000-visual-prediction-000690.png
      '2025-01-16T18:58:02Z':
        area: 570.9007382392883
        damage: 0.35183247923851013
        object_name: predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010C12B000-2025-01-24-511jt9
        thumbnail: thumbnail-11-031311102213-103001010C12B000-103001010C12B000-visual-prediction-000690.png
```

```bash
palisades analytics render \
  building=035501-377213,~download \
  palisades-analytics-2025-01-26-17-13-55-jl0par
```

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-26-17-13-55-jl0par/thumbnail-035521-377202-palisades-analytics-2025-01-26-17-13-55-jl0par.gif?raw=true)


object:::palisades-analytics-2025-01-26-18-10-00-b4q5wj
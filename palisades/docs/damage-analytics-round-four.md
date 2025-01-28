# Damage Analytics - Round Four

- [round one](./damage-analytics-round-one.md)
- [round two](./damage-analytics-round-two.md)
- [round three](./damage-analytics-round-three.md)

## 1️⃣ ingesting from the target,

```bash
@batch eval - \
  palisades ingest - \
  target=Altadena \
  scope=rgb \
  predict \
  profile=FULL,upload - - - \
  to=aws_batch
```

also for `Palisades-Maxar`.

## 2️⃣  ingesting analytics,

```bash
palisades analytics ingest upload
```

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-27-15-10-29-dkqvtj/damage-history.png?raw=true)


```bash
@download - \
  palisades-analytics-2025-01-27-15-10-29-dkqvtj \
  open,QGIS
```

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-27-15-10-29-dkqvtj/QGIS-3.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-27-15-10-29-dkqvtj/QGIS-2.png?raw=true)


![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-27-15-10-29-dkqvtj/QGIS.png?raw=true)

```yaml
analytics:
  building_count: 3836
  datetime:
  - '2025-01-01T18:29:58Z'
  - '2025-01-13T19:06:55Z'
  - '2025-01-14T18:30:37Z'
  - '2025-01-14T18:30:58Z'
  - '2025-01-14T18:36:40Z'
  - '2025-01-14T18:37:03Z'
  - '2025-01-15T18:52:23Z'
  - '2025-01-15T18:52:40Z'
  - '2025-01-16T18:58:02Z'
  - '2025-01-19T18:47:58Z'
  - '2025-01-19T18:49:13Z'
  - '2025-01-19T18:49:37Z'
...
  observation_count:
    1: 589
    2: 787
    3: 1722
    4: 320
    5: 418

```

## 3️⃣ ingesting one building,

```bash
palisades analytics ingest_building \
  building=035501-377213,~download \
  palisades-analytics-2025-01-26-17-13-55-jl0par
```

![image](https://github.com/kamangir/assets/blob/main/palisades/palisades-analytics-2025-01-26-17-13-55-jl0par/thumbnail-035521-377202-palisades-analytics-2025-01-26-17-13-55-jl0par.gif?raw=true)


[palisades-analytics-2025-01-27-15-10-29-dkqvtj](https://kamangir-public.s3.ca-central-1.amazonaws.com/palisades-analytics-2025-01-27-15-10-29-dkqvtj.tar.gz)


# Damage Analytics

- [round one](./damage-analytics-round-one.md)
- [round two](./damage-analytics-round-two.md)
- [round three](./damage-analytics-round-three.md)
- [round four](./damage-analytics-round-four.md)

## 1️⃣ ingesting from the target,

🚧

```bash
@batch eval - \
  palisades ingest - \
  target=LA \
  scope=rgb \
  predict \
  profile=FULL,upload - - - \
  to=aws_batch
```

## 2️⃣  ingesting analytics,

🚧

```bash
palisades analytics ingest upload
```

## 3️⃣ ingesting one building,

🚧

```bash
palisades analytics ingest_building \
  building=035501-377213,~download \
  palisades-analytics-2025-01-26-17-13-55-jl0par
```

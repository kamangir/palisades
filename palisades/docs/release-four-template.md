# release four 🎰

```bash
@batch eval - \
  palisades ingest - \
  target=LA-250 \
  scope=rgb \
  predict \
  profile=FULL,upload - - - \
  to=aws_batch
```

🎰

```bash
@select palisades-release-four-$(@@timestamp)

palisades analytics ingest upload .

@open QGIS .

@assets publish push .
@publish tar .
```

set:::object_name palisades-release-four-2025-01-30-jqnc4l

object:::get:::object_name

coverage: assets:::get:::object_name/coverage.geojson

assets:::get:::object_name/QGIS.png

yaml:::get:::object_name:::analytics.summary

assets:::get:::object_name/damage-history.png

---

🎯 Target List: object:::blue-geo-target-list-v1
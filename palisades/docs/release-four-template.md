# release four

🔥

```bash
@select palisades-release-four-$(@@timestamp)

palisades analytics ingest upload .

@open QGIS .
code metadata.yaml

@assets publish push .
@publish tar .
```

set:::object_name TBA

object:::get:::object_name

coverage: assets:::get:::object_name/coverage.geojson

yaml:::get:::object_name:::analytics.summary

assets:::get:::object_name/damage-history.png

---

🎯 Target List: object:::blue-geo-target-list-v1
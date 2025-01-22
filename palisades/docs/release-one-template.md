# 🧑🏽‍🚒 `palisades`: release one

ℹ️ for details about these objects refer to [step-by-step](./step-by-step.md).

## Objects

Prediction on a train datacube: 
object:::predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00-2025-01-21-lhnxrc

Prediction on an eval datacube: 
object:::predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-10400100A0B73800-2025-01-21-jeko6i

Datacube: 
object:::datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00

Datacube: 
object:::datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102212-10400100A0B73800

Review: 
object:::palisades-round-one-2025-01-21-le9rww

Dataset: 
object:::palisades-dataset-v1-ingest-2025-01-19-v48x7l

Model: 
object:::palisades-dataset-v1-ingest-2025-01-20-520ze1-model-2025-01-20-s5xtkp

List of targets: 
object:::blue-geo-target-list-v1

Sentinel-2 grid: 
object:::Sentinel-2-Shapefile-Index-v3

Prediction result template: 
object:::predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00-2025-01-20-x54yb0

---

total: 10 files, 821 MB.

## Tech Stack

- ML: [segmentation_models.pytorch](https://github.com/qubvel-org/segmentation_models.pytorch)
- Catalog: https://maxar-opendata.s3.amazonaws.com/events/catalog.json
- Inspired by: https://github.com/microsoft/building-damage-assessment
- Triggered by: https://www.linkedin.com/feed/update/urn:li:activity:7282676832011730944/, https://www.satellite-image-deep-learning.com/p/building-damage-assessment
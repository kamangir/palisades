#! /usr/bin/env bash

function test_palisades_buildings_download_footprints() {
    local options=$1

    palisades_buildings_download_footprints \
        ,$options \
        predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00-2025-01-22-h6u7wj \
        country_code=US,source=microsoft
}

#! /usr/bin/env bash

function test_palisades_buildings_download() {
    local options=$1

    local object_name=predict-datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00-2025-01-22-h6u7wj
    abcli_download - $object_name

    local filename=$(abcli_metadata_get \
        key=predict.output_filename \
        $object_name)

    palisades_buildings_download \
        dryrun,filename=$filename,$options \
        $object_name \
        country_code=US,source=microsoft
}

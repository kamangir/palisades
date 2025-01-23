#! /usr/bin/env bash

function test_palisades_predict() {
    local options=$1

    palisades_predict \
        ingest,$options \
        - \
        - \
        datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311102213-103001010B9A1B00 \
        test_palisades_predict-$(abcli_string_timestamp_short) \
        country_code=US,source=microsoft
}

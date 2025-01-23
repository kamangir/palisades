#! /usr/bin/env bash

function test_palisades_predict() {
    local options=$1

    palisades_predict \
        ingest,$options \
        - \
        - \
        $PALISADES_TEST_DATACUBE \
        test_palisades_predict-$(abcli_string_timestamp_short) \
        country_code=US,source=microsoft
}

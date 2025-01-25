#! /usr/bin/env bash

function test_palisades_buildings_download_footprints() {
    local options=$1

    palisades_buildings_download_footprints \
        ,$options \
        $PALISADES_TEST_PREDICTION_OBJECT \
        overwrite
}

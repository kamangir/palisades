#! /usr/bin/env bash

function test_palisades_buildings_analyze() {
    local options=$1

    palisades_buildings_analyze \
        ,$options \
        $PALISADES_TEST_PREDICTION_OBJECT
}

#! /usr/bin/env bash

function test_palisades_analytics_ingest() {
    local options=$1

    abcli_eval ,$options \
        palisades_analytics_ingest \
        acq_count=2,building_count=20
}

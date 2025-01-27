#! /usr/bin/env bash

function test_palisades_analytics_render() {
    local options=$1

    abcli_eval ,$options \
        palisades_analytics_render \
        building=039338-378002 \
        test_palisades_analytics_ingest_and_render-2025-01-26-wuchjv
}

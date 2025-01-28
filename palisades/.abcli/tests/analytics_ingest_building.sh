#! /usr/bin/env bash

function test_palisades_analytics_ingest_building {
    local options=$1

    abcli_eval ,$options \
        palisades_analytics_ingest_building \
        building=039568-378514 \
        palisades-analytics-2025-01-27-12-56-12-vsgg6z
}

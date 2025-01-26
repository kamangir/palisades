#! /usr/bin/env bash

function test_palisades_analytics_ingest_and_render() {
    local options=$1

    local object_name=test_palisades_analytics_ingest_and_render-$(abcli_string_timestamp_short)

    abcli_eval ,$options \
        palisades_analytics_ingest \
        acq=2,buildings=20 \
        $object_name
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        palisades_analytics_render \
        building=TBA,~download \
        $object_name
}

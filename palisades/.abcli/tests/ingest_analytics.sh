#! /usr/bin/env bash

function test_palisades_ingest_analytics() {
    local options=$1

    abcli_eval ,$options \
        palisades_ingest_analytics \
        acq=2,buildings=20,~upload \
        test_palisades_ingest_analytics-$(abcli_string_timestamp_short)
}

#! /usr/bin/env bash

function test_palisades_predict() {
    local options=$1

    palisades_predict \
        - \
        ,$options \
        - \
        - \
        $PALISADES_TEST_DATACUBE \
        test_palisades_predict-$(abcli_string_timestamp_short) \
        - \
        count=3

    [[ $? -ne 0 ]] && return 1

    abcli_hr

    palisades_predict \
        ~tag \
        ,$options \
        - \
        - \
        $PALISADES_TEST_DATACUBE \
        test_palisades_predict-$(abcli_string_timestamp_short) \
        - \
        count=3
}

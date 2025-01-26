#! /usr/bin/env bash

function test_palisades_help() {
    local options=$1

    local module
    for module in \
        "palisades buildings" \
        "palisades buildings analyze" \
        "palisades buildings download_footprints" \
        \
        "palisades pypi" \
        "palisades pypi browse" \
        "palisades pypi build" \
        "palisades pypi install" \
        \
        "palisades pytest" \
        \
        "palisades test" \
        "palisades test list" \
        \
        "palisades ingest" \
        "palisades ingest analytics" \
        "palisades label" \
        "palisades predict" \
        "palisades train" \
        \
        "palisades"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}

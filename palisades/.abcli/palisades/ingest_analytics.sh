#! /usr/bin/env bash

function palisades_ingest_analytics() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local acq_count=$(abcli_option "$options" acq -1)
    local building_count=$(abcli_option "$options" buildings -1)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 palisades-analytics-$(abcli_string_timestamp))

    abcli_eval dryrun=$do_dryrun \
        python3 -m palisades.analytics \
        ingest \
        --object_name $object_name \
        --acq_count $acq_count \
        --building_count $building_count
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}

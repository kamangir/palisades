#! /usr/bin/env bash

function palisades_analytics_ingest_building() {
    local options=$1
    local building_id=$(abcli_option "$options" building void)
    local acq_count=$(abcli_option "$options" acq_count -1)
    local building_count=$(abcli_option "$options" building_count -1)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_deep=$(abcli_option_int "$options" deep 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload 0)

    local object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m palisades.analytics \
        ingest_building \
        --object_name $object_name \
        --building_id $building_id \
        --acq_count $acq_count \
        --building_count $building_count \
        --do_deep $do_deep
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}

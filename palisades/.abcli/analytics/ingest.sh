#! /usr/bin/env bash

function palisades_analytics_ingest() {
    local options=$1
    local acq_count=$(abcli_option "$options" acq_count -1)
    local building_count=$(abcli_option "$options" building_count -1)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)
    local damage_threshold=$(abcli_option "$options" damage $PALISADES_DAMAGE_THRESHOLD)

    local object_name=$(abcli_clarify_object $2 palisades-analytics-$(abcli_string_timestamp))
    abcli_clone \
        - \
        $PALISADES_QGIS_TEMPLATE_ANALYTICS \
        $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m palisades.analytics \
        ingest \
        --object_name $object_name \
        --acq_count $acq_count \
        --building_count $building_count \
        --damage_threshold $damage_threshold
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}

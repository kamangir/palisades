#! /usr/bin/env bash

function palisades_buildings_analyze() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_ingest=$(abcli_option_int "$options" ingest $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload 0)
    local buffer=$(abcli_option "$options" buffer $PALISADES_DEFAULT_BUFFER_M)
    local max_count=$(abcli_option "$options" count -1)

    local object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    if [[ "$do_ingest" == 1 ]]; then
        local datacube_id=$(abcli_metadata_get \
            key=predict.datacube_id,object \
            $object_name)

        blue_geo_datacube_ingest \
            scope=rgb \
            $datacube_id
        [[ $? -ne 0 ]] && return 1
    fi

    abcli_log "analyzing $object_name @ buffer=$buffer ..."

    abcli_eval dryrun=$do_dryrun \
        python3 -m palisades.buildings analyze \
        --object_name $object_name \
        --buffer $buffer \
        --max_count $max_count \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}

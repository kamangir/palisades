#! /usr/bin/env bash

function palisades_label() {
    local options=$1
    local do_download=$(abcli_option_int "$options" download 0)
    local offset=$(abcli_option "$option" offset 0)

    local datacube_label_options=$2

    local query_object_name=$(abcli_clarify_object $3 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $query_object_name

    local datacube_id=$(blue_geo_catalog_query_read - \
        $query_object_name \
        --offset $offset)
    if [[ -z "$datacube_id" ]]; then
        abcli_log_error "datacube $query_object_name/#$offset not found."
        return 1
    fi

    blue_geo_datacube_label \
        ,$datacube_label_options \
        $datacube_id
}

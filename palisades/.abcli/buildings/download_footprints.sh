#! /usr/bin/env bash

function palisades_buildings_download_footprints() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" dryrun $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload 0)

    local input_object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $input_object_name

    local input_filename=$(abcli_metadata_get \
        key=predict.output_filename \
        $input_object_name)
    input_filename=$(abcli_option "$options" filename $input_filename)

    local query_options=$3
    local country_code=$(abcli_option "$query_options" country_code US)
    local country_name=$(abcli_option "$query_options" country_name)
    local do_overwrite=$(abcli_option_int "$query_options" overwrite 0)
    local source=$(abcli_option "$query_options" source microsoft)

    local output_object_name=$(abcli_clarify_object $4 $country_code-$source-buildings-$(abcli_string_timestamp))
    local output_object_path=$ABCLI_OBJECT_ROOT/$output_object_name
    mkdir -pv $output_object_path

    abcli_log "buildings: $source $input_object_name/$input_object_name -$country_code-> $output_object_name ..."

    local extra_args=""
    [[ ! -z "$country_name" ]] &&
        extra_args="--country_name $country_name"

    [[ "$do_overwrite" == 1 ]] &&
        extra_args="$extra_args --overwrite"

    abcli_eval dryrun=$do_dryrun,path=$abcli_path_git/building-damage-assessment \
        python3 download_building_footprints.py \
        --source $source \
        --input_fn $ABCLI_OBJECT_ROOT/$input_object_name/$input_filename \
        --output_dir $output_object_path \
        --country_alpha2_iso_code $country_code \
        $extra_args \
        "${@:5}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $output_object_name

    return 0
}

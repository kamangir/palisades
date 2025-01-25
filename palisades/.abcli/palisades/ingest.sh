#! /usr/bin/env bash

function palisades_ingest() {
    local options=$1
    local target_options=$2
    local datacube_ingest_options=$3
    local batch_options=$4
    local predict_options=$5
    local model_object_name=${6:--}
    local buildings_query_options=$7
    local analysis_options=$8

    blue_geo_watch_targets_download

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))

    local target=$(abcli_option "$target_options" target)
    local query_object_name
    if [[ -z "$target" ]]; then
        query_object_name=$target_options

        abcli_download - $query_object_name
    else
        query_object_name=palisades-$target-query-$(abcli_string_timestamp_short)

        blue_geo_watch_query \
            $target_options \
            $query_object_name
        [[ $? -ne 0 ]] && return 1
    fi

    local do_predict=$(abcli_option_int "$batch_options" predict 0)
    [[ "$do_predict" == 0 ]] &&
        return 0

    local count=$(abcli_option "$batch_options" count -1)
    local do_tag=$(abcli_option_int "$batch_options" tag 1)

    local list_of_datacubes=$(blue_geo_catalog_query_read \
        all \
        $query_object_name \
        --count $count \
        --delim +)
    abcli_log_list "$list_of_datacubes" \
        --before "predicting" \
        --delim + \
        --after "datacubes(s)"

    local datacube_id
    local prediction_object_name
    for datacube_id in $(echo "$list_of_datacubes" | tr + " "); do
        prediction_object_name=predict-$datacube_id-$(abcli_string_timestamp_short)

        palisades_predict \
            tag=$do_tag \
            ,$datacube_ingest_options \
            ,$predict_options \
            "$model_object_name" \
            $datacube_id \
            $prediction_object_name \
            ,$buildings_query_options \
            ,$analysis_options
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done
    return 0
}

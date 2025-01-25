#! /usr/bin/env bash

function palisades_ingest() {
    local options=$1
    local target_options=$2
    local datacube_ingest_options=$3
    local batch_options=$4
    local predict_options=$5
    local model_object_name=$(abcli_clarify_object $6 $PALISADES_DEFAULT_FIRE_MODEL)
    local buildings_query_options=$7
    local analysis_options=$8
    local workflow_options=$9

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

    local job_name="$query_object_name-job-$(abcli_string_timestamp_short)"

    abcli_log "🧑🏽‍🚒 ingest: $query_object_name: -[ $workflow_options @ $job_name]-> $workflow_options ..."

    abcli_eval dryrun=$do_dryrun \
        python3 -m palisades.workflow \
        generate \
        --workflow_name ingest \
        --job_name $job_name \
        --query_object_name $query_object_name \
        --count $count \
        --do_tag $do_tag \
        --datacube_ingest_options ,$datacube_ingest_options \
        --predict_options ,$predict_options \
        --model_object_name $model_object_name \
        --buildings_query_options ,$buildings_query_options \
        --analysis_options ,$analysis_options \
        "${@:10}"
    [[ $? -ne 0 ]] && return 1

    local do_submit=$(abcli_option_int "$workflow_options" submit 1)
    [[ "$do_submit" == 0 ]] && return 0

    abcli_eval dryrun=$do_dryrun \
        blueflow_workflow_submit \
        ~download,$workflow_options \
        $job_name
}

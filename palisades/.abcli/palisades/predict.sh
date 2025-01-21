#! /usr/bin/env bash

function blue_sandbox_palisades_predict() {
    local options=$1
    local do_ingest=$(abcli_option_int "$options" ingest 0)
    local do_tag=$(abcli_option_int "$options" tag 1)

    local predict_options=$2
    $abcli_gpu_status_cache && local device=cuda || local device=cpu
    local device=$(abcli_option "$predict_options" device $device)
    local do_dryrun=$(abcli_option_int "$predict_options" dryrun 0)
    local do_download=$(abcli_option_int "$predict_options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$predict_options" upload $(abcli_not $do_dryrun))
    local profile=$(abcli_option "$predict_options" profile VALIDATION)

    local model_object_name=$(abcli_clarify_object $3 ..)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $model_object_name

    local datacube_id=$(abcli_clarify_object $4 .)
    [[ "$do_ingest" == 1 ]] &&
        blue_geo_datacube_ingest \
            scope=rgb \
            $datacube_id

    local prediction_object_name=$(abcli_clarify_object $5 predict-$datacube_id-$(abcli_string_timestamp_short))

    abcli_log "semseg[$model_object_name].predict($datacube_id) -$device-@-$profile-> $prediction_object_name."

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_sandbox.palisades predict \
        --device $device \
        --model_object_name $model_object_name \
        --datacube_id $datacube_id \
        --prediction_object_name $prediction_object_name \
        --profile $profile \
        "${@:6}"
    local status="$?"

    [[ "$do_tag" == 1 ]] &&
        abcli_mlflow_tags_set \
            $prediction_object_name \
            datacube_id=$datacube_id,model=$model_object_name,profile=$profile

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $prediction_object_name

    return $status
}

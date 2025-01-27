#! /usr/bin/env bash

function palisades_predict() {
    local options=$1
    local do_tag=$(abcli_option_int "$options" tag 1)

    local ingest_options=$2
    local do_ingest=$(abcli_option_int "$ingest_options" ingest 1)

    local predict_options=$3
    $abcli_gpu_status_cache && local device=cuda || local device=cpu
    local device=$(abcli_option "$predict_options" device $device)
    local do_dryrun=$(abcli_option_int "$predict_options" dryrun 0)
    local do_download=$(abcli_option_int "$predict_options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$predict_options" upload 0)
    local profile=$(abcli_option "$predict_options" profile VALIDATION)

    local model_object_name=$(abcli_clarify_object $4 $PALISADES_DEFAULT_FIRE_MODEL)

    local datacube_id=$(abcli_clarify_object $5 .)

    local prediction_object_name=$(abcli_clarify_object $6 predict-$datacube_id-$(abcli_string_timestamp_short))

    if [[ "$do_tag" == 1 ]]; then
        local previous_prediction=$(abcli_mlflow_tags_search \
            contains=palisades.prediction,datacube_id=$datacube_id,model=$model_object_name,profile=$profile \
            --log 0 \
            --count 1)

        if [[ ! -z "$previous_prediction" ]]; then
            abcli_log "✅  $previous_prediction: $datacube_id @ $model_object_name @ $profile"
            return 0
        fi

        abcli_mlflow_tags_set \
            $prediction_object_name \
            contains=palisades.prediction,datacube_id=$datacube_id,model=$model_object_name,profile=$profile
    fi

    [[ "$do_download" == 1 ]] &&
        abcli_download - $model_object_name

    [[ "$do_ingest" == 1 ]] &&
        blue_geo_datacube_ingest \
            ,$ingest_options \
            $datacube_id

    abcli_clone \
        - \
        $PALISADES_QGIS_TEMPLATE_PREDICT \
        $prediction_object_name

    local buildings_query_options=$7

    local analysis_options=$8

    abcli_log "semseg[$model_object_name].predict($datacube_id) -$device-@-$profile-> $prediction_object_name."

    abcli_eval dryrun=$do_dryrun \
        python3 -m palisades.semseg predict \
        --device $device \
        --model_object_name $model_object_name \
        --datacube_id $datacube_id \
        --prediction_object_name $prediction_object_name \
        --profile $profile
    [[ $? -ne 0 ]] && return 1

    local do_download_building_footprints=$(abcli_option_int "$buildings_query_options" download_footprints 1)
    if [[ "$do_download_building_footprints" == 1 ]]; then
        palisades_buildings_download_footprints \
            ~download,dryrun=$do_dryrun \
            $prediction_object_name \
            ,$buildings_query_options \
            $prediction_object_name
        [[ $? -ne 0 ]] && return 1
    fi

    local do_analyze=$(abcli_option_int "$analysis_options" analyze 1)
    if [[ "$do_analyze" == 1 ]]; then
        palisades_buildings_analyze \
            ~download,~ingest,$analysis_options \
            $prediction_object_name
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $prediction_object_name

    return 0
}

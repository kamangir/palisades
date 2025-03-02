#! /usr/bin/env bash

function palisades_train() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_review=$(abcli_option_int "$options" review 0)

    local query_object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $query_object_name

    local ingest_options=$3
    local count=$(abcli_option "$ingest_options" count 10000)

    local dataset_object_name=$(abcli_clarify_object $4 ${query_object_name}-ingest-$(abcli_string_timestamp_short))

    local train_options=$5
    local epoch_count=$(abcli_option "$train_options" epochs 5)

    local model_object_name=$(abcli_clarify_object $6 ${dataset_object_name}-model-$(abcli_string_timestamp_short))

    if [[ "$do_review" == 1 ]]; then
        roofai_dataset_review \
            dryrun=$do_dryrun \
            $query_object_name \
            --index 0 \
            --subset test
        [[ $? -ne 0 ]] && return 1
    fi

    roofai_dataset_ingest \
        ~download,source=$query_object_name,$ingest_options \
        $dataset_object_name \
        --test_count $(python3 -c "print(int($count*0.1))") \
        --train_count $(python3 -c "print(int($count*0.8))") \
        --val_count $(python3 -c "print(int($count*0.1))")
    [[ $? -ne 0 ]] && return 1

    if [[ "$do_review" == 1 ]]; then
        local subset
        for subset in train test val; do
            roofai_dataset_review \
                dryrun=$do_dryrun \
                $dataset_object_name \
                --index 0 \
                --subset $subset
            [[ $? -ne 0 ]] && return 1
        done
    fi

    roofai_semseg_train \
        ~download,$train_options \
        $dataset_object_name \
        $model_object_name \
        --classes affected \
        --epoch_count $epoch_count
}

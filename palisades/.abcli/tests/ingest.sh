#! /usr/bin/env bash

function test_palisades_ingest_target_no_ingest() {
    local options=$1

    abcli_eval ,$options \
        palisades_ingest \
        - \
        target=Palisades-Maxar-test \
        ~ingest
}

function test_palisades_ingest_query_object_no_ingest() {
    local options=$1

    abcli_eval ,$options \
        palisades_ingest \
        - \
        $PALISADES_QUERY_OBJECT_PALISADES_MAXAR_TEST \
        ~ingest
}

function test_palisades_ingest_target_no_predict() {
    local options=$1

    abcli_eval ,$options \
        palisades_ingest \
        - \
        target=Palisades-Maxar-test \
        scope=rgb
}

function test_palisades_ingest() {
    local options=$1
    local list_of_runners=$(abcli_option "$options" runner local+aws_batch)

    local runner
    for runner in $(echo $list_of_runners | tr + " "); do
        abcli_log "testing runner: $runner ..."

        abcli_eval ,$options \
            palisades_ingest \
            - \
            target=Palisades-Maxar-test \
            scope=rgb \
            predict,count=1,~tag \
            profile=VALIDATION \
            - \
            - \
            count=3 \
            to=$runner
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

}

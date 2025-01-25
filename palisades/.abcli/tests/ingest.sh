#! /usr/bin/env bash

function test_palisades_ingest() {
    local options=$1

    abcli_eval ,$options \
        palisades_ingest \
        - \
        target=Palisades-Maxar-test \
        ~ingest
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    abcli_eval ,$options \
        palisades_ingest \
        - \
        $PALISADES_QUERY_OBJECT_PALISADES_MAXAR_TEST \
        ~ingest
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    abcli_eval ,$options \
        palisades_ingest \
        - \
        target=Palisades-Maxar-test \
        scope=rgb
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    abcli_eval ,$options \
        palisades_ingest \
        - \
        target=Palisades-Maxar-test \
        scope=rgb \
        predict,count=1,~tag \
        profile=VALIDATION \
        - \
        - \
        count=3
}

#! /usr/bin/env bash

function test_blue_sandbox_palisades_ingest() {
    local options=$1

    abcli_eval ,$options \
        blue_sandbox_palisades_ingest \
        ~upload \
        target=Palisades-Maxar-test \
        ~ingest_datacubes
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    abcli_eval ,$options \
        blue_sandbox_palisades_ingest \
        ~upload \
        $PALISADES_QUERY_OBJECT_PALISADES_MAXAR_TEST \
        ~ingest_datacubes
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    abcli_eval ,$options \
        blue_sandbox_palisades_ingest \
        ~upload \
        target=Palisades-Maxar-test \
        scope=rgb
}

#! /usr/bin/env bash

function palisades() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=palisades_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m palisades "$@"
}

abcli_source_caller_suffix_path /palisades

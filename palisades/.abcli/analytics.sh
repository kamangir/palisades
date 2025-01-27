#! /usr/bin/env bash

function palisades_analytics() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=palisades_analytics_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m palisades.analytics "$@"
}

abcli_source_caller_suffix_path /analytics

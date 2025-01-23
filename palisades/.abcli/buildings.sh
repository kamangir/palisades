#! /usr/bin/env bash

function palisades_buildings() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=palisades_buildings_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m palisades.buildings "$@"
}

abcli_source_caller_suffix_path /buildings

#! /usr/bin/env bash

function blue_plugin_node() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=blue_plugin_node_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi
    abcli_log "blue-plugin: node: 🪄"
}

abcli_source_caller_suffix_path /node

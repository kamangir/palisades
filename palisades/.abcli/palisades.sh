#! /usr/bin/env bash

function palisades() {
    local task=$(abcli_unpack_keyword $1 version)

    abcli_generic_task \
        plugin=palisades,task=$task \
        "${@:2}"
}

abcli_log $(palisades version --show_icon 1)

abcli_source_caller_suffix_path /palisades

#! /usr/bin/env bash

function blue_plugin() {
    local task=$(abcli_unpack_keyword $1 version)

    if [ "$task" == "task" ]; then
        local options=$2
        local do_dryrun=$(abcli_option "$options" dryrun 0)
        local what=$(abcli_option "$options" what all)

        local object_name_1=$(abcli_clarify_object $3 .)

        abcli_eval dryrun=$do_dryrun \
            python3 -m blue_plugin \
            task \
            --what "$what" \
            --object_name "$object_name_1" \
            "${@:4}"

        return
    fi

    abcli_generic_task \
        plugin=blue_plugin,task=$task \
        "${@:2}"
}

abcli_log $(blue_plugin version --show_icon 1)

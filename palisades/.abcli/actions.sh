#! /usr/bin/env bash

function palisades_action_git_before_push() {
    palisades build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "main" ]] &&
        return 0

    palisades pypi build
}



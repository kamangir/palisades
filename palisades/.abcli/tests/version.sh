#! /usr/bin/env bash

function test_palisades_version() {
    local options=$1

    abcli_eval ,$options \
        "palisades version ${@:2}"
}



#! /usr/bin/env bash

function test_palisades_thing() {
    local options=$1

    local test_options=$2

    abcli_eval ,$options \
        "echo 📜 palisades: test: thing: $test_options: ${@:3}."
}



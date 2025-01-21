#! /usr/bin/env bash

function test_palisades_README() {
    local options=$1

    abcli_eval ,$options \
        palisades build_README
}



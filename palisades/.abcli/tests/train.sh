#! /usr/bin/env bash

function test_blue_sandbox_palisades_train() {
    local options=$1

    blue_sandbox_palisades_train \
        review,~upload,$options \
        palisades-dataset-v1 \
        count=1000 \
        - \
        epochs=1 \
        -
}

#! /usr/bin/env bash

function test_palisades_train() {
    local options=$1

    palisades_train \
        review,~upload,$options \
        palisades-dataset-v1 \
        count=1000 \
        - \
        epochs=1 \
        -
}

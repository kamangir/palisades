#! /usr/bin/env bash

function abcli_install_palisades() {
    abcli_git_clone https://github.com/microsoft/building-damage-assessment.git
}

abcli_install_module palisades 1.1.1

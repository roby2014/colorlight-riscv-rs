#!/usr/bin/env bash

# TODO 2: runner can only be set to one of these scripts
# find a way to have different "runner" targets (simulation & hw)

set -ex

# create bin file
riscv64-elf-objcopy $1 -O binary $1.bin

# run simulation
litex_sim --output-dir=target/litex_sim --cpu-type=vexriscv --ram-init=$1.bin --no-compile-software

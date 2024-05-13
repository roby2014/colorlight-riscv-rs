#!/usr/bin/env bash

# TODO2: runner can only be set to one of these scripts
# find a way to have different "runner" targets (simulation & hw)

set -e
riscv64-elf-objcopy $1 -O binary $1.bin
litex_sim --output-dir=target/litex_sim --cpu-type=vexriscv --rom-init=$1.bin --no-compile-software --csr-csv "csr.csv"
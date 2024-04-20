#!/usr/bin/env bash

# TODO: simulation does not work ATM
# TODO2: runner can only be set to one of these, 
# find a way to have different "runner" targets

set -e
riscv64-elf-objcopy $1 -O binary $1.bin
litex_sim --output-dir=target/litex_sim  --cpu-type=vexriscv --integrated-main-ram-size=0x10000 --ram-init=$1.bin
#!/usr/bin/env bash

# FIXME: /dev/ttyUSB1 should not be hardcoded

set -ex

# create bin file
riscv64-elf-objcopy $1 -O binary $1.bin

# upload binary
litex_term --kernel $1.bin $DEVICE

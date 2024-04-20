#!/usr/bin/env bash

# FIXME: /dev/ttyUSB1 should not be hardcoded

set -e
riscv64-elf-objcopy $1 -O binary $1.bin
litex_term --kernel $1.bin /dev/ttyUSB1
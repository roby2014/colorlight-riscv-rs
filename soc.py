#!/usr/bin/env python3

import argparse
import os

from migen import *
from migen.genlib.io import CRG

from litex_boards.platforms import colorlight_5a_75e
from litex.build.lattice.trellis import trellis_args, trellis_argdict
from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *

from litex.soc.cores import uart

# BaseSoC -----------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
    def __init__(self, version, revision):
        # 25 MHz
        sys_clk_freq = int(25e6)

        # SoC with CPU
        platform = colorlight_5a_75e.Platform(revision)
        SoCCore.__init__(self, platform,
            cpu_type                 = "vexriscv",
            clk_freq                 = sys_clk_freq,
            ident                    = f"LiteX RISC-V CPU Test SoC {version}", ident_version=True,
            integrated_rom_size      = 0x8000,
            integrated_main_ram_size = 0x4000)

        # Clock Reset Generation
        self.submodules.crg = CRG(platform.request("clk25"))

# Build --------------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LiteX RISC-V SoC on Colorlight 5A-75E")
    builder_args(parser)
    soc_core_args(parser)
    trellis_args(parser)
    parser.add_argument("--build", action="store_true", help="Build bitstream")
    parser.add_argument("--load",  action="store_true", help="Load bitstream")
    parser.add_argument("--cable", default="ft232",    help="openFPGALoader JTAG probe model")
    parser.add_argument("--revision", default="6.0",  help="Colorlight 5A-75E model revision")
    args = parser.parse_args()

    soc = BaseSoC("5A-75E", revision=args.revision)

    builder = Builder(soc, **builder_argdict(args))
    builder.build(**trellis_argdict(args), run=args.build)

    if args.load:
        extra_args = ""
        if args.cable == "ft232RL":
            extra_args = "--pins=RXD:RTS:TXD:CTS"
        elif args.cable == "usb-blaster":
            extra_args = f"--probe-firmware {os.environ['QUARTUSPATH']}"
            
        bitstream_file = builder.get_bitstream_filename()
        cmd = f"openFPGALoader --cable {args.cable} {extra_args} {bitstream_file}"
        print(f"Uploading bitstream file: {bitstream_file}")
        print(f"JTAG cable: {args.cable}")
        print(f"Running command: {cmd}")
        os.system(cmd)

if __name__ == "__main__":
    main()

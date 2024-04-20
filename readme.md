work in progress, lots of todo

### overview
my (ongoing) adventure on trying to control a
- [colorlight 5a-75e v8.0 board](https://www.colorlight-led.com/product/colorlight-5a-75e-led-display-receiving-card.html)
    - [lattice ecp5 fpga](https://www.latticesemi.com/Products/FPGAandCPLD/ECP5)
        - running a [risc-v soc](https://github.com/SpinalHDL/VexRiscv)
            - built with [litex](https://github.com/enjoy-digital/litex/tree/master)

with rust and open source tools ([yosys](https://github.com/YosysHQ/yosys), [nextpnr](https://github.com/YosysHQ/nextpnr), [prjtrellis](https://github.com/YosysHQ/prjtrellis) and [openFPGALoader](https://github.com/trabucayre/openFPGALoader)).

### layout
- [soc](./soc/) - files for building & flashing the fpga with the risc-v soc
- [litex-pac](./litex-pac/) - the peripheral access crate (pac), generated via svd2rust
- [app](./app/) - the firmware that will run

each directory should have a `readme.md` with instructions

### firmware in c
you can check [this repo](https://github.com/roby2014/risc-v-colorlight-5a-75e) for a similar example, but flashing a C firmware.
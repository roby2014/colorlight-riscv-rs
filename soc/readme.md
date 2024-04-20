dependencies
    litex

build with 

    python3 soc.py --build

flash fpga with 

    python3 soc.py --load --no-compile-software --csr-svd "../litex-pac/5a-75e_6.0.svd" --memory-x "../litex-pac/memory.x"
REGION_ALIAS("REGION_TEXT", main_ram);
REGION_ALIAS("REGION_RODATA", main_ram);
REGION_ALIAS("REGION_DATA", main_ram);
REGION_ALIAS("REGION_BSS", sram);
REGION_ALIAS("REGION_HEAP", sram);
REGION_ALIAS("REGION_STACK", sram);

PROVIDE(uart = DefaultHandler);
PROVIDE(timer0 = DefaultHandler);

# adapted from https://github.com/roby2014/risc-v-colorlight-5a-75e/blob/master/firmware/linker.ld 
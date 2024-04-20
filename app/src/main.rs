#![no_std]
#![no_main]

extern crate panic_halt;

use riscv_rt::entry;
use litex_pac as pac;

fn uart_write(uart: &pac::Uart, value: u8) {
    while uart_txfull_read(uart) != 0 {}
    uart.rxtx().write(|w| unsafe { w.bits(value.into()) });
    uart.ev_pending().write(|w| unsafe { w.bits(0x1) });
}

fn uart_txfull_read(uart: &pac::Uart) -> u8 {
    return uart.txfull().read().bits() as u8;
}

fn hprint(uart: &pac::Uart, s: &str) {
    for c in s.bytes() {
        uart_write(uart, c);
    }
}

#[entry]
fn main() -> ! {
    let peripherals = unsafe { pac::Peripherals::steal() };
    let uart = peripherals.uart;

    loop {
        hprint(&uart, "aaaaa");
    }
}

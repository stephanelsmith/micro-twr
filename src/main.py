
import asyncio
import sys
import gc
from micropython import const

from machine import Pin
from machine import UART

from sa868.sa868 import SA868
from sa868.pwr import SA868Pwr
import sa868.defs as sa868_defs

# lilygo-twr specific pin
_MIC_CH_SEL  = const(17)     # mic channel select, 0->mic, 1->esp

async def gc_coro():
    try:
        while True:
            gc.collect()
            await asyncio.sleep(5)
    except asyncio.CancelledError:
        raise
    except Exception as err:
        sys.print_exception(err)

async def sa868_tx_coro(sa868_uart):
    read_stdin = asyncio.StreamReader(sys.stdin)
    while True:
        r = await read_stdin.readline()
        sa868_uart.write(r)

async def sa868_rx_coro(sa868_uart):
    read_sa868 = asyncio.StreamReader(sa868_uart)
    while True:
        r = await read_sa868.readline()
        sys.stdout.write(r)

async def start():
    try:
        gc_task = asyncio.create_task(gc_coro())

        # radio to connect to mic esp
		self.mic_ch_sel = Pin(_MIC_CH_SEL, Pin.OUT)
		self.mic_ch_sel.value(1)

        async with SA868Pwr():
            tasks = []
            sa868_uart = UART(1, 9600, 
                              tx = sa868_defs.SA868_RX, 
                              rx = sa868_defs.SA868_TX)
            tasks.append(asyncio.create_task(sa868_tx_coro(sa868_uart)))
            tasks.append(asyncio.create_task(sa868_rx_coro(sa868_uart)))
            await asyncio.gather(*tasks)

    finally:
        gc_task.cancel()

def main():
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        pass
    except Exception as err:
        sys.print_exception(err)
    finally:
        asyncio.new_event_loop()  # Clear retained state


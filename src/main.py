
import asyncio
import sys
import gc
from micropython import const
from machine import Pin

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


async def start():
    try:
        gc_task = asyncio.create_task(gc_coro())
    finally:
        if rx_task:
            rx_task.cancel()
        if cam_task:
            cam_task.cancel()
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


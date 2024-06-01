
import asyncio
from micropython import const
from machine import Pin

_SA868_PTT = const(41)       # 0-> transmit mode
_SA868_PD  = const(40)       # 0-> power down, 1-> enable

# the actual module implements open-drain logic, lilygo module uses logic level
#_SA868_HL_POWER  = const(38) # open drain logic, 0->low power, open->high power
_SA868_HL_POWER  = const(38) # 0->low power, 1->high power

_SA868_TX  = const(48)       # radio tx, connect to esp32 rx
_SA868_RX  = const(39)       # radio rx, connect to esp32 tx

_SA868_AUDIO_MIC       = const(18)  # radio mic
_SA868_AUDIO_SPEAKER   = const(1)   # audio/adc




from micropython import const

SA868_PTT = const(41)       # 0-> transmit mode
SA868_PD  = const(40)       # 0-> power down, 1-> enable

# the actual module implements open-drain logic, lilygo module uses logic level
#SA868_HL_POWER  = const(38) # open drain logic, 0->low power, open->high power
SA868_HL_POWER  = const(38) # 0->low power, 1->high power

SA868_TX  = const(48)       # radio tx, connect to esp32 rx
SA868_RX  = const(39)       # radio rx, connect to esp32 tx

SA868_AUDIO_MIC       = const(18)  # radio mic
SA868_AUDIO_SPEAKER   = const(1)   # audio/adc


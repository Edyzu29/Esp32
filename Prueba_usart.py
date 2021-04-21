# Librerias

import time
import machine
from machine import UART
from micropython import const

# Constantes


# Declaracion de pines
led = Pin(2, Pin.OUT)
led.value(0)

# Inicializacion de devices
uart = machine.UART(3, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

uart.write('q pasa bb, quiere una matriz')

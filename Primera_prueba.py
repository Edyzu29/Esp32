# Librerias
import time
import machine
import esp32
from micropython import const

# Constantes
DELAY = const(1000)

# Variables
a = 0

# Declaracion de pines
button = Pin(34, Pin.IN)
led = Pin(2, Pin.OUT)
led.value(0)

print((esp32.raw_temperature()-32)/1.8)

while True:
    if(button.value()):
        led.value( not led.value())


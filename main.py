from machine import Pin

from utime import sleep


ledG = Pin(15, Pin.OUT)
ledY = Pin(2, Pin.OUT)
ledR = Pin(0, Pin.OUT)

while True:
    ledG.on()
    print("Led ON Green!")
    sleep(20)
    ledG.off()
    print("Led OFF!")
    sleep(0.5)

    ledY.on()
    print("Led ON Yellow!")
    sleep(10)
    ledY.off()
    print("Led OFF!")
    sleep(0.5)

    ledR.on()
    print("Led ON Red!")
    sleep(7)
    ledR.off()
    print("Led OFF!")
    sleep(0.5)
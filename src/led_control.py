from hal import hal_led as led
from threading import Thread
from time import sleep
from hal import hal_keypad as keypad


def led_thread(d):
    global delay
    delay = d
    while(True):
        if delay!= 0:
            led.set_output(20,1)
            sleep(delay)
            led.set_output(20,0)
            sleep(delay)



def led_control_init():

    led.init()

    global delay

    t1 = Thread(target = led_thread)

    t1.start()

    delay = 1


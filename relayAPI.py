import RPi.GPIO as GPIO
from flask import Flask
import time

#Had to swap the on/off states around
#because I'm a numpty and bought a low=on relay from ebay
ON = False
OFF = True

TIMER = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#What PI pins have we connected the relays to?
activePins = [2,3,4,5]
#Now set those pins up...
for i in activePins:
    GPIO.setup(i, GPIO.OUT)

#API Functionz
def on(PIN):
    GPIO.output(PIN, ON)

def off(PIN):
    GPIO.output(PIN, OFF)

def state(PIN):
    return GPIO.input(PIN) == ON

def switch(PIN):
    if state(PIN):
        print('Lights are on, turning off')
        off(PIN)
    else:
        print('Lights are off, turning on')
        on(PIN)

def timer(m):
    timer_start = time.time()
    length = m*60
    on()
    while time.time() <= timer_start +  length:
        time.sleep(1)
    off()
    return "Time's up!"

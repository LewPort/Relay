import RPi.GPIO as GPIO
from flask import Flask
import time

PIN = 2
ON = False
OFF = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

def on():
    GPIO.output(PIN, ON)

def off():
    GPIO.output(PIN, OFF)

def get_state():
    return GPIO.input(PIN) == ON

def switch():
    if get_state():
        print('Lights are on, turning off')
        off()
    else:
        print('Lights are off, turning on')
        on()

def timer(m):
    timer_start = time.time()
    length = m*60
    on()
    while time.time() <= timer_start +  length:
        time.sleep(1)
    off()
    return "Time's up!"

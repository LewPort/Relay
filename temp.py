import Adafruit_DHT as dht
import time

PIN = 3

def temp():
    temp = dht.read_retry(dht.DHT22, PIN)[1]
    return round(temp, 1)

def humidity():
    h = dht.read_retry(dht.DHT22, PIN)[0]
    return round(h, 1)

import urllib.request
import json

_URL = "http://api.openweathermap.org/data/2.5/weather?q=Toronto&APPID=677f6b056af14113e02f38ae1b18f342"

with urllib.request.urlopen(_URL) as url:
    data = json.loads(url.read().decode())


def temp():
    if data:
        temp = data['main']['temp']
        temp = temp/10
        return temp
    else:
        return "N/A"

def humidity():
    if data:
        humidity = data['main']['humidity']
        return humidity
    else:
        return "N/A"

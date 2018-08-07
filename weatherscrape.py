import urllib.request
import json

_URL = "http://api.openweathermap.org/data/2.5/weather?q=Toronto&units=metric&APPID=677f6b056af14113e02f38ae1b18f342"

def get_data():
    with urllib.request.urlopen(_URL) as url:
        data = json.loads(url.read().decode())
    return data

def temp(data):
    if data:
        temp = data['main']['temp']
        temp = temp
        return round(temp, 1)
    else:
        return "N/A"

def humidity(data):
    if data:
        humidity = data['main']['humidity']
        return round(humidity, 1)
    else:
        return "N/A"

def get_report():
    data = get_data()
    print(data)
    return {'temp': temp(data),
            'humidity': humidity(data)}

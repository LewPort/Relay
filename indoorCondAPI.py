import datetime, time
import json
import temp
import os

_OUTPUT = '/home/lewis/relay/static/indoorCondAPI.json'

def get_current():
    api = {
        'time':{'unix': time.time(),
                'date':datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y'),
                'time':datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')},
        'ht':{'temp': '{0:.1f}'.format(temp.temp()),
              'humidity': round(temp.humidity())},
        }
    return api

def write_json(api):
    with open(_OUTPUT, 'w') as outfile:
        json.dump(api, outfile)

api = None

while True:
    api = get_current()
    write_json(api)
    time.sleep(1)
    


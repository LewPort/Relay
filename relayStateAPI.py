import datetime, time
import relayAPI
import json

#Location of JSON
_OUTPUT = '/home/lewis/relay/static/relayStateAPI.json'

#Return current relay states as a dict
def get_current():
    api = {
        'state': [relayAPI.state(i) for i in relayAPI.activePins]
        }
    return api

#Write that dict out to JSON
def write_json(api):
    with open(_OUTPUT, 'w') as outfile:
        json.dump(api, outfile)


while True:
    try:
        api = get_current()
        write_json(api)
    except:
        pass
    time.sleep(1)
    


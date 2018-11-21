from flask import Flask, render_template, request, redirect, Response
import relayAPI
import temp

app = Flask(__name__)

def switch_text(state):
    if state:
        return 'Lights are On'
    else:
        return 'Lights are Off'

@app.route('/')
def index():
    return render_template('index.html', switch_text=switch_text(relayAPI.state(2)))

@app.route('/switch')
def switch():
    relayAPI.switch(2)
    return Response(200)

@app.route('/on')
def on():
    relayAPI.on(2)
    return Response(200)

@app.route('/off')
def off():
    relayAPI.off(2)
    return Response(200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1977)

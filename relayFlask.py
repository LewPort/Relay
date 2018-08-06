from flask import Flask, render_template, request, redirect
import weatherscrape as outdoor
import relay
import temp

app = Flask(__name__)
relay.off()

conditions = {'indoor':
              {'temp': temp.temp(),
               'humidity': temp.humidity()},
              'outdoor':
               {'temp': outdoor.temp(),
               'humidity': outdoor.humidity()}
               }

def switch_text(state):
    if state:
        return 'Lights are On'
    else:
        return 'Lights are Off'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'onoff' in request.form:
            relay.switch()
        elif 'time' in request.form and request.form.get("time"):
            time = int(request.form.get("time"))
            print('%d minute timer set.' % time)
            relay.timer(time)
        return redirect('/')
    else:
        return render_template('index.html', switch_text=switch_text(relay.get_state()), conditions=conditions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1977)

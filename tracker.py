from config import AUTH_HEADER, ENDPOINT
from flask import Flask, render_template, request, make_response
import os
import requests


app = Flask("manualtracker")
headers = {}

if AUTH_HEADER != '':
        headers = {
                'Authorization': AUTH_HEADER
        }

def update(id, lat, lon, accuracy, voltage):
        update = {
                'device_id': id,
                'lat': lat,
                'lng': lon,
                'accuracy': accuracy,
                'battery_voltage': voltage
        }
        resp = requests.post(ENDPOINT, headers=headers, data=update)
        print(resp)
        print(resp.text)


class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app.wsgi_app = ReverseProxied(app.wsgi_app)



def to_dict(args):
    outdict = {}
    for key, val in args.items():
        outdict[key] = val
    return outdict



@app.route('/')
def index():
    return render_template(
        'tracker.html', 
        approot='/')


@app.route('/set_tracker', methods=['POST'])
def set_tracker():
    data = to_dict(request.form)
    name = data['name']
    lat = data['lat'] 
    lon = data['lon'] 
    voltage = data['voltage']
    update(name, lat, lon, 1, voltage)
    return "OK"

# update('tracker2', 51.493695, 11.969930, 1, 3.6)



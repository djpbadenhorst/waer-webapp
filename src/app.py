from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

import os
import json
import requests
import waer_utils

app = Flask(__name__, static_url_path='/')

@app.route('/panel',methods=['GET'])
def index_get():
    return render_template('index.html', device=request.args.get('device','garmin'))

@app.route('/panel/signup',methods=['GET'])
def signup_get():
    return redirect(waer_utils.get_auth_url(request.args.get('device','garmin')))

@app.route('/panel/success',methods=['GET'])
def success_get():
    user_id = request.args.to_dict().get('user_id')
    if False: #user_id:
        try:
            waer_utils.call_data_api(user_id)
        except:
            pass
    return render_template('success.html', context={})

@app.route('/panel/failure',methods=['GET'])
def failure_get():
    return render_template('failure.html', context={})

@app.route('/panel/data',methods=['POST'])
def data_post():
    try:
        waer_utils.write_to_storage(request.json)
        return(json.dumps({'success':True}), 200, {'ContentType':'application/json'})
    except:
        return(json.dumps({'success':False}), 500, {'ContentType':'application/json'})


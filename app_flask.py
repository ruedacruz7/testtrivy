#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
import os
import json


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
	if request.method == 'GET':
            return '<h1>Hello from Webhook Listener!</h1>'
	if request.method == 'POST':
            req_data = request.get_json(force=True)
            str_obj = json.dumps(req_data)
            print(req_data)
            return '{"success":"true"}'

if __name__ == "__main__":   
    #context = ('ssl.cert', 'ssl.key') # certificate and key file. Cannot be self signed certs    
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False) # will listen on port 5000

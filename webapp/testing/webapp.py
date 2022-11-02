#!/usr/bin/env python3

import json
import sys
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/main')
def get_help():
    return 'This is the main page, no html file found here!'

@app.route('/')
def html():
    return render_template('webapp.html')

if __name__=='__main__':
    host = 'localhost'
    port = 5000
    app.run(host=host,port=port,debug=True)

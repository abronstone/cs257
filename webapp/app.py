#!/usr/bin/env python3

import json
import sys
import api

from flask import Flask,render_template

app = Flask(__name__,static_folder='static',template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/main')
def get_help():
    return 'This is the main page, no html file found here!'

@app.route('/')
def main_page():
    return render_template('mockup1.html')

@app.route('/search')
def search_page():
    return render_template('mockup2.html')

@app.route('/overviews')
def overview_page():
    return render_template('mockup3.html')

@app.route('/popularity')
def popularity_page():
    return render_template('mockup4.html')

@app.route('/comparison')
def comparison_page():
    return render_template('mockup5.html')

if __name__=='__main__':
    host = 'localhost'
    port = 5000
    app.run(host=host,port=port,debug=True)
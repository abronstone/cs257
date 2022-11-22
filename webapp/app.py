#!/usr/bin/env python3

'''
    app.py for Vidinfo
    Jack Owens and Aaron Bronstone
'''

import json
import sys
import api
import argparse

from flask import Flask,render_template

app = Flask(__name__,static_folder='static',template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

#Renders the 'index.html' template at https://127.0.0.1/index
@app.route('/index')
def index():
    return render_template('index.html')

#Renders the 'main.html' template at https://127.0.0.1/main, used mainly for testing purposes
@app.route('/main')
def get_help():
    return 'This is the main page, no html file found here!'

#Renders the 'mockup1.html' 'MAIN PAGE' template at https://127.0.0.1/
@app.route('/')
def main_page():
    return render_template('mockup1.html')

#Renders the 'mockup2.html' 'SEARCH' template at https://127.0.0.1/search
@app.route('/movies')
def search_page():
    return render_template('mockup2.html')

#Renders the 'mockup3.html' 'OVERVIEWS' template at https://127.0.0.1/overviews
@app.route('/overviews')
def overview_page():
    return render_template('mockup3.html')

#Renders the 'mockup4.html' 'GENERATOR' template at https://127.0.0.1/generator (changed from /popularity after 'First Draft Review' assignment)
@app.route('/generator')
def popularity_page():
    return render_template('mockup4.html')

#Renders the 'mockup5.html' 'COMPARISON' template at https://127.0.0.1/comparison
@app.route('/comparison')
def comparison_page():
    return render_template('mockup5.html')

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='the host server for the web page')
    parser.add_argument('port', help='the port the server runs on')
    arguments = parser.parse_args()
    app.run(host=arguments.host,port=arguments.port,debug=True)
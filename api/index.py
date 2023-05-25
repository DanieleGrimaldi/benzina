from flask import Flask
import requests
from metodi import upload
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/carica')
def download_file_impianti():
    return upload() 

#app.run(debug=True, port=80)

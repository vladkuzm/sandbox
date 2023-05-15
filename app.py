from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    resp = requests.get("https://lookmovie2.to")
    return f'Hello, World! {resp.status_code}'

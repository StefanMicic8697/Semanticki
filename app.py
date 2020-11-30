from flask import Flask, render_template
from rdflib import Graph

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from FLASK"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000")

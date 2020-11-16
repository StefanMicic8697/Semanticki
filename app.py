from flask import Flask, render_template
from rdflib import Graph

app = Flask(__name__)

g = Graph()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)

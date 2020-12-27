from flask import Flask, render_template, request, jsonify
from rdflib import Graph
from flask_cors import CORS

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return "Hello from FLASK"

@app.route('/smerovi', methods=['GET'])
def get_smerovi():
    jezik = request.args.get('jezik')

    return jsonify({'smerovi': []}), 200

@app.route('/kursevi', methods=['GET'])
def get_kursevi():
    obrazovni_cilj = request.args.get('obrazovni_cilj')
    smer = request.args.get('smer')
    kurs = request.args.get('kurs')

    return jsonify({'kursevi': []}), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port="5000")


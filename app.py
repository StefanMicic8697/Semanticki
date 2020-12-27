from flask import Flask, render_template, request, jsonify
from rdflib import Graph, Namespace, Literal, URIRef
from flask_cors import CORS

app = Flask(__name__)

g = Graph()
g.parse('semanticki.owl')
n = Namespace(
    "http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#")

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def index():
    return "Hello from FLASK"


@app.route('/smerovi', methods=['GET'])
def get_smerovi():
    jezik = request.args.get('jezik')

    qres = g.query(
        """
        Prefix uni:<http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#>
        SELECT ?smer ?source
        WHERE {{
            ?smer uni:Language ?b .
            FILTER(str(?b) = '{jezik}')
            ?smer uni:Source ?source
        }}""".format(jezik="Srpski"))

    ret_value = []
    for row in qres:
        data = {
            "smer": row[0].split("#")[1],
            "url": row[1].split(",")[0]
        }
        ret_value.append(data)
    ret_value

    return jsonify({'smerovi': ret_value}), 200


@app.route('/kursevi', methods=['GET'])
def get_kursevi():
    c = request.args.get('obrazovni_cilj')
    s = request.args.get('smer')
    k = request.args.get('kurs')

    if k == '':
        qres = g.query(
            f"""
            Prefix uni:<http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#>
            SELECT ?kurs ?source
            WHERE {{
                ?smer uni:HasPart ?kurs .
                FILTER(?smer = uni:{s})
                ?kurs uni:Objective ?cilj .
                FILTER(?cilj = uni:{c})
                ?smer uni:Source ?source
            }}""")

        ret_value = []
        for row in qres:
            data = {
                "kurs": row[0].split("#")[1],
                "url": row[1].split(",")[0]
            }
            ret_value.append(data)

        return jsonify({'kursevi': ret_value}), 200

    else:
        qres = g.query(
            f"""
            Prefix uni:<http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#>
            SELECT ?kurs2 ?source
            WHERE {{
                ?smer uni:HasPart ?kurs .          
                FILTER(?kurs = uni:{k})
                ?smer uni:HasPart ?kurs2 .
                FILTER(?kurs2 != uni:{k})
                ?kurs2 uni:Source ?source
            }}""")

        ret_value = []
        for row in qres:
            data = {
                "kurs": row[0].split("#")[1],
                "url": row[1].split(",")[0]
            }
            ret_value.append(data)

        return jsonify({'kursevi': ret_value}), 200


@app.route('/dodaj-kurs', methods=['POST'])
def dodaj_kurs():
    data = request.get_json()

    autor = data.get('autor')
    datum = data.get('datum')
    opis = data.get('opis')
    id_kursa = data.get('id')
    jezik = data.get('jezik')
    naslov = data.get('naslov')
    predmet = data.get('predmet')
    izvor = data.get('izvor')

    addKurs(autor, datum, opis, id_kursa, jezik, naslov, predmet, izvor)

    return jsonify({'message': "uspesno dodan kurs"}), 200


@app.route('/dodaj-studijski-program', methods=['POST'])
def dodaj_studijski_program():
    data = request.get_json()

    autor = data.get('autor')
    datum = data.get('datum')
    opis = data.get('opis')
    id_programa = data.get('id')
    jezik = data.get('jezik')
    naslov = data.get('naslov')
    predmet = data.get('predmet')
    izvor = data.get('izvor')

    addProgram(autor, datum, opis, id_programa, jezik, naslov, predmet, izvor)

    return jsonify({'message': "uspesno dodat studijski program"}), 200


@app.route('/dodaj-obrazovni-cilj', methods=['POST'])
def dodaj_obrazovni_cilj():
    data = request.get_json()

    opis = data.get('opis')
    id_cilja = data.get('id')
    naslov = data.get('naslov')

    addCilj(opis, id_cilja, naslov)

    return jsonify({'message': "uspesno dodat obrazovni cilj"}), 200


@app.route('/dodaj-nastavni-materijal', methods=['POST'])
def dodaj_nastavni_materijal():
    data = request.get_json()

    autor = data.get('autor')
    opis = data.get('opis')
    id_materijala = data.get('id')
    jezik = data.get('jezik')
    naslov = data.get('naslov')
    predmet = data.get('predmet')
    izvor = data.get('izvor')

    addMaterijal(autor, opis, id_materijala, jezik, naslov, predmet, izvor)

    return jsonify({'message': "uspesno dodat nastani materijal"}), 200


def upit(u):
    return [{
        "smer": row[0].split("#")[1],
        "url": row[1].split(",")[0]
    } for row in g.query(u)]


@app.route('/query', methods=['GET'])
def get_query():
    query = request.args.get('query')

    return jsonify({'redovi': upit(query)}), 200

def addProgram(Creator, Date, Description, Id, Language, Title, Subject, Source):
    NoviCilj = URIRef(
        "http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#"+Title)
    g.add((NoviCilj, n.Class, n.Studijski_program))
    g.add((NoviCilj, n.Creator, Literal(Creator)))
    g.add((NoviCilj, n.Date, Literal(Date)))
    g.add((NoviCilj, n.Description, Literal(Description)))
    g.add((NoviCilj, n.Identifier, Literal(Id)))
    g.add((NoviCilj, n.Language, Literal(Language)))
    g.add((NoviCilj, n.Title, Literal(Title)))
    g.add((NoviCilj, n.Subject, Literal(Subject)))
    g.add((NoviCilj, n.Source, Literal(Source)))


def addKurs(Creator, Date, Description, Id, Language, Title, Subject, Source):
    NoviKurs = URIRef(
        "http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#"+Title)
    g.add((NoviKurs, n.Class, n.Kurs))
    g.add((NoviKurs, n.Creator, Literal(Creator)))
    g.add((NoviKurs, n.Date, Literal(Date)))
    g.add((NoviKurs, n.Description, Literal(Description)))
    g.add((NoviKurs, n.Identifier, Literal(Id)))
    g.add((NoviKurs, n.Language, Literal(Language)))
    g.add((NoviKurs, n.Title, Literal(Title)))
    g.add((NoviKurs, n.Subject, Literal(Subject)))
    g.add((NoviKurs, n.Source, Literal(Source)))


def addMaterijal(Creator, Description, Id, Language, Title, Subject, Source):
    NoviMaterijal = URIRef(
        "http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#"+Title)
    g.add((NoviMaterijal, n.Class, n.Nastavni_materijal))

    g.add((NoviMaterijal, n.Creator, Literal(Creator)))
    g.add((NoviMaterijal, n.Description, Literal(Description)))
    g.add((NoviMaterijal, n.Identifier, Literal(Id)))
    g.add((NoviMaterijal, n.Language, Literal(Language)))
    g.add((NoviMaterijal, n.Title, Literal(Title)))
    g.add((NoviMaterijal, n.Subject, Literal(Subject)))
    g.add((NoviMaterijal, n.Source, Literal(Source)))


def addCilj(desc, ids, title):
    NoviCilj = URIRef(
        "http://www.semanticweb.org/hp/ontologies/2020/11/untitled-ontology-4#"+title)
    g.add((NoviCilj, n.Class, n.Cilj))
    g.add((NoviCilj, n.Description, Literal(desc)))
    g.add((NoviCilj, n.Identifier, Literal(ids)))
    g.add((NoviCilj, n.Title, Literal(title)))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")

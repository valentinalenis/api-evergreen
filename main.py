from flask import Flask, request
from controllers.Entrada import Entrada
import json

app = Flask(__name__)

@app.route('/')
def listarEntradas():
    return (json.dumps(Entrada.list()))

@app.route('/nueva_entrada', methods=['POST'])
def nueva_entrada():
    body = request.json
    return (Entrada.create(json.dumps(body)))

@app.route('/delete/<string:id>', methods = ['DELETE'])
def eliminar_entrada(id):
    return (Entrada.delete(id))

@app.route('/update/<id>', methods=['PUT'])
def actualizar_entrada(id):
    body = json.dumps(request.json)
    return (Entrada.edit(body, id))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_entrada(id):
    return (Entrada.findOne(id))

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
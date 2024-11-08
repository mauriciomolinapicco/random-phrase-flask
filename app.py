from flask import Flask, jsonify, request
import random

app = Flask(__name__)

frases = [
    "esto es una frase v1",
    "esto es una frase v2",
    "esto es una frase v3",
    "esto es una frase v4",
    "esto es una frase v5",
]

@app.route('/frase', methods=['GET'])
def get_phrase():
    frase = random.choice(frases)
    return jsonify({"frase":frase})


@app.route('/suma', methods=['GET'])
def sum_numbers():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Los parámetros deben ser números"}), 400

if __name__ == '__main__':
    app.run(debug=True)
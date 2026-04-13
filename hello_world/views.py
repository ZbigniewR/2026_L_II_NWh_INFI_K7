from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request, jsonify  # Dodaliśmy jsonify tutaj

moje_imie = "Zbigniew"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')

    if output == 'json':
        return jsonify(imie=moje_imie, mgs=msg)

    if not output:
        output = PLAIN

    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)

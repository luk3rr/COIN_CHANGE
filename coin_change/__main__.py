#!/usr/bin/env python3

# Filename: __main__.py
# Created on: July  1, 2024
# Author: Lucas Araújo <araujolucas@dcc.ufmg.br>

import json

from flask import Flask, request, Response
from .coin_change import coin_change

app = Flask(__name__)


@app.route("/api/saque", methods=["POST"])
def main():
    data = request.get_json()

    if "valor" not in data:
        return Response(
            "Erro: valor não encontrado", mimetype="application/json", status=400
        )

    value = data["valor"]

    try:
        solution = coin_change(value)
    except ValueError as e:
        return Response(f"Erro: {str(e)}", mimetype="application/json", status=400)

    solution_json = json.dumps(solution[0], indent=4)

    return Response(solution_json, mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(debug=True)

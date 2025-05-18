from flask import Flask, render_template, request, abort
import json

app = Flask(__name__)

# Cargar el JSON
with open('equipos.json', encoding='utf-8') as f:
    equipos = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/xxxs")
def xxxs():
    return render_template("xxxs.html")

@app.route("/listaxxxs", methods=["POST"])
def listaxxxs():
    nombre = request.form.get("nombre", "").lower()
    if nombre:
        resultados = [e for e in equipos if e["nombre"].lower().startswith(nombre)]
    else:
        resultados = equipos
    return render_template("listaxxxs.html", resultados=resultados)

@app.route("/xxx/<identificador>")
def detalle(indicador=0, identificador=None):
    equipo = next((e for e in equipos if e["id"] == identificador), None)
    if equipo:
        return render_template("detalle.html", equipo=equipo)
    abort(404)

@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

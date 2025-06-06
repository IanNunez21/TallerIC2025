import os
from flask import Flask, render_template, request, jsonify
from src.calculadora import suma, resta, multiplicacion, division

#comentario de prueba para Jira de nuevo fff

# Apunta al templates que está en ../templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None

    if request.method == "POST":
        a = request.form.get("a", "")
        b = request.form.get("b", "")
        op = request.form.get("op", "")
        try:
            a_f = float(a)
            b_f = float(b)
            if op == "+":
                resultado = suma(a_f, b_f)
            elif op == "-":
                resultado = resta(a_f, b_f)
            elif op == "*":
                resultado = multiplicacion(a_f, b_f)
            elif op == "/":
                resultado = division(a_f, b_f)
            else:
                error = "Operación inválida"
        except Exception as e:
            error = str(e)

    return render_template("index.html", resultado=resultado, error=error)

@app.route("/api/calc", methods=["POST"])
def api_calc():
    data = request.get_json()
    a, b, op = data.get("a"), data.get("b"), data.get("op")
    try:
        res = {
            "+": suma,
            "-": resta,
            "*": multiplicacion,
            "/": division
        }[op](a, b)
        return jsonify(result=res)
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    app.run(debug=True)

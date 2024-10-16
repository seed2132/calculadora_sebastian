from flask import Flask
from flask_cors import CORS
import math as mt
from flask import jsonify

app = Flask(__name__)
CORS(app)

@app.route('/suma/<int:num1>/<int:num2>')
@app.route('/suma/<float:num1>/<float:num2>')
@app.route('/suma/<int:num1>/<float:num2>')
@app.route('/suma/<float:num1>/<int:num2>')
def suma(num1=0, num2=0):
    resultado = num1 + num2
    data={
        'resultado': resultado,
        'operacion': 'suma'
    }
    return jsonify(data)

@app.route('/resta/<int:num1>/<int:num2>')
@app.route('/resta/<float:num1>/<float:num2>')
@app.route('/resta/<int:num1>/<float:num2>')
@app.route('/resta/<float:num1>/<int:num2>')
def resta(num1=0,num2=0):
    resultado = num1 - num2
    data={
        'resultado': resultado,
        'operacion': 'resta'
    }
    return jsonify(data)

@app.route('/multiplicacion/<int:num1>/<int:num2>')
@app.route('/multiplicacion/<float:num1>/<float:num2>')
@app.route('/multiplicacion/<int:num1>/<float:num2>')
@app.route('/multiplicacion/<float:num1>/<int:num2>')
def multiplicacion(num1=0,num2=0):
    resultado = num1 * num2
    data={
        'resultado': resultado,
        'operacion': 'multiplicacion'
    }
    return jsonify(data)

@app.route('/division/<int:num1>/<int:num2>')
@app.route('/division/<float:num1>/<float:num2>')
@app.route('/division/<int:num1>/<float:num2>')
@app.route('/division/<float:num1>/<int:num2>')
def division(num1=0,num2=0):
    if num2 != 0:
        resultado = num1 / num2
        data={
            'resultado': resultado,
            'operacion': 'division'
        }
        return jsonify(data)
    else:
        return jsonify({'resultado': 'No se puede dividir por 0', 'operacion': 'division'})

@app.route('/potencia/<int:num1>/<int:num2>')
@app.route('/potencia/<float:num1>/<float:num2>')
@app.route('/potencia/<int:num1>/<float:num2>')
@app.route('/potencia/<float:num1>/<int:num2>')
def potencia(num1=0,num2=0):
    resultado = mt.pow(num1,num2)
    data={
        'resultado': resultado,
        'operacion': 'potencia'
    }
    return jsonify(data)

@app.route('/seno/<int:num1>')
@app.route('/seno/<float:num1>')
def seno(num1=0):
    resultado = mt.sin(num1)
    data={
        'resultado': resultado,
        'operacion': 'seno'
    }
    return jsonify(data)

@app.route('/coseno/<int:num1>')
@app.route('/coseno/<float:num1>')
def coseno(num1=0):
    resultado = mt.cos(num1)
    data={
        'resultado': resultado,
        'operacion': 'coseno'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
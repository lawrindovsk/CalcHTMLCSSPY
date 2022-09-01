from flask import Flask, render_template
from flask import request
from Calc import Calc
import this 

calculadora = Calc()
app = Flask(__name__)#criando uma variável APP que guarda os elementos do Flask
this.resultadoFinal = ""

@app.route("/")#Página Index - Primeira Página de Qualquer Site
def homepage():
    return render_template("Index.html")

@app.route("/soma", methods=['POST','GET'])
def soma():
    this.resultado = 0
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calculadora.somar(numero1,numero2)
    return render_template("soma.html", titulo="Soma", resultado=this.resultadoFinal)
        
@app.route("/subtracao", methods=['POST','GET'])
def subt():
    this.resultado = 0   
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calculadora.subtrair(numero1, numero2)
    return render_template("subtracao.html",titulo='Subtrair',resultado=this.resultadoFinal)        

@app.route("/divisao", methods=['POST', 'GET'])
def divi():
    this.resultado = 0
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calculadora.dividir(numero1, numero2)
    return render_template("divisao.html", titulo='Dividir', resultado=this.resultadoFinal)

@app.route('/multiplicacao', methods=['POST', 'GET'])
def mult():
    this.resultado = 0
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calculadora.multiplicar(numero1, numero2)
    return render_template("multiplicacao.html", titulo='Multiplicar', resultado=this.resultadoFinal)

@app.route('/potencia', methods=['POST', 'GET'])
def pote():
    this.resultado = 0
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calculadora.potencia(numero1, numero2)
    return render_template("potencia.html", titulo='Potência', resultado=this.resultadoFinal)

@app.route('/raiz', methods=['POST', 'GET'])
def raizes():
    this.resultado = 0
    if request.method == 'POST':
        numero1 = request.form['num1']
        this.resultadoFinal = calculadora.raiz(numero1)
    return render_template("raiz.html", titulo='Raiz', resultado=this.resultadoFinal)

@app.route('/tabuada', methods=['POST', 'GET'])
def tabuad():
    this.resultado = 0
    if request.method == 'POST':
        numero1 = request.form['num1']
        this.resultadoFinal = calculadora.tabuada(numero1)
    return render_template("tabuada.html", titulo='Tabuada', resultado=this.resultadoFinal)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask import request
from Calc import Calc
import this 

calculadora = Calc()
app = Flask(__name__)#criando uma variável APP que guarda os elementos do Flask
this.resultadoFinal =""

@app.route("/")#Página Index - Primeira página de qualquer website
def homepage():
    return render_template("index.html")

##########
@app.route("/soma", methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        this.resultadoFinal= calculadora.somar(num1,num2)
    return render_template("soma.html", titulo="Soma", resultado=this.resultadoFinal)

#########       
@app.route("/subtracao", methods=['POST','GET'])
def subt():
    if request.methode == 'POST':
        numero1 = request.form['num1'] 
        numero2 = request.form['num2'] 
        this.resultadoFinal = calculadora.subtrair(numero1,numero2)
        return render_template("subtracao.html",titulo='Subtrair',resultado=this.resultadoFinal)

########
@app.route("/divisao", methods=['POST',"GET"])
def divi():

    this.resultado = 0
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2'] #mudar aqui
        this.resultadoFinal = calculadora.dividir(numero1, numero2)
        return render_template("divisao.html",titulo='Dividir',resultado=this.resultadoFinal)

#######
@app.route("/multiplicacao", methods=['POST',"GET"])
def mult():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2'] #mudar aqui
        this.resultadoFinal = calculadora.dividir(numero1, numero2)
        return render_template("multiplicacao.html",titulo='Multiplicação',resultado=this.resultadoFinal)

########
@app.route("/potencia", methods=['POST',"GET"])
def pot()):
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2'] 
        this.resultadoFinal = calculadora.potencia(numero1, numero2)
        return render_template("potencia.html",titulo='Potência',resultado=this.resultadoFinal)

#########
@app.route("/raiz", methods=['POST',"GET"])
def raiz():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2'] 
        this.resultadoFinal = calculadora.potencia(numero1, numero2)
        return render_template("raiz.html",titulo='Raíz',resultado=this.resultadoFinal)

#########
@app.route("/tabuada", methods=['POST','GET'])
def tab():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calculadora.tabuada(numero1, numero2)
        return render_template("tabuada.html",título='Raíz',resultado=this.resultadoFinal)





# Run the script:
if __name__ == '__main__':
    app.run(debug=True)


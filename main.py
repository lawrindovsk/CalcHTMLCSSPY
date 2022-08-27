from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)  # variável APP que guarda elementos.


@app.route("/")  # Index - primeira página de qualquer site.
def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        num1= request.form['num1']
        num2= request.form['num2']








if __name__ == '__main__':
    app.run(debug=True)

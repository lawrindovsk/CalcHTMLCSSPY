import math

class Calc:
    def __init__(self):
        pass

    def somar(self, num1, num2):
        return float(num1 + num2)

    def subtrair(self, num1, num2):
        return float(num1 - num2)

    def multiplicar(self, num1, num2):
        return float(num1 * num2)

    def dividir(self, num1, num2):
        if float(num2) == 0:
            return "Impossível dividir por zero!"
        else:
            return float(num1/num2)

    def potencia(self, base, expoente):
        if expoente == 0:
            return 1
        elif expoente == 1:
            return base
        else:
            return math.pow(float(base, expoente))

    def raiz(self, num):
        if float(num) < 0:
            return "Impossível calcular"
        else:
            return math.sqr(float(num)) 

    def tabuada(self, num):
        for i in range(11):
            resultado = resultado + "\n{} * {} = {}".format(num, i, float(float(num*i)))
        return resultado








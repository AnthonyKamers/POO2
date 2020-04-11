#Anthony Bernardo Kamers - 19204700

from fractions import Fraction
from random import randint

def mmc(x1, x2):
    if x1 > x2:
        maior = x1
    else:
        maior = x2
    
    while True:
        if (maior % x1 == 0) and (maior % x2 == 0):
            return maior
        else:
            maior += 1

def criaFracao(numReal):
    string = str(numReal)
    explode = string.split('.')
    count = len(explode[1])

    multiplicador = 10 ** count

    cima = numReal * multiplicador
    cima = int(cima)

    x = Fraction(cima, multiplicador)
    string1 = str(x)
    explode1 = string1.split('/')

    fracao = Fracao(int(explode1[0]), int(explode1[1]))
    return fracao

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def show(self):
        #print(f'{self.numerador}/{self.denominador}')
        print(Fraction(self.numerador, self.denominador))

    def multiplicacao(self, fracao1):
        num1 = fracao1.numerador
        denom1 = fracao1.denominador

        resultado = Fraction((self.numerador * num1), (self.denominador * denom1)) #usa lib somente para apresentar "certinho"

        print(resultado)

    def divisao(self, fracao1):
        num1 = fracao1.numerador
        denom1 = fracao1.denominador

        resultado = Fraction((self.numerador * denom1), (self.denominador * num1))
        print(resultado)

    def soma(self, fracao1):
        num1 = fracao1.numerador
        denom1 = fracao1.denominador

        mmc1 = mmc(self.denominador, denom1)
        
        cima = ((mmc1 / self.denominador) * self.numerador) + ((mmc1 / denom1) * num1)
        cima = int(cima)

        resultado = Fraction(cima, mmc1)
        print(resultado)

    def subtracao(self, fracao1):
        num1 = fracao1.numerador
        denom1 = fracao1.denominador

        mmc1 = mmc(self.denominador, denom1)
        
        cima = ((mmc1 / self.denominador) * self.numerador) - ((mmc1 / denom1) * num1)
        cima = int(cima)

        resultado = Fraction(cima, mmc1)
        print(resultado)

    def inverteFracao(self):
        invertido = Fracao(self.denominador, self.numerador)

        invertido.show()
    
    def valorReal(self):
        valorReal = self.numerador / self.denominador
        print(valorReal)
        #return valorReal

class Fatorial:
    def __init__(self, numero):
        self.numero = numero

    def fatorial(self):
        def fat(numero):
            if numero == 0 or numero == 1:
                return 1
            else:
                return numero * fat(numero-1)
        return fat(self.numero)

class Combinacao:
    def __init__(self, elementos, posicoes):
        self.elementos = elementos #lista tamanho n
        self.posicoes = posicoes #numero posicoes p
        self.n = len(self.elementos)

    def arranjo(self):
        numerador = Fatorial(self.n).fatorial()
        denominador = Fatorial(self.n - self.posicoes).fatorial()

        fracao = Fracao(numerador, denominador).show()

    def permutacao(self):
        resultado = Fatorial(self.n).fatorial()
        print(resultado)

    def combinacao(self):
        numerador = Fatorial(self.n).fatorial()
        denominador = Fatorial(self.posicoes).fatorial() * Fatorial(self.n - self.posicoes).fatorial()

        fracao = Fracao(numerador, denominador).show()

arranjo = Combinacao(['A', 'M', 'O', 'R'], 2)
#arranjo.arranjo()
#arranjo.combinacao()
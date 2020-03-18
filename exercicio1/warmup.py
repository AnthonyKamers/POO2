#Anthony Bernardo Kamers - 19204700
#Warm Up

#Questão 1
class Televisao:
    def __init__(self):
        self.canal = 2
        self.ligada = False

#Questão 2
class Televisao:
    def __init__(self, tamanho, marca, ligada = False, canal = 2):
        self.tamanho = tamanho
        self.marca = marca        
        
        self.canal = 2
        self.ligada = False
        
tv1 = Televisao('42', 'Samsung')
tv2 = Televisao('22', 'LG')

print(tv1.tamanho)
print(tv1.marca)

print(tv2.tamanho)
print(tv2.marca)

#Questão 3
class Televisao:
    def __init__(self, tamanho, marca, canal = 2):
        self.tamanho = tamanho
        self.marca = marca        
        
        self.canal = canal
        self.ligada = False
    
    def muda_canal_para_cima(self):
        self.canal += 1
    
    def muda_canal_para_baixo(self):
        self.canal -= 1
        

#Questão 4
class Televisao:
    def __init__(self, tamanho, marca, canal = 2):
        self.tamanho = tamanho
        self.marca = marca        
        
        self.canal = canal
        self.ligada = False
        
        self.canal_minimo = 1
        self.canal_maximo = 99
    
    def muda_canal_para_cima(self):
        if self.canal == self.canal_maximo:
            self.canal = self.canal_minimo
        else:
            self.canal += 1
            
    
    def muda_canal_para_baixo(self):
        if self.canal == self.canal_minimo:
            self.canal = self.canal_maximo
        else:
            self.canal -= 1


#Questão 5
class Televisao:
    def __init__(self, tamanho, marca, canal_minimo = 2, canal_maximo = 14, canal = 2):
        self.tamanho = tamanho
        self.marca = marca        
        
        self.canal = canal
        self.ligada = False
        
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo #Cada cidade tem nome e população
    
    def muda_canal_para_cima(self):
        if self.canal == self.canal_maximo:
            self.canal = self.canal_minimo
        else:
            self.canal += 1
            
    
    def muda_canal_para_baixo(self):
        if self.canal == self.canal_minimo:
            self.canal = self.canal_maximo
        else:
            self.canal -= 1
            
#Questão 6
tv3 = Televisao(42, 'samsung', canal_minimo = 1, canal_maximo = 14)
tv4 = Televisao(32, 'AOC', canal_minimo = 2, canal_maximo = 15)


#Questão 7
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades1 = cidades
        self.cidades = []

        for i in range(0, len(self.cidades1), 2):
            cidade = Cidade(self.cidades1[i], self.cidades1[i+1])
            self.cidades.append(cidade)
    
    def calculaPopulacao(self): 
        populacaoEstado = 0
        
        for i in self.cidades:
            populacaoEstado += i.populacao
        
        print(populacaoEstado)
        #return populacaoEstado

sc = Estado('Santa Catarina', 'SC', ['tijucas', 35000, 'itapema', 75000])
pr = Estado('Paraná', 'PR', ['curitiba', 3500000, 'cascavel', 120000])
rs = Estado('Rio Grande do Sul', 'RS', ['porto alegre', 1000000, 'são bento', 100000])

sc.calculaPopulacao()
pr.calculaPopulacao()
rs.calculaPopulacao()


#Questão 8
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrarCoordenada(self):
        print(self.x, self.y)
        #return self.x, self.y
    
    def distanciaCoordenada(self, ponto1):
        #self.ponto1 = ponto1

        x1 = ponto1.x
        y1 = ponto1.y

        distancia = (((self.x - x1) ** 2) + ((self.y - y1) ** 2)) ** 0.5

        print(distancia)
        #return distancia

    def compararCoordenada(self, ponto1):
        #self.ponto1 = ponto1
        x1 = ponto1.x
        y1 = ponto1.y

        print("Ponto 1: ", self.x, ",", self.y)
        print("Ponto 2: ", x1, ",", y1)

        if(self.x == x1 and self.y == y1):
            print("Pontos são iguaus")
        else:
            print("Pontos são diferentes")

    def coordenadaPolar(self):
        r = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        tanTeta = self.y / self.x

        print("r = ", r)
        print("Tangente de Teta = ", tanTeta)
        #return r, tantTeta

# ponto1 = Coordenada(1, 1)
# ponto2 = Coordenada(1, 4)

# ponto1.distanciaCoordenada(ponto2)
# ponto1.compararCoordenada(ponto2)
# ponto1.coordenadaPolar()


#Questão 9
import math #biblioteca no meio do código somente para ilustrar o exercício

class Quadrado:
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura
    
    def area(self):
        area = self.comprimento * self.altura

        print(area)
        #return area

class Retangulo:
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura
    
    def area(self):
        area = self.comprimento * self.altura

        print(area)
        #return area

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        area = math.pi * (self.raio ** 2) #usa lib para fazer conta com "pi"

        print(area)
        #return area


#Questão 10
from fractions import Fraction #biblioteca no meio do código, somente para ilustrar exercício

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
        print(f'{self.numerador}/{self.denominador}')
        #print(Fraction(self.numerador, self.denominador))

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


fracao1 = Fracao(1, 2)
fracao2 = Fracao(2, 3)

fracaoNova = criaFracao(0.75)
fracaoNova.show()
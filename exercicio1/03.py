#Anthony Bernardo Kamers - 19204700

class Polinomio:
    def __init__(self, numeros):
        self.numeros = numeros
        self.polinomio = []
        self.dic = {}

        self.grau = 0

        for k, v in enumerate(self.numeros):
            self.dic['coeficiente'] = v
            self.dic['x'] = k
            self.polinomio.append(self.dic.copy())
            self.dic.clear()

            self.grau = k
        
    def getGrau(self):
        print(self.grau)
        #return self.grau

    def getX(self, x):
        valor = 0
        for k, v in enumerate(self.numeros):
            valor += v * x**k

        print(valor)
        #return valor

    def somarPolinomio(self, polinomio):
        len1 = len(self.numeros)
        len2 = len(polinomio.numeros)

        expressao = []
        expressao1 = []

        if len1 > len2:
            for k, v in enumerate(self.numeros):
                for k1, v1 in enumerate(polinomio.numeros):
                    if k == k1:
                        self.dic['coeficiente'] = v + v1
                        self.dic['x'] = k
                        expressao.append(self.dic.copy())
                        self.dic.clear()

                        expressao1.append(v + v1)
                
                if k > len2 - 1:
                    self.dic['coeficiente'] = v
                    self.dic['x'] = k
                    expressao.append(self.dic.copy())
                    self.dic.clear()

                    expressao1.append(v)
        
        elif len2 > len1:
            for k, v in enumerate(polinomio.numeros):
                for k1, v1 in enumerate(self.numeros):
                    if k == k1:
                        self.dic['coeficiente'] = v + v1
                        self.dic['x'] = k
                        expressao.append(self.dic.copy())
                        self.dic.clear()

                        expressao1.append(v + v1)
                
                if k > len1 - 1:
                    self.dic['coeficiente'] = v
                    self.dic['x'] = k
                    expressao.append(self.dic.copy())
                    self.dic.clear()

                    expressao1.append(v)

        elif len1 == len2:
            for k, v in enumerate(polinomio.numeros):
                for k1, v1 in enumerate(self.numeros):
                    if k == k1:
                        self.dic['coeficiente'] = v + v1
                        self.dic['x'] = k
                        expressao.append(self.dic.copy())
                        self.dic.clear()

                        expressao1.append(v + v1)

        #print(expressao)
        #print(expressao1)

        lenFinal = len(expressao1)
        for k, v in enumerate(expressao1):
            if k == 0:
                print(f'{v} + ', end="")
            elif k > 0 and k < lenFinal-1:
                print(f'{v}*x^{k} + ', end="")
            else:
                print(f'{v}*x^{k}')


    def multiplicaPolinomio(self, polinomio):
        len1 = len(self.numeros)
        len2 = len(polinomio.numeros)

        resultado = len1 * len2

        expressao = []
        for i in range(0, resultado):
            expressao.append(0)
        
        for k, v in enumerate(self.numeros):
            for k1, v1 in enumerate(polinomio.numeros):
                x = k + k1
                coeficiente = v * v1
                expressao[x] = expressao[x] + coeficiente

        index1 = expressao.index(0)

        del(expressao[index1:len(expressao)])
        
        lenFinal = len(expressao)
        for k, v in enumerate(expressao):
            if k == 0:
                print(f'{v} + ', end="")
            elif k > 0 and k < lenFinal-1:
                print(f'{v}*x^{k} + ', end="")
            else:
                print(f'{v}*x^{k}')

# x = Polinomio([1, 1])
# y = Polinomio([1, 1, 1])

# x.somarPolinomio(y)
# x.multiplicaPolinomio(y)
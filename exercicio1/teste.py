class Teste:
    def __init__(self, valor = 0):
        self.valor = valor

    def aumenta(self, valor1):
        self.valor += valor1

        print(self.valor)

a = Teste()
a.aumenta(150)
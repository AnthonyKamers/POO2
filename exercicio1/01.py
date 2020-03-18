#Anthony Bernardo Kamers - 19204700

print("Banco Tatu")

class ContaCorrente:
    def __init__(self, titulares=[], saldo=0, extrato=[], especial = False, poupanca = False):
        self.titulares = titulares #list[nome, telefone]
        self.saldo = saldo
        self.extrato = extrato
        self.especial = especial
        self.poupanca = poupanca

        self.dic = {}

    #setters
    def especial(self, especial1, valorEspecial):
        self.especial = especial1

        self.contaEspecial.addLimiteEspecial(valorEspecial)

        print(self.limiteEspecial)

    def poupanca(self, poupanca1):
        self.poupanca = poupanca1

    def addTitular(self, nome, telefone):
        self.dic['nome'] = nome
        self.dic['telefone'] = telefone
        self.titulares.append(self.dic.copy())
        self.dic.clear()
        print("Titular adicionado com sucesso")

    #methods
    def verSaldo(self):
        print(f'Seu saldo é de: R${0:.3g}' .format(self.saldo))

    def verExtrato(self):
        for i in self.extrato:
            if i['tipo'] == "Saque":
                print('- R${0:.3g}' .format(i['valor']))

            elif i['tipo'] == "Deposito":
                print('+ R${0:.3g}' .format(i['valor']))

        print(f'Saldo Final: R${0:.3g}' .format(self.saldo))

    def verTitulares(self):
        for i in self.titulares:
            print(f'Nome: {i["nome"]} | Telefone: {i["telefone"]}')

    def saque(self, valor):
        if self.saldo < valor:
            print("Você não tem saldo suficiente!")
        else:
            self.saldo -= valor
            self.dic['tipo'] = "Saque"
            self.dic['valor'] = valor
            self.extrato.append(self.dic.copy())
            self.dic.clear()
            print('Saque de R${0:.3g} efetuado com sucesso' .format(valor))
    
    def deposito(self, valor):
        self.saldo += valor
        self.dic['tipo'] = "Deposito"
        self.dic['valor'] = valor
        self.extrato.append(self.dic.copy())
        self.dic.clear()
        print('Depósito de R${0:.3g} efetuado com sucesso' .format(valor))

# class ContaEspecial(ContaCorrente):
#     def addLimiteEspecial(self, limite):
#         self.limiteEspecial = limite


anthony = ContaCorrente()
anthony.addTitular("Anthony", "48984685758")
anthony.verTitulares()
anthony.verSaldo()
anthony.deposito(250)
anthony.verExtrato()
anthony.saque(300)
anthony.saque(100)
anthony.verExtrato()
#Anthony Bernardo Kamers - 19204700
#Como deve ter limite especial e poupança, fiz métodos separados para cada um. Ao fazer um saque ou depósito e tenha usado limite especial (se for esse tipo de conta), é feita a verificação e adicionado a cada campo

print("Banco Tatu")

class ContaCorrente:
    def __init__(self, titulares=[], saldo = 0, extrato=[]):
        self.titulares = titulares #list[nome, telefone]
        self.saldo = saldo
        self.extrato = extrato

        self.especial = False
        self.poupanca = False
        self.limiteEspecial = 0
        self.limiteUsado = 0
        self.rendimentoPoupanca = 0 #porcentagem mes

        self.dic = {}

    #setters
    def especial1(self, especial1 = False, limite = 0):
        self.especial = especial1

        if(especial1):
            self.limiteEspecial = limite
        else:
            self.limiteEspecial = 0


    def poupanca1(self, poupanca1, rendimentoMensal):
        self.poupanca = poupanca1

        if(poupanca1):
            self.rendimentoPoupanca = rendimentoMensal
        else:
            self.rendimentoPoupanca = 0

    def addRendimentoPoupanca(self): #fazer rotina q repita a cada mês
        if(self.poupanca):
            x = (self.saldo * self.rendimentoPoupanca) / 100
            self.saldo += x

            self.dic['tipo'] = "Rendimento"
            self.dic['valor'] = x
            self.extrato.append(self.dic.copy())
            self.dic.clear()

        else:
            print('Não tem rendimento de poupança')

    def addTitular(self, nome, telefone):
        self.dic['nome'] = nome
        self.dic['telefone'] = telefone
        self.titulares.append(self.dic.copy())
        self.dic.clear()
        print("Titular adicionado com sucesso")

    #methods
    def verSaldo(self):
        print('Seu saldo é de: R${0:.3g}' .format(self.saldo))

        if(self.limiteEspecial):
            print('Seu limite especial é de: R${0:.3g}' .format(self.limiteEspecial))
            print('Seu limite usado é de: R${0:.3g}' .format(self.limiteUsado))
            print('Seu limite a usar é de: R${0:.3g}' .format(self.limiteEspecial - self.limiteUsado))

    def verExtrato(self):
        for i in self.extrato:
            if i['tipo'] == "Saque":
                print('- R${0:.3g}' .format(i['valor']))

            elif i['tipo'] == "Deposito":
                print('+ R${0:.3g}' .format(i['valor']))

            elif i['tipo'] == "Rendimento":
                print('+ R${0:.3g} - Rendimento' .format(i['valor']))

        print('Saldo Final: R${0:.3g}' .format(self.saldo))

    def verTitulares(self):
        for i in self.titulares:
            print(f'Nome: {i["nome"]} | Telefone: {i["telefone"]}')

    def saque(self, valor):
        if((not self.especial and self.saldo < valor) or (self.especial and (self.saldo + (self.limiteEspecial - self.limiteUsado)) < valor)):
            print("Você não tem saldo suficiente")
        else:
            if(self.saldo > valor):
                self.saldo -= valor
            
            else:
                if(self.especial and (self.saldo + (self.limiteEspecial - self.limiteUsado)) > valor):
                    limiteUsado = (valor - self.saldo)
                    self.limiteUsado += limiteUsado
                    self.saldo -= valor
            
            self.dic['tipo'] = "Saque"
            self.dic['valor'] = valor
            self.extrato.append(self.dic.copy())
            self.dic.clear()
            print('Saque de R${0:.3g} efetuado com sucesso' .format(valor))
    
    def deposito(self, valor):
        self.saldo += valor

        if(self.especial and self.limiteUsado != 0):
            if (self.limiteUsado + valor > self.limiteEspecial):
                self.limiteUsado = 0
            else:
                self.limiteUsado += valor

        self.dic['tipo'] = "Deposito"
        self.dic['valor'] = valor
        self.extrato.append(self.dic.copy())
        self.dic.clear()
        print('Depósito de R${0:.3g} efetuado com sucesso' .format(valor))


# anthony = ContaCorrente(saldo = 150)
# anthony.addTitular("Anthony", "48984685758")
# anthony.verSaldo()
# anthony.especial1(True, 350)
# anthony.verSaldo()
# anthony.saque(400)
# anthony.verSaldo()
# anthony.deposito(300)
# anthony.verSaldo()
# anthony.poupanca1(True, 1)
# anthony.addRendimentoPoupanca()
# anthony.verExtrato()
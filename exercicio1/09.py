#Anthony Bernardo Kamers
#Campo Minado (15 x 15)

from random import randint

class CampoMinado:
    def __init__(self):
        self.qtdBombas = randint(35, 55) #bombas aleatórias (de 35 a 55 bombas)
        self.campo = []
        self.bombas = []

        self.qtdJogadas = 225 - self.qtdBombas #225 porque é 15 * 15
        self.qtd = 0 #cada jogada do usuário aumenta 1 (se não for bomba)

        self.abertos = [] #campos q são abertos a cada abrirCampos()

        #preencher campo minado
        for i in range(0, 15):
            x = []
            for j in range(0, 15):
                x.append([0, 0])
            self.campo.append(x)

        #preencher campo minado com bombas
        i = 0
        while True:
            linha = randint(0, 14)
            coluna = randint(0, 14)

            while(self.campo[linha][coluna][1] == 'X'):
                linha = randint(0, 14)
                coluna = randint(0, 14)

            self.bombas.append([linha, coluna])
            self.campo[linha][coluna][1] = 'X'
            i += 1

            if i == self.qtdBombas:
                break

        
        #preencher com números (perto das bombas)
        for i in range(0, len(self.bombas)):
            for linha in range(0, len(self.campo)):
                for coluna in range(0, len(self.campo)):
                    if self.campo[linha][coluna][1] == 'X':
                        pass
                    else:
                        if ((linha == self.bombas[i][0] - 1 or linha == self.bombas[i][0] or linha == self.bombas[i][0] + 1) and (coluna == self.bombas[i][1] - 1 or coluna == self.bombas[i][1] or coluna == self.bombas[i][1] + 1)):
                            self.campo[linha][coluna][1] += 1
                            

        #chamar função do jogo
        self.play()

    #show do campo minado (abertos ou não)
    def show(self):
        print('''      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14''')
        for linha in range(0, len(self.campo)):
            if linha < 10:
                print(f'{linha}  - ', end='')
            else:
                print(f'{linha} - ', end='')

            for coluna in range(0, len(self.campo)):
                if self.campo[linha][coluna][0] == 0:
                    print('[ ]', end=' ')
                else:
                    print(f'[{self.campo[linha][coluna][1]}]', end=' ')
            print()

    def atacar(self, x, y):

        if self.campo[x][y][0] == 1:
            return 'preenchido'

        else:
            if self.campo[x][y][1] == 'X':
                return 'bomba'
            
            elif self.campo[x][y][1] == 0:
                self.campo[x][y][0] = 1 #abre campo
                self.qtd += 1 #aumenta, dizendo q abriu mais um campo
                return 'vazio'
            
            else:
                self.campo[x][y][0] = 1 #abre campo
                self.qtd += 1 #aumenta, dizendo q abriu mais um campo
                return 'numero'

    def abrirCampos(self, x, y):
        for linha in range(0, len(self.campo)):
            for coluna in range(0, len(self.campo)):
                if ((linha == x - 1 or linha == x or linha == x + 1) and (coluna == y - 1 or coluna == y or coluna == y + 1)):
                    resp = self.atacar(linha, coluna)

                    if resp == 'vazio': #or resp == 'numero':
                        self.abertos.append([linha, coluna])

    #sempre abre o primeiro item (index = 0)
    def abrirAbertos(self):
        while len(self.abertos) > 0:
            self.abrirCampos(self.abertos[0][0], self.abertos[0][1])

            self.abertos.pop(0)
    
    #método q faz o usuário jogar
    def play(self):
        while True:
            self.show()
            campo = input("Diga as coordenadas do campo que deseja atacar (x,y): ")

            campo1 = campo.split(',')
            x = int(campo1[0])
            y = int(campo1[1])

            resposta = self.atacar(x, y)

            if resposta == 'bomba':
                self.perdeu()
                break

            elif resposta == 'vazio':
                self.abrirCampos(x, y)
                self.abrirAbertos()
            
            elif resposta == 'numero':
                pass #só abre o próprio campo

            elif resposta == 'preenchido':
                print('já preenchido')

            if(self.qtd == self.qtdJogadas):
                self.ganhou()
                break
    
    def perdeu(self):
        print('Você explodiu uma bomba! Você perdeu')

        #mostrar para o usuário o self.campo inteiro
        for linha in range(0, len(self.campo)):
            print('', end='')
            for coluna in range(0, len(self.campo)):
                print(self.campo[linha][coluna][1], end=' ')
            print()
        
        self.campoInteiro()

    def ganhou(self):
        print('Parabéns!! Você ganhou!! Abriu todos os campos sem abrir nenhuma bomba!!')

        self.campoInteiro()

    def campoInteiro(self):
        for linha in range(0, len(self.campo)):
            print('', end='')
            for coluna in range(0, len(self.campo)):
                print(self.campo[linha][coluna][1], end=' ')
            print()



if __name__ == "__main__":
    campoMinado = CampoMinado()
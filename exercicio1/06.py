#Anthony Bernardo Kamers
#Baralho de cartas convencional (baralho de 52 cartas) - Pode escolher se quer 1 baralho de 52 cartas(52 cartas) ou 2 (104 cartas)

from random import randint

class Baralho:
    def __init__(self, tipoBaralho): #tipoBaralho = int (recebe 52 ou 104)
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        naipes = ['copas', 'paus', 'espadas', 'ouros']

        if tipoBaralho != 52 and tipoBaralho != 104:
            self.tipoBaralho = 104
        else:
            self.tipoBaralho = tipoBaralho

        self.cartas = []

        for i in numeros:
            for j in naipes:
                self.cartas.append([i, j])

    def distribuir(self, qtdCartas, qtdJogadores): #qtdCartas por jogador
        jogadores = []
        cartasAleatorias = []

        for i in range(0, qtdJogadores):
            jogadores.append([])

            for j in range(0, qtdCartas):

                if self.tipoBaralho == 52:
                    cartaAleatoria = randint(0, 51)

                    while cartaAleatoria in cartasAleatorias:
                        cartaAleatoria = randint(0, 51)
                else:
                    cartaAleatoria = randint(0, 51)
                    count = cartasAleatorias.count(cartaAleatoria)
                    
                    while count == 2:
                        cartaAleatoria = randint(0, 51)
                        count = cartasAleatorias.count(cartaAleatoria)

                jogadores[i].append(self.cartas[cartaAleatoria])
                cartasAleatorias.append(cartaAleatoria)

        self.jogadores = jogadores #opcao de trabalhar com a classe jogadores (self.jogadores)
        return jogadores #opcao de trabalhar individualmente com a lista jogadores

    def printJogadores(self):
        for i in self.jogadores:
            print(i)


# baralho = Baralho(104)
# baralho.distribuir(9, 4)
# baralho.printJogadores()
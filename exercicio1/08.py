#Anthony Bernardo Kamers - 19204700
#Jogo Forca - POO

#imports
import os
import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

#global variable (usage)
clear = lambda: os.system('clear') #on Linux System

class JogoForca:
    def __init__(self):
        self.palavraFormada = []
        self.palavraLista = []
        self.letrasPalavra = []

        self.erros = 0
        self.acertos = 0
        self.letrasEscolhidas = []

        #lista de categorias (para sozinho - site: palabrasaleatorias.com)
        self.listaCategoria = ['Todas', 'Alimentos', 'Animais', 'Cores', 'Corpo Humano', 'Educação', 'Família', 'Figuras Geométricas']

        print("Jogo da Forca \n")
        print("Na categoria sozinho, você escolhe uma categoria e uma palavra é gerada automaticamente")
        print("Na categoria multiplayer, um desafiante escolhe uma categoria e uma palavra e o desafiado tenta acertar")
        print("Em ambos os jogos, há a possibilidade de errar 7 vezes \n")

        tipoJogo = int(input("Você deseja jogar sozinho(1) ou multiplayer(2): "))

        if tipoJogo == 1:
            self.alone()
        else:
            self.multiplayer()

    def alone(self):
        print("Categorias: ")
        for i in range(0, len(self.listaCategoria)):
            if i == 0:
                print(f'{i} - {self.listaCategoria[i]}')
            
            else:
                print(f'{i+1} - {self.listaCategoria[i+1]}')
                if i == 6:
                    break

        categoria = int(input('Escolha uma categoria: '))

        while(categoria == 1 or categoria > 8 or categoria < 0):
            categoria = int(input("Categoria: \n 0 - Todas \n 2 - alimentos \n 3 - animais \n 4 - cores \n 5 - corpo humano \n 6 - educação \n 7 - família \n 8 - figuras geométricas \n : "))

        categoria = str(categoria)

        url = "https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1&fs2=" + categoria + "&Submit=Nova+palavra"

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        palavraDiv = soup.find('div', attrs={'style': 'font-size:3em; color:#6200C5;'})

        palavra = palavraDiv.text
        palavra = palavra.replace('\n', '')
        palavra = palavra.replace('\r', '')
        palavra = palavra.lower()

        self.categoria = categoria
        self.palavra = palavra

        #inicia procedimentos formação palavra
        self.format()

    def multiplayer(self):
        self.categoria = input("Desafiante: Qual a categoria da palavra: ")
        self.palavra = input("Desafiante: Qual a palavra que você quer: ")

         #inicia procedimentos formação palavra
        self.format()

    def format(self):
        #print(self.palavra)
        self.lenPalavra = len(self.palavra)

        for i in range(self.lenPalavra):
            self.palavraFormada.append("_")

        for i in self.palavra:
            if self.letrasPalavra.count(i) == 0:
                self.letrasPalavra.append(i)
            self.palavraLista.append(i)

        self.lenLetrasPalavra = len(self.letrasPalavra)

        #usa o OS para dar clear no terminal (linux somente)
        clear()

        #começa processos para mostrar para o usuário
        self.jogo()
    
    def jogo(self):
        #while do usuário: identificar as letras que o usuário digitou, ver se acertou/errou e mostrar
        while True:

            #apresentar categoria escolhida para o usuário
            if(self.categoria == "0" or self.categoria == "2" or self.categoria == "3" or self.categoria == "4" or self.categoria == "5" or self.categoria == "6" or self.categoria == "7" or self.categoria == "8"):
                if self.categoria == "0":
                    print("Desafiado: A categoria da palavra é {}" .format(self.listaCategoria[0]))
                else:
                    print("Desafiado: A categoria da palavra é {}" .format(self.listaCategoria[int(self.categoria)-1]))
            else:
                print("Desafiado: A Categoria da palavra é: {}" .format(self.categoria))

            #apresentar informações para o usuário
            print("Desafiado: A palavra formada é: {}" .format(self.palavraFormada))
            print("Desafiado: As letras escolhidas até agora foram: {}" .format(self.letrasEscolhidas))
            print("Desafiado: A sua quantidade de erros é: {} \n" .format(self.erros))
            letra = input("Desafiado: escolha uma letra: ")

            while(len(letra) == 0 or len(letra) > 1):
                letra = input("Parâmetro errados para letra: Desafiado: escolha uma letra: ")

            self.letrasEscolhidas.append(letra)
            
            lenCerto = 0    
            
            #ver se a palavra já está certa
            for i in self.letrasEscolhidas:
                for j in self.letrasPalavra:
                    if i == j:
                        lenCerto += 1
            
            #se está certo, adiciona à flag acertos 1, se não, vê se somente acertou uma letra ou errou e adiciona em cada variável
            if lenCerto == self.lenLetrasPalavra:
                self.acertos += 1
            else:
                if self.letrasPalavra.count(letra) == 0:
                    self.erros += 1
                    print("Você errou essa! \n")
                else:
                    k = 0
                    for i in self.palavraLista:
                        if i == letra:
                            self.palavraFormada[k] = letra
                        k += 1
                            
                    print("Você acertou uma! \n")
            
            #testa as variáveis para, se for o caso, dar break no loop
            if self.erros == 7:
                break
            
            if self.acertos == 1:
                break
        
        #mostra resultados para o usuário
        self.showResults()

    def showResults(self):
        #apresentar as informações finais para o usuário
        if(self.erros == 7):
            print("Desafiado: Você não conseguiu acertar a palavra! A palavra era: ")
            print(self.palavra)

        elif (self.acertos == 1):
            print("Desafiado: Parabéns! Você acertou! A palavra era: {}" .format(self.palavra))


#inicia já com a classe JogoForca
if __name__ == "__main__":
    jogo = JogoForca()
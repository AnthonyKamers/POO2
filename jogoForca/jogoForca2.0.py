import os
import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

clear = lambda: os.system('clear') #on Linux System

print("Jogo da Forca \n")
print("Na categoria sozinho, você escolhe uma categoria e uma palavra é gerada automaticamente")
print("Na categoria multiplayer, um desafiante escolhe uma categoria e uma palavra e o desafiado tenta acertar")
print("Em ambos os jogos, há a possibilidade de errar 7 vezes \n")

palavraFormada = []
palavraLista = []

listaCategoria = ['Todas', 'Alimentos', 'Animais', 'Cores', 'Corpo Humano', 'Educação', 'Família', 'Figuras Geométricas']

tipoJogo = int(input("Você deseja jogar sozinho(1) ou multiplayer(2): "))

if(tipoJogo == 1):
    categoria = int(input("Categoria: \n 0 - Todas \n 2 - alimentos \n 3 - animais \n 4 - cores \n 5 - corpo humano \n 6 - educação \n 7 - família \n 8 - figuras geométricas \n : "))

    while(categoria == 1 or categoria == 9):
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

else:
    categoria = input("Desafiante: Qual a categoria da palavra: ")

    palavra = input("Desafiante: Qual a palavra que você quer: ")

print(palavra)
lenPalavra = len(palavra)

for i in range(lenPalavra):
    palavraFormada.append("_")

letrasPalavra = []

for i in palavra:
    if letrasPalavra.count(i) == 0:
        letrasPalavra.append(i)
    palavraLista.append(i)

lenLetrasPalavra = len(letrasPalavra)

erros = 0
acertos = 0

letrasEscolhidas = []

clear()


while True:

    #apresentar categoria escolhida para o usuário
    if(categoria == "0" or categoria == "2" or categoria == "3" or categoria == "4" or categoria == "5" or categoria == "6" or categoria == "7" or categoria == "8"):
        if categoria == "0":
            print("Desafiado: A categoria da palavra é {}" .format(listaCategoria[0]))
        else:
            print("Desafiado: A categoria da palavra é {}" .format(listaCategoria[int(categoria)-1]))
    else:
        print("Desafiado: A Categoria da palavra é: {}" .format(categoria))

    print("Desafiado: A palavra formada é: {}" .format(palavraFormada))
    print("Desafiado: As letras escolhidas até agora foram: {}" .format(letrasEscolhidas))
    print("Desafiado: A sua quantidade de erros é: {} \n" .format(erros))
    letra = input("Desafiado: escolha uma letra: ")
    letrasEscolhidas.append(letra)
    
    lenCerto = 0    
    
    for i in letrasEscolhidas:
        for j in letrasPalavra:
            if i == j:
                lenCerto += 1
    
    if lenCerto == lenLetrasPalavra:
        acertos += 1
    else:
        if letrasPalavra.count(letra) == 0:
            erros += 1
            print("Você errou essa! \n")
        else:
            k = 0
            for i in palavraLista:
                if i == letra:
                    palavraFormada[k] = letra
                k += 1
                    
            print("Você acertou uma! \n")
    
    if erros == 7:
        break
    
    if acertos == 1:
        break


if(erros == 7):
    print("Desafiado: Você não conseguiu acertar a palavra! A palavra era: ")
    print(palavra)

elif (acertos == 1):
    print("Desafiado: Parabéns! Você acertou! A palavra era: {}" .format(palavra))
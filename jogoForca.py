import os
clear = lambda: os.system('clear') #on Linux System


print("Jogo da Forca \n")
print("Para funcionar, o desafiante deve escolher uma palavra e o desafiado deve tentar adivinhar com letras. \n")

palavraFormada = []
palavraLista = []

categoria = input("Desafiante: Qual a categoria da palavra: ")

palavra = input("Desafiante: Qual a palavra que você quer: ")

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
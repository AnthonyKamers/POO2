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
        self.canal_maximo = canal_maximoCada cidade tem nome e população
    
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



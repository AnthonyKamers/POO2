#Questão 7
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        
        for i in range(0, len(cidades) + 1, 2):
            cidade = Cidade(cidades[i], cidades[i+1])
            self.cidades.append(cidade)
    
    def calculaPopulacao(self): 
        populacaoEstado = 0
        
        for i in self.cidades:
            populacaoEstado += i.populacao
        
        return populacaoEstado

sc = Estado('Santa Catarina', 'SC', ['tijucas', 35000, 'itapema', 75000])
pr = Estado('Paraná', 'PR', ['curitiba', 3500000, 'cascavel', 120000])
rs = Estado('Rio Grande do Sul', 'RS', ['porto alegre', 1000000, 'são bento', 100000])

sc.calculaPopulacao()
pr.calculaPopulacao()
rs.calculaPopulacao()
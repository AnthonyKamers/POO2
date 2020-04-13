#Anthony Bernardo Kamers - 19204700

class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def getNome(self):
        return self.nome

class Professor:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def getData(self):
        print(f'''
            Nome: {self.nome}
            CPF: {self.cpf}
        ''')

class Turma:
    def __init__(self, turma_id, professor, alunos):
        self.turma_id = turma_id
        self.professor = professor
        self.alunos = alunos #lista []

        self.dic = {}
        self.notas = []
        self.presenca = []
    
    def getProfessor(self):
        self.professor.getData()

    def addNota(self, nomeAluno, nota):
        s = 'n'
        for i in self.alunos:
            if i.getNome() == nomeAluno:
                self.dic['nota'] = nota
                self.dic['aluno'] = i
                self.notas.append(self.dic.copy())

                self.dic.clear()
                s = 's'
                break
        
        if s == 'n':
            print('Não foi encontrado o aluno')
        else:
            print('Nota atualizada')
    
    def addPresenca(self, nomeAluno, diaPresenca):
        s = 'n'
        for i in self.alunos:
            if i.getNome() == nomeAluno:
                self.dic['diaPresenca'] = diaPresenca
                self.dic['aluno'] = i
                self.presenca.append(self.dic.copy())

                self.dic.clear()
                s = 's'
                break
        
        if s == 'n':
            print('Não foi encontrado o aluno')
        else:
            print('Presença atualizada')

    def getAlunosData(self):
        for i in self.alunos:
            print(f'Nome: {i.getNome()}')

            print('Notas: ')
            for j in self.notas:
                if j['aluno'] == i:
                    print(j['nota'])
            
            print('Presença: ')
            for k in self.presenca:
                if k['aluno'] == i:
                    print(k['diaPresenca'])
            
            print()
    
    def getAluno(self, aluno):
        for i in self.alunos:
            if i == aluno:
                print(f'Nome: {i.getNome()}')

                print('Notas: ')
                for j in self.notas:
                    if j['aluno'] == i:
                        print(j['nota'])
                
                print('Presença: ')
                for k in self.presenca:
                    if k['aluno'] == i:
                        print(k['diaPresenca'])


class Usuario: #secretaria
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    
    def getProfessorTurma(self, turma):
        turma.getProfessor()

    def getAlunosTurma(self, turma):
        turma.getAlunosData()

    def getAlunoTurma(self, turma, aluno):
        turma.getAluno(aluno)


    
# anthony = Aluno('Anthony', 123)
# bernardo = Aluno('Bernardo', 456)
# mateus = Professor('Mateus', 123)

# poo2 = Turma(2, mateus, [anthony, bernardo])
# poo2.addNota("Anthony", 8)
# poo2.addNota("Anthony", 10)
# poo2.addNota("Bernardo", 2)
# poo2.addNota("Bernardo", 5)

# poo2.addPresenca("Anthony", '15/02/2020')
# poo2.addPresenca("Anthony", '20/02/2020')
# poo2.addPresenca("Bernardo", '15/02/2020')
# poo2.addPresenca("Bernardo", '20/02/2020')


# usuario = Usuario('teste', 123)

# usuario.getProfessorTurma(poo2)
# usuario.getAlunosTurma(poo2)
# usuario.getAlunoTurma(poo2, anthony)
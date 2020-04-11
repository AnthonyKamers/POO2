#Anthony Bernardo Kamers - 19204700

class Usuario:
    
    def criar(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.lendo = False

    def updateSenha(self, senhaAntiga, senhaNova):
        if self.senha == senhaAntiga:
            self.senha = senhaNova
            #atualiza senha e mostra na tela
        else:
            print("Senha atual está errada")
            #mostra na tela q senha antiga está errada

    def verUsuario(self):
        print(self.usuario)

    def ler(self):
        self.lendo = True

    def naoLer(self):
        self.lendo = False

    def verLer(self):
        return self.lendo

class Autor:
    def __init__(self, nome):
        self.nome = nome

    def setNome(self, nome1):
        self.nome = nome1

    def getNome(self):
        return self.nome

class Livro:
    def __init__(self, titulo, autores, ano, editora, edicao, volume):
        self.titulo = titulo
        self.autores = autores
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume

    def getLivro(self):
        print(f"""
        Título: {self.titulo}
        Ano: {self.ano}
        Editora: {self.editora}
        Edicao: {self.edicao}
        Volume: {self.volume}
        """)

        print(f"""Autores: """, end=" ")
        for i in self.autores:
            print(i.getNome(), end=", ")

        print()

    def getAutores(self):
        autores = []
        for i in self.autores:
            autores.append(i.getNome())

        return autores

    def getTitulo(self):
        return self.titulo

class Biblioteca:
    def __init__(self, livros=[]):
        self.livros = livros

        #novo código (exercício 7)
        self.usuarios = []
        self.ativos = 0

    def addLivro(self, livro):
        self.livros.append(livro)
    
    def searchTitulo(self, usuarioI, titulo):
        s = "n"
        for i in self.livros:
            if i.titulo == titulo:
                
                #ver se usuário já está lendo
                if not self.usuarios[usuarioI].lendo:
                    print("Usuário já está lendo")

                #ver se já há alguém lendo
                elif(self.ativos != 0):
                    print("Já há um usuário ativo")

                else:
                    self.usuarios[usuarioI].ler()
                    self.ativos = 1
                    i.getLivro()
                    s = "s"
                    break

            else:
                s = "n"

        if(s == "n"):
            print("Não há livro com esse nome")

    def searchAutor(self, usuarioI, autor):
        #ver se usuário já está lendo
        if not self.usuarios[usuarioI].lendo:
            print("Usuário já está lendo")

        #ver se já há alguém lendo
        elif(self.ativos != 0):
            print("Já há um usuário ativo")

        else:
            autoresI = []

            for i in self.livros:
                x = i.getAutores()

                for j in range(0, len(x)):
                    if x[j] == autor:
                        autoresI.append(j)
                        #i.getLivro()

            if (len(autoresI) == 0):
                print("Não foi encontrado livro com esse autor")

            else:
                print(f"Encontramos {len(autoresI)} livro(s) do autor, escolha: ")

                for i in range(0, len(autoresI)):
                    print(f'{i} = {self.livros[autoresI[i]].getTitulo()}')
                
                resposta = int(input("Escolha o número referente ao livro que você deseja: "))

                while resposta < 0 or resposta > len(autoresI):
                    resposta = int(input("Escolha o número referente ao livro que você deseja: "))
                
                #mostrar livro para usuário
                self.usuarios[usuarioI].ler()
                self.ativos = 1
                self.livros[autoresI[resposta]].getLivro()

    def addUsuario(self, usuario):
        self.usuarios.append(usuario)
        #aparece mensagem tela (usuário adicionado com sucesso)

    def testaUsuario(self, usuario):
        #ver se usuario está na classe biblioteca
        x = 0
        usuarioI = 0

        for i in range(0, len(self.usuarios)):
            if self.usuarios[i] == usuario:
                x = 1
                usuarioI = i
                break
        
        if x == 0:
            return "nao cadastrado"
            #print("Esse usuário não está cadastrado")
        else:
            return usuarioI

    def lerTitulo(self, usuario, titulo):
        x = self.testaUsuario(usuario)

        if x == "nao cadastrado":
            print("Esse usuário não está no sistema da biblioteca")

        else:
            self.searchTitulo(x, titulo)

    def lerAutor(self, usuario, autor):
        x = self.testaUsuario(usuario)

        if x == "nao cadastrado":
            print("Esse usuário não está no sistema da biblioteca")

        else:
            self.searchAutor(x, autor)


# biblioteca = Biblioteca()

# anthony = Usuario()
# anthony.criar('anthony', 'anthony')
# biblioteca.addUsuario(anthony)

# autor1 = Autor("Anthony")
# autor2 = Autor("Bernardo")
# autor3 = Autor("Kamers")

# livro = Livro("Titulo Livro", [autor1, autor2, autor3], 2019, "Editora Teste", "Primeira Edição", 3)
# livro.getAutores()


# biblioteca.addLivro(livro)
# biblioteca.searchTitulo("Titulo Livro1")
# biblioteca.searchAutor("Anthony")

# biblioteca.lerTitulo(anthony, "Titulo Livro")
# biblioteca.lerAutor(anthony, "Anthony")
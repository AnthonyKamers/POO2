#Anthony Bernardo Kamers - 19204700

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

class Biblioteca:
    def __init__(self, livros=[]):
        self.livros = livros

    def addLivro(self, livro):
        self.livros.append(livro)
    
    def searchTitulo(self, titulo):
        s = "n"
        for i in self.livros:
            if i.titulo == titulo:
                i.getLivro()
                s = "s"
                break
            else:
                s = "n"

        if(s == "n"):
            print("Não há livro com esse nome")

    def searchAutor(self, autor):
        for i in self.livros:
            x = i.getAutores()

            for j in x:
                if j == autor:
                    i.getLivro()

# biblioteca = Biblioteca()

# autor1 = Autor("Anthony")
# autor2 = Autor("Bernardo")
# autor3 = Autor("Kamers")

# livro = Livro("Titulo Livro", [autor1, autor2, autor3], 2019, "Editora Teste", "Primeira Edição", 3)
# livro.getAutores()


# biblioteca.addLivro(livro)
# biblioteca.searchTitulo("Titulo Livro1")
# biblioteca.searchAutor("Anthony")
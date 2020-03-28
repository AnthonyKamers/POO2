#Anthony Bernardo Kamers - 19204700

class Usuario:
    
    def criar(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def updateSenha(self, senhaAntiga, senhaNova):
        if self.senha == senhaAntiga:
            self.senha = senhaNova
        else:
            print("Senha atual está errada")

    def verUsuario(self):
        print(self.usuario)


anthony = Usuario()
anthony.criar('anthony', 'anthony')
anthony.verUsuario()
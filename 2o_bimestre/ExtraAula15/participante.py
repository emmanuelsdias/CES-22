class Participante():

    def __init__(self, nome, login, senha, email, endereco, telefone):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    def authenticate_part(self, login_input, senha_input):
        if (self.login == login_input and self.senha == senha_input):
            return True
        return False

    @staticmethod
    def get_fields():
        return {'nome': "Nome",
                'login': "Login",
                'senha': "Senha",
                'email': "E-mail",
                'endereco': "Endereço",
                'telefone': "Telefone"}

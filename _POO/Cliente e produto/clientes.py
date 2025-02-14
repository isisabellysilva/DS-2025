from sql import Banco

class Cliente:
    def __init__(self, nome, email, telefone,):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.banco = Banco()

    def inserir_dados(self):
        try:
            dados = {
                'nome' : self.nome,
                'email' : self.email,
                'telefone' : self.telefone
            }
            self.banco.inserir('tb_clientes', dados)
            print("Cliente cadastrado com sucesso!")
        except Exception:
            print("Deu erro amigão, tem que ver isso ai")
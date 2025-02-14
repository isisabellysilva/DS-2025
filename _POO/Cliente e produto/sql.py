import sqlite3

class Banco:
    def conectar(self):
        self.conexao = sqlite3.connect("banco.db")
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()

    def inserir(self, tabela, dados: dict):    
        self.conectar()
        colunas = ", ".join(dados.keys())
        valores = ", ".join(['?'] * len(dados))
        lista = list(dados.values())

        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
        self.cursor.execute(sql, lista)
        self.conexao.commit()
        self.desconectar()
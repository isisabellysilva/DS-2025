class Conta:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito realizado com sucesso,seu saldo atual: {self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor 
            print(f"Saque realizado com sucesso, seu saldo atual: {self.saldo}")

            self.saldo_consulta()

    def imprimir_informações(self):
        print(f"Conta criada para {self.titular} - Número {self.numero_conta}")
    def consultar_saldo(self):
        print(f"Seu saldo atual: {self.saldo}")
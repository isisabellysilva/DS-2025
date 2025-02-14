import conta_bancaria

conta = conta_bancaria.Conta("Ana Souza","123456", 0)
conta.imprimir_informações()
conta.depositar(1000)
#conta.consultar_saldo()
conta.sacar(500)
#conta.consultar_saldo()
conta.sacar(100)
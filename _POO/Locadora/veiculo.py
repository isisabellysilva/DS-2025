class Veiculo:
    def __init__(self, modelo, marca, ano, preco_diaria, unidades_disponiveis):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco_diaria = preco_diaria
        self.unidades_disponiveis = unidades_disponiveis

    def detalhes(self):
        print("=== Dados do Veículo ===")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Preço da diária: R$ {self.preco_diaria:.2f}")
        print(f"Unidades disponíveis: {self.unidades_disponiveis}\n")

    def alugar(self, quantidade, cliente):
        if quantidade > self.unidades_disponiveis:
            print("Veículo indisponível para aluguel na quantidade solicitada.\n")
        else:
            self.unidades_disponiveis -= quantidade
            total = quantidade * self.preco_diaria
            print(f"{cliente.nome} alugou {quantidade} unidade(s) do {self.modelo} por R$ {total:.2f}.")
            self.detalhes()

    def devolver(self, quantidade):
        self.unidades_disponiveis += quantidade
        print(f"{quantidade} unidade(s) do {self.modelo} foram devolvidas.")
        self.detalhes()

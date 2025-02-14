class Doceria:

    def __init__(self, nome, sabor, preco, estoque):
        self.nome = nome
        self.sabor = sabor
        self.preco = preco
        self.estoque = estoque
        
    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Estoque insuficiente para a retirada, faça o abastecimento")
        else:
            self.estoque -= quantidade
            total = quantidade * self.preco
            print(f"Venda efetuada. Total: R$ {total:.2f}")

    def reabastecer(self, quantidade):
        self.estoque += quantidade
        print(f"Reabastecimento efetuado. Estoque atual: {self.estoque}")
    def detalhes(self):
        print(f"Doce: {self.nome} - Sabor: {self.sabor} - Preço: R$ {self.preco:.2f} - Estoque: {self.estoque}") 
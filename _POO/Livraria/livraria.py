class Livraria:
    def __init__(self, titulo, autor, valor, estoque):
        self.titulo = titulo
        self.autor = autor
        self.valor = valor
        self.estoque = estoque     
   
    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Estoque insuficiente para a venda")
        else:
            self.estoque -= quantidade
            total = quantidade * self.valor
            print(f"Venda efetuada. Total: R$ {total:.2f}")
    def reabastecer(self, quantidade):
        self.estoque += quantidade
        print(f"Reabastecimento efetuado. Estoque atual: {self.estoque}")
    def detalhes(self):
        
        print(f"Livro cadastrado: {self.titulo} - Autor:{self.autor} - Preço: R$ {self.valor:.2f} - Estoque: {self.estoque}")
class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        print(f"Carro criado: {self.marca} {self.modelo} ({self.ano})")
    
    def acelerar(self):
        self.velocidade += 10
        print(f"Velocidade aumentada para {self.velocidade} km/h")
    
    def frear(self):
        
        if self.velocidade < 10:
            self.velocidade = 0
        else:
            self.velocidade -= 10
        print(f"Velocidade reduzida para {self.velocidade} km/h")
    
    def exibir_info(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) - Velocidade atual: {self.velocidade} km/h")

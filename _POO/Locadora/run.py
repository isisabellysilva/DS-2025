from cliente import Cliente
from veiculo import Veiculo


cliente1 = Cliente(
    nome="João Silva",
    email="joao.silva@email.com",
    telefone="(11) 99999-9999",
    endereco="Rua das Palmeiras, 123"
)
cliente1.detalhes()


veiculo1 = Veiculo(
    modelo="HB20",
    marca="Hyundai",
    ano=2023,
    preco_diaria=120.00,
    unidades_disponiveis=3
)
veiculo1.detalhes()


print("Aluguel de 2 unidades:")
veiculo1.alugar(2, cliente1)


print("Devolução de 1 unidade:")
veiculo1.devolver(1)


print("Tentativa de alugar 3 unidades:")
veiculo1.alugar(3, cliente1)

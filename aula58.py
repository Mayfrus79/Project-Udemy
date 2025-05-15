# Metaclasse (define como as classes são criadas)
class MetaOficina(type):
    def __new__(cls, name, bases, dct):
        print(f"Criando a classe: {name}")
        return super().__new__(cls, name, bases, dct)

# Classe Carro (usando a metaclasse MetaOficina)
class Carro(metaclass=MetaOficina):
    def __init__(self, modelo):
        self.modelo = modelo

# Instância de Carro
meu_carro = Carro("Fusca")
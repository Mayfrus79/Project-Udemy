class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo privado
    
    @property
    def nome(self):  # Getter
        return self._nome

    @nome.setter
    def nome(self, nome):  # Setter
        if len(nome) < 3:
            raise ValueError("O nome precisa ter pelo menos 3 caracteres")
        self._nome = nome

# Usando a classe
p = Pessoa("Ana")
print(p.nome)  # Acessando o getter, vai imprimir 'Ana'

p.nome = "Lu"  # Tenta mudar o nome (vai levantar um erro)

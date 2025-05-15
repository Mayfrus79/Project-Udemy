from itertools import zip_longest

# Listas de cidades e estados (definidas antes)
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# Função para emparelhar as listas
def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))  # Limita a iteração ao tamanho da menor lista
    return [(l1[i], l2[i]) for i in range(intervalo)]

# Usando zip para emparelhar as duas listas (vai até o tamanho da menor lista)
print("Resultado com zip:")
for cidade, estado in zip(l1, l2):
    print(f"({cidade}, {estado})")

# Usando zip_longest para preencher com 'SEM CIDADE' se a lista l1 for menor
print("\nResultado com zip_longest:")
for cidade, estado in zip_longest(l1, l2, fillvalue='SEM CIDADE'):
    print(f"({cidade}, {estado})")

# Usando a função zipper (versão customizada)
print("\nResultado com a função 'zipper':")
for cidade, estado in zipper(l1, l2):
    print(f"({cidade}, {estado})")

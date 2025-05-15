from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total = reduce(
    lambda ac, p: ac + p['preco'],  # Função lambda simplificada
    produtos,
    0  # Valor inicial
)

print('Total é', total)

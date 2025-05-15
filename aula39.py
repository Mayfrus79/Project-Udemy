
def add_clients(name, client_list=None):
    if client_list is None:
        client_list = []  # Create a new list if 'client_list' is None
    client_list.append(name)
    return client_list


client1 = add_clients('luiz')
add_clients('Joana', client1)
add_clients('Fernando', client1)
client1.append('Edu')

client2 = add_clients('Helena')
add_clients('Maria', client2)

client3 = add_clients('Moreira')
add_clients('Vivi', client3)

print(client1)  # ['luiz', 'Joana', 'Fernando', 'Edu']
print(client2)  # ['Helena', 'Maria']
print(client3)  # ['Moreira', 'Vivi']

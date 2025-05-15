import os

lista = []
while True:
    print('Select an option')
    option = input('[I]nsert, [D]elete, [L]ist: ')

    if option == 'I':
        os.system("cls")
        value = input('Value: ')
        lista.append(value)
    elif option == "D":
        indice_str = input('Choose index to delete: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Please enter an integer!')
        except IndexError:
            print('Index does not exist in the list!')
        except Exception:
            print('Unknown error')
    
    elif option == 'L':
        os.system("cls")
        if len(lista) == 0:
            print('Nothing to list!')
    
        else:
            for i, valor in enumerate(lista):
                print(i, valor)
    else:
        print('Please choose I, A or L.')

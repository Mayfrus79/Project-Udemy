
numero = int(input('Digite o seu número: '))
while numero >= 0:
    print(numero, end=', ')
    if numero == 5:
        print('pular esse número')
    elif numero == 0:
        print('Chegou a 0')
    numero -= 1


for x in reversed(range(1, 11)):
    print(x, end=', ')
    if x == 3:
        print('Pular esse número!')
    elif x == 1:
        print('Terminou a contagem!')
    else:
        continue

        
    

    


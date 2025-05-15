couter = 0

while couter < 10:
    print(f'Counter: {couter}')
    couter += 1

    if couter == 5:
        print('Vou pular esse número')
        continue

print('Out of the Loop!')

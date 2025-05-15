while True:
    name = input('Enter your name: ')
    age = input('Enter your age: ')

    if name and age:
        nome_backwords = name[::-1]
        have_spaces = 'Yes' if " " in name else 'No'
        number_letters = len(name)
        firs_letter = name[0]
        last_letter = name[-1]

        print(f'Your name is {name}')
        print(f"Your backwords name is {nome_backwords}")
        print(f'Your name have spaces: {have_spaces}')
        print(f'your name have {number_letters} letters')
        print(f'The firs word of your name is: {firs_letter}')
        print(f'The last letter of your name is: {last_letter}')
    
    else:
        print('Sorry, you left empty spaces!')
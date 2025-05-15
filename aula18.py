
number_to_guess = 7

while True:
    guess = int(input("Guess the number between 1 and 10 (type 0 to quit):"))
    if guess == 0:
        print("GoodBye!")
        break

    if guess == number_to_guess:
        print("Congratulatios, You guess it!!!")
        break  
    
    print("Try again!")




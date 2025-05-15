# List of questions, each with its options and correct answer
questions = [
    {'Question': 'What is 2+2?', 'Options': ['1', '3', '4', '5'], 'Answer': '4',},
    {'Question': 'What is 5*5?', 'Options': ['25', '55', '10', '51'], 'Answer': '25',},
    {'Question': 'What is 10/2?', 'Options': ['4', '5', '2', '1'], 'Answer': '5',},
]

# Initializes the score counter
correct_answers = 0

# Loop through each question in the list of questions
for question in questions:
    # Display the question
    print('Question:', question['Question'])
    print()


    # Retrieve the options for the question
    options = question['Options']

    # Loop to display the numbered options
    for i, option in enumerate(options):
        # Display the numbered option
        print(f'{i})', option)
    print()

    # Prompt the user to choose an option
    choice = input('Choose an option: ')

    # Initialize the variable that will check if the user answered correctly
    correct = False
    # Variable to store the user's choice converted to an integer
    choice_int = None
    # Store the number of available options
    num_options = len(options)

    # Check if the user's input is a number
    if choice.isdigit():
        # Convert the input to an integer
        choice_int = int(choice)

    # Check if the user's choice is a valid number (within the range of options)
    if choice_int is not None:
        if choice_int >= 0 and choice_int < num_options:
            # Check if the user's answer matches the correct answer
            if options[choice_int] == question['Answer']:
                # If the answer is correct, mark it as correct
                correct = True

    # Display a blank line to separate the question from the answer
    print()
    if correct:
        # If the user answered correctly, increment the correct answers counter
        correct_answers += 1
        # Display the correct answer message
        print('Correct 👍')
    else:
        # If the user answered incorrectly, display the incorrect answer message
        print('Incorrect ❌')

    print()

# At the end, display the number of correct answers and the total number of questions
print('You got', correct_answers)
print('out of', len(questions), 'questions.')

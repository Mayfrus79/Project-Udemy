from datetime import datetime

# List of people with name and age
people = [
    {"name": "João", "age": 25},
    {"name": "Maria", "age": 30},
    {"name": "Pedro", "age": 20},
]

# Function that calculates the year of birth
def calculate_birth_year(age):
    current_year = datetime.now().year
    return current_year - age

# Using lambda with map to apply the birth year calculation function
result = map(lambda person: {**person, "birth_year": calculate_birth_year(person["age"])}, people)

# Converting the result to a list and printing
print(list(result), sep='\n', end='  ')

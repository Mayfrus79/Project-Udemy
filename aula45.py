
class Person: 
    current_year = 2025

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def birth_year(self):
        return Person.current_year - self.age
    
p1 = Person('John', 35, 'male')
p2 = Person('Helena', 12, 'female')

print(f'The current year is {Person.current_year}')
print(f'The birth year of John is {p1.birth_year()}')
print(f'The birth year of Helena is {p2.birth_year()}')

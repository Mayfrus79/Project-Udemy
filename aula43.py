class Person:
    # Class attribute
    species = "Human"
    
    def __init__(self, name):
        # Instance attribute
        self.name = name
    
    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name}."
    
    # Class method
    @classmethod
    def species_of_class(cls):
        return f"The species is {cls.species}."
    
    # Static method
    @staticmethod
    def static_method():
        return "This is a static method."

# Using the methods
p1 = Person("John")
print(p1.greet())  # Instance method
print(Person.species_of_class())  # Class method
print(Person.static_method())  # Static method

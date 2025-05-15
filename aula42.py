class Fruit:
    def __init__(self, name, type, color, origin):
        self.name = name
        self.type = type
        self.color = color
        self.origin = origin
    
    def display_info(self):
        return f"My fruit is a {self.name}, which is a {self.type}, of color {self.color}, from {self.origin}"

# Criando instâncias de frutas
apple = Fruit('Apple', 'Pome', 'Red', 'USA')
banana = Fruit('Banana', 'Berry', 'Yellow', 'Ecuador')

# Imprimindo as informações das frutas
print(apple.display_info())
print(banana.display_info())

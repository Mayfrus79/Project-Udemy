def my_repr(self):
    class_name = self.__class__.__name__
    attributes = self.__dict__
    return_repr = f'{class_name}({attributes})'
    return return_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

def my_fruit(method):
    def inner(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Apple' in result:
            return 'You chose a sweet fruit!'
        return result
    return inner

@add_repr
class Fruit:
    def __init__(self, name):
        self.name = name

@add_repr
class FruitBasket:
    def __init__(self, name):
        self.name = name

    @my_fruit
    def say_name(self):
        return f'The fruit is {self.name}'

apple = Fruit('Apple')
banana = Fruit('Banana')

orange = FruitBasket('Orange')
mango = FruitBasket('Mango')

print(apple)
print(banana)

print(orange)
print(mango)

print(orange.say_name())
print(mango.say_name())

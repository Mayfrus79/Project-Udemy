
def counters():
    yield 1
    yield 2
    yield 3

def generator_a():
    yield 1
    yield 2

def generator_b():
    yield 3
    yield 4

def full_generator():
    yield from generator_a()
    yield from generator_b()

def list_generators():
    yield from [10, 20, 30, 40, 50]

print('Exemple 1: counter generator')
for value in counters():
    print(value)
print("Example 2: Full generator with yield from")
for value in full_generator():
    print(value)
print("Example 3: List generator with yield from")
for number in list_generators():
    print(number)
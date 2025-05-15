def create_greeting(greeting):
    # Inner function that uses the greeting and name to create the message
    def greet(name):
        return f'{greeting}, {name}!'
    return greet  # Returns the inner function (closure)

# Create customized greeting functions
say_good_morning = create_greeting('Good morning')
say_good_night = create_greeting('Good night')

# Use the created functions to greet different people
for name in ['Maria', 'Joana', 'Luiz']:
    print(say_good_morning(name))  # Ex: "Good morning, Maria!"
    print(say_good_night(name))  # Ex: "Good night, Maria!"

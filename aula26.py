# Define a simple function that doubles a number
def double(x):
    return x * 2

# Use map to apply the `double` function to a list of numbers
numbers = [1, 2, 3, 4]
doubled_numbers = map(double, numbers)

# Convert the result to a list and print
print(list(doubled_numbers))

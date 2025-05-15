import json

# Defining a dictionary with fruit data
fruits = {
    'apple': {'color': 'red', 'price': 1.2},
    'banana': {'color': 'yellow', 'price': 0.5},
    'orange': {'color': 'orange', 'price': 0.8},
}

# Writing the fruit data to a JSON file
with open('fruits.json', 'w', encoding='utf8') as file:
    json.dump(fruits, file, ensure_ascii=False, indent=2)

# Reading the fruit data back from the JSON file
with open('fruits.json', 'r', encoding='utf8') as file:
    fruits = json.load(file)

    # Printing the color and price of the apple
    print(f"Apple color: {fruits['apple']['color']}")
    print(f"Apple price: ${fruits['apple']['price']}")

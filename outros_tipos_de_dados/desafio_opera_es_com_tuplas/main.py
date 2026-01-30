# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# TODO: Count apples and print
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

# TODO: Find first banana index and print
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

# TODO: Print apple stock status
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# TODO: Print grape stock status
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

# TODO: Print oranges index or out of stock message
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")
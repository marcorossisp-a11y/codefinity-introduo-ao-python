grocery_inventory = {"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99, 15)}

# se o preço das ovos for alto demais, aplica desconto
if grocery_inventory["Eggs"][1] > 5:
    # reduz o preço em 1
    old_price = grocery_inventory["Eggs"][1]
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],
        old_price - 1,
        grocery_inventory["Eggs"][2]
    )
    print("Eggs are too expensive, reducing the price by $1.")

# Add a new item "Tomatoes"
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30,)
print("Inventory after adding Tomatoes:", grocery_inventory)

# se o estoque de leite estiver baixo, reabastece
if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    # aumenta o estoque em 20
    category, price, stock = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, stock + 20)
print("Updated inventory:", grocery_inventory)

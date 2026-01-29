# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = discounted or lowStock
promotion = not movingProduct

# Print the result
print("Is the item eligible for promotion?", promotion)

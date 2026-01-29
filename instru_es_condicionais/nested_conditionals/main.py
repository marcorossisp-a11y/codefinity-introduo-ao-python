product_type = "Perishable"
days_in_stock = 1
stock_quantity = 3

# Write a nested if-else statement below 
if product_type == "Perishable":
    if days_in_stock > 7:
        print("perishable and very old - apply 70% discount")
    elif stock_quantity < 3:
        print("perishable and low stock - restock immediately")
    else:
        print("perishable and fresh - full price")
else:
    if stock_quantity == 0:
        print("non-perishable and out of stock - reorder now")
    else:
        print("non-perishable and stock is sufficient")

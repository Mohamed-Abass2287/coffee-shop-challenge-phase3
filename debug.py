from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
gedi = Customer("gedi")
gabriel = Customer("gabriel")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create Orders
order1 = Order(gedi, latte, 3.5)
order2 = Order(gedi, espresso, 2.75)
order3 = Order(gabriel, latte, 4.0)

# Print out data to verify correctness
print("=== Customers ===")
print(gedi.name)  
print(gabriel.name)    

print("\n=== Coffees ===")
print(latte.name)      
print(espresso.name)  

print("\n=== Orders ===")
print(f"Order1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")
print(f"Order2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")
print(f"Order3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")



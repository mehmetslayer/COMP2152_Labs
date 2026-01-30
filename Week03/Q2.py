#Q2 create a shopping cart program

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

apple_count = cart.count("apple")

print(f"Number of apples: {apple_count}")

milk_index = cart.index("milk")

print(f"Position of milk is: {milk_index}")

cart.remove("apple") #using remove

removed_item = cart.pop()

print(f"Apple succesfully removed. New shopping cart is {cart}")

print("Is banana in cart?", "banana" in cart)





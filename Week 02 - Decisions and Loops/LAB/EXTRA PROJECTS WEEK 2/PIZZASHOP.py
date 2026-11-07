print("Welcome to the Pizza Shop!")
size = input("What size pizza do you want? (small, medium, large) ")

if size == "small":
    price = 8
elif size == "medium":
    price = 12
elif size == "large":
    price = 16

type_of_pizza = input("What type of pizza do you want? (pepperoni,mushroom,corn) ")
if type_of_pizza == "pepperoni":
    price += 2
elif type_of_pizza == "mushroom":
    price += 1
elif type_of_pizza == "corn":
    price += 1.5    


print(f"The price of your {size} pizza is ${price:}.")
my_pizzas = ['margerita','chicken','duck']
friend_pizzas = my_pizzas[:]
my_pizzas.append('pineapple')
friend_pizzas.append('pepperoni')
print("My favourite pizzas are:")
for pizza in my_pizzas[:]:
 print(f"- {pizza.title()} pizza")
print(f"\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas[:]:
 print(f"- {pizza.title()} pizza")  
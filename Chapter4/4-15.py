#1: Using 4 Spaces instead of tabs:
buffet = ('sushi','eggs','cabbage','toast','cereal')
for food in buffet:
    print(food.title())

buffet = ('sushi','eggs','cabbage','cucumber','pasta')
print(f"\n")
for food in buffet:
    print(f"{food.title()}")

#2: Using less than 80 characters:
my_pizzas = ['margerita','chicken','duck','pineapple']
print("My favourite pizzas are:")
for pizza in my_pizzas[:]:
 print(f"- {pizza.title()} pizza")

#3: Not using blank lines excessively:
random_items = ['table','chair','laptop','apple','orange','bowl','charger','mat','pencil','pen']

print(len (random_items))
print("The first three items in the list are:")
print(random_items[:3])
print("Three items from the middle of the list are:")
print(random_items[4:6])
print("The last three items in the list are:")
print(random_items[-3:])
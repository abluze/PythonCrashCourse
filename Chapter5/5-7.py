favourite_fruits = ['strawberries', 'blueberries', 'melon']

print('strawberry' in favourite_fruits)
for fruit in favourite_fruits:
  if fruit == 'strawberries' or 'blueberries' or 'melon':
    print(f"You really like {fruit}.")
  else:
    print("This fruit is not your favourite.")

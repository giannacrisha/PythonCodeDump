pizzas = ['hawaiian', 'margherita', 'veggie']

for pizza in pizzas:
	print("I love " + pizza.title() + " Pizzas!")

print('Bro, I really loved pizza back then.\n')

friend_pizzas = pizzas[:]
pizzas.append('mushroom')
friend_pizzas.append('all-meat')

print('My favorite pizzas are: ' + str(pizzas))
print("My friend's favorite pizzas are " + str(friend_pizzas))

for pizza in pizzas:
	print(pizza)

for pizza in friend_pizzas:
	print(pizza)
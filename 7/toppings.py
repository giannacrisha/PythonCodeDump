active = True
while active:
    topping = input("Insert a topping to put on your pizza: \nType 'quit' when you are finished. ")

    if topping == 'quit':
        active = False
    else:
        print('Adding ' + topping + ' on your pizza.')
        continue

print("Thank you for ordering at Gianna's Pizzeria!")


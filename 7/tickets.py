print('\nMovie Ticket Price Calculator\n')
print("Type 'quit' when you're done.\n")

active = True
while active:
    age = input('Enter your age to begin: ')
    
    if age == 'quit':
        break

    if int(age) < 3:
        print('The ticket is free.\n')
    elif int(age) < 12:
        print('The ticket is $10.\n')
    elif int(age) > 12:
        print('The ticket is $15.\n')

print('Thank you for using our Movie Ticket Price Calculator!')

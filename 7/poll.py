print('\n--- DREAM VACATION POLL ---\n')

print("Type 'quit' when you're done.\n ")

database = {}
poll_active = True
while poll_active:
    name = input('What is your name? ')
    dream_vacation = input('Where do you want to go for your dream vacation? ')
    
    database[name] = dream_vacation

    response = input('Will you let someone answer this poll? ')
    if response.lower() == 'yes':
        continue
    elif response.lower() == 'no':
        poll_active = False
    else:
        print('You entered an invalid response. Please try again!')

print('\nThank you for answering our poll! Here are the results: ')

for name, dream_vacation in database.items():
    print('\t' + name.title() + ' wants to go to ' + dream_vacation.title() + '.')

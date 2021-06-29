print('\n--- SANDWICH ORDERS ---\n')
sandwich_orders = ['pastrami', 'ham and cheese', 'pastrami', 
'tuna', 'nutella', 'peanut butter and jelly', 'pastrami']
finished_sandwiches = []

print('\nUnfortunately, we have run out of pastrami. Sorry for the inconvenience.\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('These are the current sandwich orders:')
for sandwich in sandwich_orders:
    print('\t' +sandwich.title())

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('\nMaking ' + current_sandwich + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

print("\nHere are all the finished sandwiches: ")

for sandwich in finished_sandwiches:
    print('\t' + sandwich.title())
print('\n---TSHIRT MAKER---\n')

def make_shirt(size, text):
    """Prints the size and text of the tshirt"""
    print('\nThe size of the tshirt is ' + size + '.')
    print('The text inside the tshirt is ' + text + '.')

size = input('What size do you want the tshirt to be? ')
text = input('What text do you want to put in the tshirt? ')

make_shirt(size, text)

print('\nThank you for ordering a tshirt!\n')
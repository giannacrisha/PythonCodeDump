magicians = ['gianna', 'rick', 'lucas', 'girby']
greatmagicians =[]

def show_magicians(magicians):
    """ Displays the magicians in a list"""
    print('\nMagicians: ')
    for magician in magicians:
        print('\t' + magician.title())

def make_great(magicians):
    """ Adds 'The Great' in front of every magicians name """
    while magicians:
        notgreat = magicians.pop()
        great = 'The Great ' + notgreat.title()
        greatmagicians.append(great)


make_great(magicians[:])
show_magicians(greatmagicians)
show_magicians(magicians)




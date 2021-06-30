print('\n--- CITY AND COUNTRY RETURNER ---\n')
print("Enter 'q' to quit.\n")

def city_country(city, country):
    """ Returns the city and the country """
    return city.title() + ', ' + country.title() + '\n'

while True:
    city = input('Enter a city: ')
    if city == 'q':
        break
    country = input('Enter a country: ')
    if country == 'q':
        break
    print(city_country(city, country))

    

print('\nThank you for using this program!')



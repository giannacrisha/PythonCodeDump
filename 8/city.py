print('\n--- CITY AND COUNTRY ---\n')
def describe_city(city, country='Philippines'):
    """Displays a city and its respective country"""
    print(city.title() + ' is in ' + country.title() + '.\n')

city = input( 'Insert a city: ')
country = input ( 'Insert a country: ')

describe_city(city)

city = input( 'Insert a city: ')
country = input ( 'Insert a country: ')

describe_city(city, country)

city = input( 'Insert a city: ')
country = input ( 'Insert a country: ')

describe_city(city)
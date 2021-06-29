person1 = {
	'first_name' : 'Gianna',
	'last_name' : 'Saludo',
	'age' : 17,
	'city' : 'Butuan'
}

person2 = {
	'first_name' : 'Girby',
	'last_name' : 'Saludo',
	'age' : 15,
	'city' : 'Butuan'
}

person3 = {
	'first_name' : 'Cristina',
	'last_name' : 'Saludo',
	'age' : 46,
	'city' : 'Butuan'
}

person4 = {
	'first_name' : 'Gimelito',
	'last_name' : 'Saludo',
	'age' : 48,
	'city' : 'Butuan'
}


people = [person1, person2, person3, person4]

for person in people:
	print(str(person['first_name']) + ' ' + str(person['last_name']) + ', ' +
		str(person['age']) + ' years old, is living in ' + str(person['city'] +
		' City.'))

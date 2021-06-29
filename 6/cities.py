cities = {
	'manila':['philippines', 'tagalog'],
	'butuan': ['philippines', 'bisaya'],
	'abu dhabi':['united arab emirates', 'arabic'],
}

for city, info in cities.items():
	print('City: ' + str(city.title()))
	print('Country: ' + str(info[0].title()))
	print('Local Language: ' + str(info[1].title()) + '\n')
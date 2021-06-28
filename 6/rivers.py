rivers = {
	'nile': 'egypt',
	'yangtze': 'china',
	'mississippi': 'usa',
}

for river, country in rivers.items():
	if country == 'usa':
		print("The " + river.title() + " river runs through " + country.upper() +".")
	else:
		print("The " + river.title() + " river runs through " + country.title() +".")
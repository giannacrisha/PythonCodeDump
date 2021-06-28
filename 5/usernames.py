current_users = ['queengianna', 'giannacrisha', 'giannaphrodite',
'queenofgamers', 'giannasaludo']

new_users = ['girbypogi', 'GIANNACRISHA', 'princegirby',
'queenofgamers', 'ninjagirby']

for new_user in new_users:
	if new_user.lower() in current_users:
		print('Please enter another username.')
	else:
		print('The username is available.')
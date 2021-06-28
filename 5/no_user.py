usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hello Admin! Would you like a status report?")
		else:
			print("Hello " + username + "!")
else:
	print('We need to find more users!')
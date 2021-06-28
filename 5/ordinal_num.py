numbers = [num*1 for num in range(1,10)]

for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")
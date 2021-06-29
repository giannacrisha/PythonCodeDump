number = input("Please give me a number and I'll tell you if it's a multiple of 10: ")

remainder = int(number) % 10

if remainder == 0:
	print('That is a multiple of ten!')
else:
	print('That is NOT a multiple of ten.')
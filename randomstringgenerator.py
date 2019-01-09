import random
import time
characters = []
lent = 0
yn = ['y', 'n']
currper = 0

def generate(lent, characters):
	prevper = 0
	i = 0
	output = ''
	while i < int(lent):
		num = random.randint(0, len(characters) - 1)
		output = output + characters[num]
		i = i + 1
		currper = round(int(i) /  int(lent) * 100)
		if prevper != currper:
			print('=' * round(currper / 10), end = '')
			print(' ' * (10 - round(currper / 10)), end = '')
			print(currper, end = '')
			print('%')
			prevper = currper
	return output

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


print('Welcome to Random String Generator v.1.0')
print('by M1ch4ll064')
goAgain = True
while goAgain:
	print('Select number of characters:')
	howlong = input()
	generate_start = time.time()
	generated = generate(howlong, chars)
	generate_done = time.time()
	generate_time = generate_done - generate_start
	print(generated)
	print('Done! ' + howlong + ' characters in ')
	print(generate_time)
	
	choice = None
	while not choice in yn:
		print('Would you like to print again? [y/n]')
		choice = input()
	if choice == 'y':
		print("\n" * 10)
		print(generated)
		dabljudabljudablju = input()

	choice = None
	while not choice in yn:
		print('Would you like to generate again? [y/n]')
		choice = input()
	if choice == 'y':
		goAgain = True
	else:
		if choice == 'n':
			goAgain = False
print('Goodbye!')
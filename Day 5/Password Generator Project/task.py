import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

letters_length = len(letters)
symbols_length = len(symbols)
numbers_length = len(numbers)

for i in range(nr_letters):
    password_list.append(letters[random.randint(0, letters_length-1)])
for i in range(nr_symbols):
    password_list.append(symbols[random.randint(0, symbols_length-1)])
for i in range(nr_numbers):
    password_list.append(numbers[random.randint(0, numbers_length-1)])

print(password_list)

shuffled_list = password_list.copy()
random.shuffle(shuffled_list)
print(shuffled_list)

password = ""
for letter in shuffled_list:
    password += letter

print(f"Your password is: {password}")
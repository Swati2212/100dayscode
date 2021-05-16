import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypython generator!")
user_letters= int(input("How many letter do you want to choose in your password? "))
user_numbers = int(input("How many letter do you want in your password? "))
user_symbols = int(input("How many symbols you want in your password? "))

password_list = []

#for letter
for i in range(user_letters):
    random_char = random.choice(letters)
    password_list.append(random_char)

#for numbers
for num in range(user_numbers):
    random_num = random.choice(numbers)
    password_list.append(random_num)

#for symbols
for symbol in range(user_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

random.shuffle(password_list)

password = ''
for char in password_list:
    password = password+char
print("Your generated password is:", password)

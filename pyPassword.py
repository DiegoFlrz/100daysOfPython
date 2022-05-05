#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number
password = ""
for letter in range(1, nr_letters + 1): #since the password needs atleast 1 letter we set a range starting at 1 and ending at whatever number was inputed, +1 since range is non-inclusive of 'b'
    random_char = random.choice(letters) #pulls a random choice from the letters up to the range from the input and saves it in a variable.
    password += random_char #concatinates the random_char's pulled from the list into the password variable.

for symbol in range(1, nr_symbols + 1):
    random_symb = random.choice(symbols)
    password += random_symb

for number in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

password_random = random.choice(password)
print(f"Your randomly generated passwor is: {password_random}")


#hardmode, randomizes where the letters, char, symbols go. sec5 vid 56 for explanation.
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password += ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
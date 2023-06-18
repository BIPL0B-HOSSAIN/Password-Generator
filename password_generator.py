#Password Generator Project
#Owner : Biplob Hossain
#Follow me on github: https://github.com/BIPL0B-HOSSAIN
import random, os
os.system("clear")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for letter in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)



password = ""
for pwd in password_list:
  password += pwd
  
print(f"Your Password is:  {password}")
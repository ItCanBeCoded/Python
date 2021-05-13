import random
import numpy as np

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
user_letters= int(input("How many letters would you like in your password?\n")) 
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

password = ''
HardPassword = ''
HardestPassword = ''
i = 0
j = 0
k = 0
while i < user_letters:
    password += random.choice(letters)
    i+=1
while j < user_symbols:
    password += random.choice(numbers)
    j+=1
while k < user_numbers:
    password += random.choice(symbols)
    k+=1
random.sample(password, len(password))
HardPassword = sorted(password, key=lambda k: random.random())
for hard in HardPassword:
    HardestPassword += hard
print(f"Your password is {HardestPassword}")

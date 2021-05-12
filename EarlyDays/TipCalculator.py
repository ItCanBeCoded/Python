#f strings allow you to add curly brace code into strings
# num_char = len(input("what is your sign?"))
# new_num_char = str(num_char)

# print(type(f"Your sign has {new_num_char} characters."))

# Data Types

# print("This program will add 2 numbers")
# num1 = int(input("Enter your first Number "))
# num2 = int(input("Enter your second Number "))
# print(num1+num2)

#exponents this is 2 to the 4th power, same as pow(2, 4)
# print(2 ** 4)

#Tip Calculator

print("Welcome to the Tip Calculator")
total = input("What was the total bill? ")
percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people will split the bill? ")

pricePerCapita = ((int(total) + (int(total)*(int(percent)/100)))/int(people) )
print(f"Each person should pay {round(pricePerCapita, 2)}")
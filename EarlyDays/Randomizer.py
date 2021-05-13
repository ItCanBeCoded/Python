# import random

# random.seed(1)

# rando = random.randint(5, 500)

# print(rando)

student_heights = [180, 124, 165, 173, 189, 169, 146]
average = 0
for height in student_heights:
    average += height
    total_average = average/len(student_heights)

print(round(total_average, 2))

total = 0
for number in range(1, 101):
    total += number
print (total)

#fizzbuzz problem

for number in range(1, 101):
    if number% 3 == 0 and number% 5 == 0:
        print("fizzbuzz")
    elif number% 3 == 0:
        print("fizz")
    elif number% 5 == 0:
        print("buzz")
    else:
        print(number)


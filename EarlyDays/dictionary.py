#using a dictionary for a secret auction program

#example
programming_dictionary = {
    "Bug": "An error in the code",
    "Function": "A piece of code you can call endlessly",
    }

programming_dictionary["loop"] = "action of doing something over again"

# print(programming_dictionary)

#creating an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

for key in programming_dictionary:
    print(key)

#nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": "chillest country, wine n baguettes"
}
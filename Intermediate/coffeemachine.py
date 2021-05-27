quarters = 12
dimes = 15
nickles = 20
pennies = 50


def choice_espresso():
    print("Your espresso will cost $3.00, please insert your coins: ")
    return


def choice_latte():
    return


def choice_cappuccino():
    return


def report_runner():
    return

def main():
    drink_choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if drink_choice == "espresso":
        choice_espresso()
    elif drink_choice == "latte":
        choice_latte()
    elif drink_choice == "cappuccino":
        choice_cappuccino()
    elif drink_choice == "report":
        report_runner()
    else: main()



main()




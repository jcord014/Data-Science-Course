# DSC 510
# Week 4
# Programming Assignment Week 4
# Auther: Joaquin Cordero
# 4/4/2024
# Fiber optic installation cost calculator

# Change Control Log:
# Change#2
# Change(s) Made: Updated code to add functions
# Date of change: 4/4/2024
# Author: Joaquin Cordero
# ----------------------------------------------

def greeting():
    message = "Welcome! To calculate fiber optic cable installation cost, enter below."
    print()
    print(message)
    print()


def get_company():
    user_company = input("Please enter your company name: ")
    '''This function retrieves the company name from the user'''
    return user_company


def get_cable():
    cable_length = float(input("Please enter fiber optic cable length in ft to be installed: ")
                         .replace(',', ''))
    '''This function retrieves the desired cable length from the user'''
    return cable_length


def calculate(feet, cost):
    calculated_cost = feet * cost
    '''This function calculates the cost per cable length'''
    return calculated_cost


def main():
    greeting()
    company_name = get_company()
    cable_length = get_cable()

    if cable_length > 500:
        price = 0.50
    elif cable_length > 250:
        price = 0.70
    elif cable_length > 100:
        price = 0.80
    else:
        price = 0.87

    total_cost = calculate(cable_length, price)

    print("---------------------------")
    print("Copy of Receipt")
    print("Company: " + company_name)
    print("Fiber length to be installed: " + str(f'{cable_length:,.2f}') + "ft")
    print("Total cost: $" + str(f'{total_cost:,.2f}'))
    print("---------------------------")


if __name__ == "__main__":
    main()
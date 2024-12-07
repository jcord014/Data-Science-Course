# DSC 510
# Week 2
# Programming Assignment Week 2
# Auther: Joaquin Cordero
# 3/22/2024
# ----------------------------------------------

greeting_message = "Welcome! To calculate fiber optic cable installation cost, enter below."
print()
print(greeting_message)
print()

company_name = input("Please enter your company name: ")

cable_feet = float(input("Please enter fiber optic cable length in ft to be installed: ")
                   .replace(',', ''))

total_cost = cable_feet * 0.87  # $0.87 cost per feet of cable

print("---------------------------")
print("Copy of Receipt")
print("Company: " + company_name)
print("Fiber length to be installed: " + str(f'{cable_feet:,.2f}') + "ft")
print("Total cost: $" + str(f'{total_cost:,.2f}'))
print("---------------------------")
# DSC 510
# Week 3
# Programming Assignment Week 3
# Auther: Joaquin Cordero
# 3/25/2024
# Fiber optic installation cost calculator

# Change Control Log:
# Change#1
# Change(s) Made: Added bulk discount calculator lines 26-31 added
# Date of change: 3/25/2024
# Author: Joaquin Cordero
# ----------------------------------------------

greeting_message = "Welcome! To calculate fiber optic cable installation cost, enter below."
print()
print(greeting_message)
print()

company_name = input("Please enter your company name: ")

cable_feet = float(input("Please enter fiber optic cable length in ft to be installed: ")
                   .replace(',', ''))

total_cost = cable_feet * 0.87  # $0.87 cost per feet of cable
if cable_feet > 100:
    total_cost = cable_feet * 0.80
if cable_feet > 250:
    total_cost = cable_feet * 0.70
if cable_feet > 500:
    total_cost = cable_feet * 0.50

print("---------------------------")
print("Copy of Receipt")
print("Company: " + company_name)
print("Fiber length to be installed: " + str(f'{cable_feet:,.2f}') + "ft")
print("Total cost: $" + str(f'{total_cost:,.2f}'))
print("---------------------------")
# DSC 510
# Week 5
# Programming Assignment Week 5
# Auther: Joaquin Cordero
# 4/10/2024
# program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user
# -----------------------------------------------

def performCalculation(sign):
    num1 = float(input("Please enter first number: ").replace(',', ''))
    num2 = float(input("Please enter second number: ").replace(',', ''))

    if sign == "+":
        print(str(f'{num1 + num2:,.2f}'))
    elif sign == "-":
        print(str(f'{num1 - num2:,.2f}'))
    elif sign == "*":
        print(str(f'{num1 * num2:,.2f}'))
    elif sign == "/":
        if num2 == 0:
            print("undefined")
        else:
            print(str(f'{num1 / num2:,.2f}'))
    else:
        input("Please enter a valid operator: ")
        return sign


def calculateAverage():
    user_num = input("How many numbers would you like to enter? To start over enter 'x': ")
    user_list = []
    count = 1
    total = 0

    if user_num == "x":
        return main()
    else:
        for n in range(int(user_num)):
            new_count = count
            user_list.append(float(input("Enter number " + str(new_count) + ": ")))
            count += 1
        for u in user_list:
            total += u

        user_input_average = total / int(user_num)
        print("Average of numbers entered is: " + str(f'{user_input_average:,.2f}'))
        calculateAverage()


def main():
    desired_calculation = input("Which calculation would you like to perform? \nEnter 'operation' to perform "
                                "calculation using (+,-,*,/) or 'average' to find the average.('x' to stop): ")
    calculation = 0

    while calculation == 0:
        if desired_calculation == "operation":
            sign = input("Please enter an operator (+,-,*,/) to calculate or enter 'x' to select another calculation: ")

            if sign == "x":
                return main()
            else:
                performCalculation(sign)
        elif desired_calculation == "average":
            user_answer = input("If you would like to find the average enter 'y', to go back enter 'x': ")
            if user_answer == "y":
                calculateAverage()
            elif user_answer == "x":
                return desired_calculation
            else:
                return main()
        elif desired_calculation == "x":
            break
        else:
            desired_calculation = input("Enter 'x' to stop. To continue enter 'operation' or 'average': ")


if __name__ == '__main__':
    main()
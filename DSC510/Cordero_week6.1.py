# DSC 510
# Week 6
# Programming Assignment Week 6
# Auther: Joaquin Cordero
# 4/20/2024
# This program will determine the largest and smallest temperature from user input
# ---------------------------------------------------

def main():
    print("Hello, this program will help you determine the largest and smallest temperature!\n")
    temperatures = []
    user_temps = input("Please enter a series of temperature or enter 'Q' to quit: ").split()
    temperatures = user_temps

    if temperatures[0] == "Q":
        print("Please enter a series of temperature first.")

    if temperatures[0] != "Q":
        while True:
            temperatures = []
            temperatures = user_temps
            largest = temperatures[0]
            smallest = temperatures[0]

            if temperatures[0] == "Q":
                print("Thank you!")
                break

            if temperatures[0] != "Q":
                for user_temps in range(len(temperatures)):
                    if temperatures[user_temps] > largest:
                        largest = temperatures[user_temps]
                    if temperatures[user_temps] < smallest:
                        smallest = temperatures[user_temps]

            print("You entered", len(temperatures), "temperatures.")
            print("The largest temperature is:", largest)
            print("The smallest temperature is:", smallest)
            print()
            user_temps = input("Please enter a series of temperature or enter 'Q' to quit: ").split()
            continue


if __name__ == "__main__":
    main()
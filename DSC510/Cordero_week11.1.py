# DSC 510
# Week 11
# Programming Assignment Week 11
# Auther: Joaquin Cordero
# 5/20/2024
# This program will take the user's entered price and add the total price and total count of the items in the cart
# ---------------------------------------------------
import locale


class CashRegister:
    def __init__(self):
        self.item_count = 0
        self.total_price = 0.0

    def addItem(self, price):
        self.total_price += price
        self.item_count += 1

    def getTotal(self):
        return self.total_price

    def getCount(self):
        return self.item_count


def main():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    welcome_message = ("Welcome to the Cash Register Program! You'll be able to enter the price and the "
                       "program will calculate the total and keep track of the quantity of items.")
    print(welcome_message)
    register = CashRegister()

    while True:
        try:
            price_input = input("Enter the price of the item or type 'c' to calculate/exit: ").lower()
            if price_input == 'c':
                break
            price = float(price_input)
        except ValueError:
            print("Please enter a valid price or 'c' to calculate/exit.")
            continue

        register.addItem(price)

    print("\nNumber of items in cart:", register.getCount())
    print("Total amount of cart:", locale.currency(register.getTotal()))


if __name__ == "__main__":
    main()
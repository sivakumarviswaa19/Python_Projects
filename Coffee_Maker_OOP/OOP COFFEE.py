from Data import CoffeeMaker
from mone import MoneyMachine
from class1 import Menu
from menuitem import MenuItem

money=MoneyMachine()
menu=Menu()
coffee=CoffeeMaker()

is_on=True
while is_on:
    option=menu.get_items()
    drink=input(f"Enter your choice from {option}")
    if drink=="off":
        is_on=False
    elif drink=="report":
        coffee.report()
        money.report()
    else:
        drink=menu.find_drink(drink)
        if coffee.is_resource_sufficient(drink):

            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
                print(f"Enjoy you {drink}")
                is_on=True







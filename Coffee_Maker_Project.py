MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit=0


def is_sufficent(req):
    cond=True
    for item in req:
        if req[item]>resources[item]:
            print("Sorry not possible")
            cond = False
    return cond

def success(money_recieved,dcost):
    if money_recieved>=dcost:
        change=round(money_recieved-dcost,2)
        print(f"The change is :{change}")
        global profit
        profit+=dcost
        return True
    else:
        print("Sorry not enough money, Refunded")
        return False

def money():
    print("Enter the coins here:")
    total=int(input("Enter number of quarters:"))*0.25
    total += int(input("Enter number of nickels:")) * 0.05
    total += int(input("Enter number of dimes:")) * 0.1
    total += int(input("Enter number of pennies:")) * 0.01
    return total





def make_coffee(dname,req):
    for item in req["ingredients"]:
        resources[item] -= req["ingredients"][item]

    print(f"Here is your {dname}")








def main():
    option=input("Enter which drink you prefer(espresso/latte/cappuccino):")


    if option=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}ml")
        print(f"Profit:{profit}")


    else:
        drink=MENU[option]
        is_sufficent(drink["ingredients"])
        if is_sufficent(drink["ingredients"]):
            pay=money()
            if success(pay,drink["cost"]):
                make_coffee(option,drink)
main()










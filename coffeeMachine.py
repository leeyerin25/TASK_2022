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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(order): #order 에 재료 리스트가 들어갈거임
    for item in order:
        if resources[item] < order[item]:
            print(f"sorry. don't enough {item} . ")
            return False
        else:
            return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total



def is_transaction_successful(received, cost):
    if received >= cost :
        change = round(received-cost, 2)
        print(f"here ${change}.")
        global profit
        profit += cost
        return True
    else:
        print("sorry")
        return False #리턴은 꼭 마지막에.


def make_coffee(drink_name, order_ingredients):
    """ 차감 단계"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}.")


is_on=True

while is_on: #무한반복
    answer = input("What would you like? (espresso / latte / cappuccino: ")
    if answer == "off":   #첫번째 실수
        is_on = False
    elif answer == "report":
        print(f"water: {resources['water']}")   #f스트링과 딕셔너리 함께 쓰는법 **
        print(f"milk: {resources['milk']} ")
        print(f"coffee: {resources['coffee']} ")
        print(f"money : {profit}")
        is_on: True
    else:
        drink = MENU[answer]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(answer, drink["ingredients"])





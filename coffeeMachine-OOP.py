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





                
 -----------------------------------
#OOP 만드는법



from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#TODO 1 먼저 클래스를 객체로 정의해주기. 정의할때 함수끝에 () 꼭 붙히기

my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

menu = Menu()
# menu_item = MenuItem() 정의가 안됨 -> 속성이라 정의할필요없고. menu.find_drink(order_name) 에서 가져와줌

#TODO 2 WHILE 문의 장치 설정
is_on = True

while is_on:
    choice = menu.get_items()
    # TODO 3 get_items() 의 출력문을 이용해서 input으로 받고, 또 다른 객체로 저장
    drink = input(f"What would you like? {choice}:")
    if drink == "off":
        is_on: False
    elif drink == "report":
        coffee_maker.report()
        my_money_machine.report()
    #TODO 4 각각의 함수가 TRUE 라는 가정아래 쭉 함수를 작성.
    else:
        drink = menu.find_drink(drink) #find_drink를 써야 MenuItem 의 3가지 속성을 다 이용할수있음
        if coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost) : #속성은 객체.속성  / print 필요x
                coffee_maker.make_coffee(drink)            
                
                
                

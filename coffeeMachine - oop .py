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
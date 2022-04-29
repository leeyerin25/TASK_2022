# # import another_module
# #
# # print(another_module.another_variable)
#
#
# from turtle import Turtle, Screen #screen 보여주는 함수?
#
# timmy = Turtle()
# print(timmy)
#
# timmy.shape("turtle")  #모양바꿔줌   객체.속성(메쏘드,함수)
# timmy.color("cyan")     #컬러바꿔줌
# timmy.forward(100)  #100칸 진전ba
#
# my_screen = Screen()    #페이지부분
# print(my_screen.canvheight)
# my_screen.exitonclick() #함수명 : exitonclick -> 페이지 클릭하면 끝나게해 줌


#속성과 메소드 활용하는법 * pypi 라는 사이트를 이용하면 파이썬프로그래밍 사이트 찾을수있음
#prettytable : 표짜는 함수를 이용해 클래스와 객체를 만들어 볼것.

from prettytable import PrettyTable #from 큰 명칭 import 클래스
table = PrettyTable() #PrettyTable 이라는 클래스를 이용하여 table 이란 객체를 만듬 / 파스칼표기법

table.add_column("pokemon", ["picachu","squirtle","charmander"])   #속성명, 데이터 리스트
table.add_column("type", ["electric", "water", "fire"]) #위랑 연결딤


#체인지 속성
table.align = "r"  #변수 쓸때 뜨는게 궁금함
print(table)    #위에같이 속성넣고 다시 프린트하기

#table.align = "l" #하면서 바꿀수있음 속성

#블루프린트 = 클래스를 의미 (대문자표기) / 함수는 무조건 () 로 호출 ex)car.brake()
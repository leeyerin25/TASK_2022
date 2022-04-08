import another_module

print(another_module.another_variable)


from turtle import Turtle, Screen #screen 보여주는 함수?

timmy = Turtle()
print(timmy)
timmy.shape("turtle")  #모양바꿔줌
timmy.color("cyan")     #컬러바꿔줌
timmy.forward(100)  #100칸 진전ba

my_screen = Screen()    #페이지부분
print(my_screen.canvheight)
my_screen.exitonclick() #클릭하면 끝남


from prettytable import PrettyTable #from import뭔차이?? 대소문자 뭔차이??
table = PrettyTable()

table.add_column("pokemon",["picachu","squirtle","charmander"])   #아래로 리스트 생기게해줌!!
table.add_column("type", ["electric", "water", "fire"])


체인지 속성
print(table.align)  #변수 쓸때 뜨는게 궁금함
print(table)    #위에같이 속성넣고 다시 프린트하기

table.align = "l" #하면서 바꿀수있음 속성

#블루프린트 = 클래스를 의미 ??
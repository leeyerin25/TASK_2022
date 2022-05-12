import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(side):
    for _ in range(side):
        angle = 360/side
        tim.forward(100)
        tim.right(angle)

for give_side in range (3,11) :
    tim.color(random.choice(colors))
    draw_shape(give_side)
#

# 무작위 구현하기
angle = [0, 90, 180, 270]
for _ in range(200) :
    tim.pensize(15)
    tim.speed("fastest")
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(angle))


#TODO 컬러모드 함수

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)  #튜플은 한번정의후 수정x . 수정원하면 리스트로변경해야함!
    return random_color  #튜플을 반환 (r,g,b)중 하나의값 반환해줌

angle = [0, 90, 180, 270]

for _ in range(200):
    tim.pensize(15)
    tim.speed("fastest")
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(angle))



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.speed("fastest")
tim.pensize(15)

#스피로그래피가 처음으로 오면 멈추기
is_on = True
while is_on :
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()  #current_heading 정의한 이유는 float로 바꿔서 +10 하려고.
    tim.setheading(current_heading + 10)
    if tim.heading() == 0.0 :
        is_on = False
    else :
        continue

#각도 지정해서 그려보기
def draw(gap):
    for _ in range( int(360 / gap)) : #나누기는 float가 되서 int로 바꿔야함
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()  #current_heading 정의한 이유는 float로 바꿔서 +10 하려고.
        tim.setheading(current_heading + gap)
draw(5)

screen = t.Screen()

 ---- 컴프입 과제 ----


import turtle
screen = turtle.Screen()
# #1번문제

screen.setup(600,600)

def draw_sqpolygon(pen, x, y, radius, size=1, side=None, pen_color='black', fill_color=None):
    pen.pensize(size)
    pen.pencolor(pen_color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if not fill_color:
        pen.circle(radius, steps=side)
    else:
        pen.fillcolor(fill_color)
        pen.begin_fill()
        pen.circle(radius, steps=side)
        pen.end_fill()


if __name__=='__main__':
    mypen = turtle.Turtle()
    mypen.home()
    mypen.pensize(1)
    mypen.hideturtle()
    mypen.speed(20)

    radius = 150
    x=-150
    y=-150
    colors = ['red', 'blue', 'green', 'yellow', 'gray', 'black']
    for color in colors:
        draw_sqpolygon(mypen, x=x, y=y, radius=radius, size=1, side=None, pen_color='black', fill_color=color)

        x+= radius
        radius /= 2
        x+= radius
        y+= radius


#2번문제
my_pen = turtle.Turtle()
screen.setup(700,700)
def draw_sqpolygon(pen, x, y, radius, size=1, side=None, pen_color='black', fill_color=None):
    pen.pensize(size)
    pen.pencolor(pen_color)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if not fill_color:
        pen.circle(radius, steps=side)
    else:
        pen.fillcolor(fill_color)
        pen.begin_fill()
        pen.circle(radius, steps=side)
        pen.end_fill()


floor = 1
reverse_range = [7, 6, 5, 4, 3, 2, 1]
y_position = -300
for i in reverse_range:
    if floor % 2 != 0: #홀수층은 레드로 시작
        start_color = 'red'
        else_color = 'blue'
        side = None
    else:  #짝수층은 side 4
        start_color = 'blue'
        else_color = 'red'
        side = 4
    x_position = -300
    for _ in range(i):
        if _ % 2 == 0:
            draw_sqpolygon(pen=my_pen, x=x_position, y=y_position, radius=40, size=1, side=side, pen_color='black',
                           fill_color=start_color)
        else:
            draw_sqpolygon(pen=my_pen, x=x_position, y=y_position, radius=40, size=1, side=side, pen_color='black',
                           fill_color=else_color)
        x_position += 90  #짝수층 옆으로 i 개수동안 90 칸씩 옮기기
    y_position += 90
    floor += 1  #끝나면 층수올리기

# #3번 별 연속으로 5개 그려보기
def draw_star(mypen, color, x, y=0 ):
    mypen.goto(x, y)
    mypen.fillcolor(color)
    mypen.begin_fill()
    for _ in range(5):
        mypen.forward(100)
        mypen.right(144)
    mypen.end_fill()

if __name__=='__main__':
    mypen = turtle.Turtle()
    mypen.pensize(1)
    mypen.hideturtle()
    mypen.speed(20)

    colors = ['blue', 'red', 'blue', 'red', 'blue']
    x = -250
    for color in colors:
        draw_star(mypen, color ,x = x )
        x+=100
        
        
 #터틀로 snake 게임 구현하기

import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(side):
    for _ in range(side):
        angle = 360/side
        tim.forward(100)
        tim.right(angle)

for give_side in range (3,11) :
    tim.color(random.choice(colors))
    draw_shape(give_side)
#

# 무작위 구현하기
angle = [0, 90, 180, 270]
for _ in range(200) :
    tim.pensize(15)
    tim.speed("fastest")
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(angle))


#TODO 컬러모드 함수

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)  #튜플은 한번정의후 수정x . 수정원하면 리스트로변경해야함!
    return random_color  #튜플을 반환 (r,g,b)중 하나의값 반환해줌

angle = [0, 90, 180, 270]

for _ in range(200):
    tim.pensize(15)
    tim.speed("fastest")
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(angle))



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.speed("fastest")
tim.pensize(15)

#스피로그래피가 처음으로 오면 멈추기
is_on = True
while is_on :
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()  #current_heading 정의한 이유는 float로 바꿔서 +10 하려고.
    tim.setheading(current_heading + 10)
    if tim.heading() == 0.0 :
        is_on = False
    else :
        continue

#각도 지정해서 그려보기
def draw(gap):
    for _ in range( int(360 / gap)) : #나누기는 float가 되서 int로 바꿔야함
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()  #current_heading 정의한 이유는 float로 바꿔서 +10 하려고.
        tim.setheading(current_heading + gap)
draw(5)

screen = t.Screen()

 ---- 컴프입 과제 ----


import turtle
screen = turtle.Screen()
# #1번문제

screen.setup(600,600)

def draw_sqpolygon(pen, x, y, radius, size=1, side=None, pen_color='black', fill_color=None):
    pen.pensize(size)
    pen.pencolor(pen_color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if not fill_color:
        pen.circle(radius, steps=side)
    else:
        pen.fillcolor(fill_color)
        pen.begin_fill()
        pen.circle(radius, steps=side)
        pen.end_fill()


if __name__=='__main__':
    mypen = turtle.Turtle()
    mypen.home()
    mypen.pensize(1)
    mypen.hideturtle()
    mypen.speed(20)

    radius = 150
    x=-150
    y=-150
    colors = ['red', 'blue', 'green', 'yellow', 'gray', 'black']
    for color in colors:
        draw_sqpolygon(mypen, x=x, y=y, radius=radius, size=1, side=None, pen_color='black', fill_color=color)

        x+= radius
        radius /= 2
        x+= radius
        y+= radius


#2번문제
my_pen = turtle.Turtle()
screen.setup(700,700)
def draw_sqpolygon(pen, x, y, radius, size=1, side=None, pen_color='black', fill_color=None):
    pen.pensize(size)
    pen.pencolor(pen_color)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if not fill_color:
        pen.circle(radius, steps=side)
    else:
        pen.fillcolor(fill_color)
        pen.begin_fill()
        pen.circle(radius, steps=side)
        pen.end_fill()


floor = 1
reverse_range = [7, 6, 5, 4, 3, 2, 1]
y_position = -300
for i in reverse_range:
    if floor % 2 != 0: #홀수층은 레드로 시작
        start_color = 'red'
        else_color = 'blue'
        side = None
    else:  #짝수층은 side 4
        start_color = 'blue'
        else_color = 'red'
        side = 4
    x_position = -300
    for _ in range(i):
        if _ % 2 == 0:
            draw_sqpolygon(pen=my_pen, x=x_position, y=y_position, radius=40, size=1, side=side, pen_color='black',
                           fill_color=start_color)
        else:
            draw_sqpolygon(pen=my_pen, x=x_position, y=y_position, radius=40, size=1, side=side, pen_color='black',
                           fill_color=else_color)
        x_position += 90  #짝수층 옆으로 i 개수동안 90 칸씩 옮기기
    y_position += 90
    floor += 1  #끝나면 층수올리기

# #3번 별 연속으로 5개 그려보기
def draw_star(mypen, color, x, y=0 ):
    mypen.goto(x, y)
    mypen.fillcolor(color)
    mypen.begin_fill()
    for _ in range(5):
        mypen.forward(100)
        mypen.right(144)
    mypen.end_fill()

if __name__=='__main__':
    mypen = turtle.Turtle()
    mypen.pensize(1)
    mypen.hideturtle()
    mypen.speed(20)

    colors = ['blue', 'red', 'blue', 'red', 'blue']
    x = -250
    for color in colors:
        draw_star(mypen, color ,x = x )
        x+=100





------------------------
#TODO 터틀이용해서 SNAKE 게임 만들기

import time
from turtle import Turtle, Screen
from snake import Snake

snake = Snake()

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0) #???

screen.listen() #입력을 들을수있음 알아보기!!
screen.onkey(snake.up,"Up") # .onkey(함수,"키보드키")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#segment =[] #3개를 한마리로 뭉침



game_is_on = True

while game_is_on:
    screen.update() #
    time.sleep(0.1)  # 0.1 초마다 업데이트시킴

    snake.move() # 움직이게하고 0.1초마다 업뎃뎃


-------------------------------
여기서부터는 snake 안에 Snake 클래스 만듬

from turtle import Turtle

STARTING_POSITION = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.crate_snake()
        self.head = self.segments[0]

    def crate_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):  # 2번째가 1번째로가고, 2번째가 0번째로가고, 0번째를 20 보 진전
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)  # 2번째가 1번째 자리로 가게함
        self.head.forward(MOVE_DISTANCE)

    def up(self): #첫번째자리가 꺾어야됨
        if self.head.heading() != DOWN :  #heading() 은 turtle 에 내장되있는 메쏘드임. 방향을 확인해줌
            self.head.setheading(UP) #self.segments[0] 을 head 라는 속성으로 정의하자

    def down(self): #첫번째자리가 꺾어야됨
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): #첫번째자리가 꺾어야됨
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self): #첫번째자리가 꺾어야됨
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

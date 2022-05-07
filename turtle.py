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

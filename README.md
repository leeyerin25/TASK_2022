# TIL

---
---
**3/15**

TYPE, 제곱 적용 

```python
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
```

#Write your code below this line 👇

```python
height_second=(float(height))
weight_second=(int(weight))
result=(weight_second/height_second**2)   
print(float(result))
print(int(result))
```

***2 는 2의제곱*


#it's teacher's code 👇
```python
bmi = weight_as_int / heiight_as_float **2
bmi_as_int = int(bmi)
print(bmi_as_int)
```
CONSOLE<br>
enter your height in m: 1.75 <br>
enter your weight in kg: 80<br>
26.122448979591837<br>
26

<br>

<br>
<br>
<br>
<br>


---
---

**3/16**

f-string 함수 적용

```
age = input("What is your current age?")
```
#Write your code below this line 👇
```python
days=(365*90-int(age)*365)
weeks=(52*90-int(age)*52)
months=(12*90-int(age)*12)
print(f" You have {days} days, {weeks} weeks, and {months} months left.")
```

CONSOLE<br>
What is your current age?56
 You have 12410 days, 1768 weeks, and 408 months left.




f함수+사칙연산함수+소수점함수



 ```python
 #If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill?"))

tip_2=(tip/100*bill+bill) #팁퍼센트*총금액 = 팁금액+총금액
pay=int(tip_2)/people
pay_final="{:.2f}".format(pay)  #f-string 더 자주사용
print(pay_final)
```

*.2f*



* CONSOLE

Welcome to the tip calculator!

What was the total bill? $150

How much tip would you like to give? 10, 12, or 15? 12

How many people to split the bill?5
33.600000
<br>
<br><br>
<br>
<br>

---
---




**3/17**

IF ELSE 함수

 ```python
number = int(input("Which number do you want to check? "))

#Write your code below this line 👇
if number%2==0:
 print("This is an even number.")
else:
  print("This is an odd number.")
```

*if 에 : 까먹지 않기* <br>
*%는 나누고 난 나머지값 도출*
<br>
COLSOLE<br>
Which number do you want to check? 94<br>
This is an even number.
<br>
<br>

---
if,else,round 적용
```python
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Write your code below this line 👇
bmi=round(weight/height**2)

if bmi<18.5:  
 print(f"Your BMI is {bmi}, you are underweight.") 
elif bmi<25:   # below만 생각하기
 print(f"Your BMI is {bmi}, you are normal weight") 
elif bmi<30:
 print(f"Your BMI is {bmi}, you are slightly overweight") 
elif bmi<35:
 print(f"Your BMI is {bmi}, you are obese") 
else:    #나머지는 else
 print(f"Your BMI is {bmi}, you are clinically obese")
 ```

 COLSOLE<br>
 Your BMI is 28, you are slightly overweight.
<br>
<br>

---
**if , else 구하기 보스문제<br>**
**leap year : 윤년 : 4년마다 도래되는 해를 표시하라**<br><br>
1.흐름 flow 만들기 (어떻게 계산할것인지)
<br>2.시각화하기<br><br>


*틀린버전1*
 ```python
 year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#t=round(year/4,1)
if year%4==0:
  if year%100\=0:     #????
    if year%400==0:
     print("Leap year.")
else:
  print("Not leap year." )  #????

```

```PYTHON
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))

#Write your code below this line 👇

if year%4==0: #4로 나눈 나머지가 0일시 윤년 아님
 if year%100==0:  #여기서 100으로 나눈값에 나머지가 0일시 윤년임
   if year%400==0: #근데 여기까지 
    print("Leap year.") 
   else:
    print("Not Leap year." ) # %400 ->0 
 else:
  print("Leap year." ) # %100->0 
else:
 print("Not leap year." ) # %4 

#4로나눴을때 0 -> 윤년아님
#4로나눳을때 0, 100으로나눳을때0 -> 윤년
#4로나눳을때 0, 100으로나눳을때0, 400으로 나눴을때가 0 -> 윤년

 ```
<br>
<br>
<br>

---
---

 3/19<BR>
IF함수
 ```PYTHON
 # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


#Write your code below this line 👇

if size=='L':
 bill = 25
 if add_pepperoni=='Y':
  bill = bill+3
 if size=='M':
  bill = 20
  if add_pepperoni=='Y':
   bill = bill+3
  if size=='S':
   bill = 15
   if add_pepperoni=='Y':
    bill = bill+1

if extra_cheese=='Y':
 bill = bill+1
 ```

 CONSOLE
<BR> 28

 ```python
 # 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Write your code below this line 👇

name1 = name1.lower() #.lower()
name2 = name2.lower()
name3 = f'{name1}{name2}' #f스트링은 가로 필요없음

a=name3.count('t')+name3.count('r')+name3.count('u')+name3.count('e')
b=name3.count('l')+name3.count('o')+name3.count('v')+name3.count('e')

ab=int(f'{a}{b}')

if ab<10 or ab>90:
 print(f'Your score is {ab}, you go together like coke and mentos.')
elif 40<ab<50:
 print(f'Your score is {ab}, you are alright together.')
else:
 print(f'Your score is {ab}.')	   
```

CONSOLE<BR>
Welcome to the Love Calculator!
What is your name? 
Kanye West
What is their name? 
Kim Kardashian
Your score is 42, you are alright together.
<br>
<br>
<br>

---
---
3/20<br>
틀린버전1
```python
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
leftright=input("Youre at a crossroad. Where do you want to go? Type 'left' or 'right'")
waitswim=input("Youve come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across.")
dore=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")

print(leftright)
if leftright=='left':
	print(waitswim)
	if waitswim=='wait':  #여기에 넣는게 아니라 여기에 바로 input을해서 질문을 이어가야함. 그리고 그 input에 제목을 붙혀줘서 나중에 이용할 수 있게 해야함
		print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
	else:
		print("You fell into a hole. Game Over.")
elif leftright=='right':
	print("fall in a hole. game over.")
  ```

  정답
  ```python
  print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
leftright=input('Youre at a crossroad. Where do you want to go? Type "left" or "right".') #1번째 질문을 INPUT 사용해서 생성

if leftright=="left": 
	waitswim=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
	if waitswim=="wait":
		door=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
		if door=='yellow':
			print("You found the treasure! You Win!")
		else:
			print("You chose a door that doesn't exist. Game Over.")	
	else:
		print("You fell into a hole. Game Over.")
elif leftright=='right':
	print("fall in a hole. game over.")
  ```

CONSOLE<br>
Welcome to Treasure Island.<br>
Your mission is to find the treasure.<br>
Youre at a crossroad. Where do you want to go? Type "left" or "right".left<br>
You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.wait<br>
You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?red<br>
You chose a door that doesn't exist. Game Over.

---

RANDOM함수<br>
함수는3종류 내장형 / 모듈 / 다운받아야되는거
```PYTHON 
import random # import  + random.radnint
ramdom2=random.randint(1,6) #1~6사이 숫자 무작위추출

print(ramdom2)

random3=random.random() #0~1사이 무작위 추출
print(random3)
```
CONSOLE
<BR> 3<BR>0.25445<br><br>

---

랜덤으로 숫자 뽑고 1이면 head를 표시, 0이면 tails를 표시하라

```python
import random
random2 =random.randint(0,1)

if random2==1:
	print("Head")
else:
	print("Tails")
```

---
random,split함수<BR>
틀린버전
```python
import random #import random 은 보통 맨윗줄에
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")  
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
len=len(names)
random1 = random.randint(0,len-1) #뽑을 범위수를 정함

print(f'{random1} is going to buy the meal today!')
```
<br>
정답버전<br>

```python
import random #import random 이라는 모듈을 써야 그에 딸려오는 choice,sample 등의 함수를 불러올수있다. 
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #kim, lee[, ]park
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
len=len(names)
random1 = random.randint(0,len-1) # 들어오는 이름에서 아무거나 뽑아주는게됨
person=names[random1]  #리스트에서 숫자로 추출하는거
print(f'{person} is going to buy the meal today!')
```
<br><br>
---
---
3/21<br>list함수
```python
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

hori=int(position[0]) #2
verti=int(position[1]) #3

selected_row=map[verti-1] #맵에서 row1,row2,row3이냐 몇번째 줄인가를 골라줌 + 줄을 정하는게 우선순위
selected_row[hori-1] = "x" #그줄에서 몇번째 박스인가를 골라줌

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
```
CONSOLE
```PYTHON
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜']
Where do you want to put the treasure? 23
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'x', '⬜']  #23을 넣었을때 
#3의 행을 먼저 찾고, 2라는열의 위치를 찾는다.
```
---
list,if,random,input 함수 "가위바위보게임"<BR>
1차버전
```python
list=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice==0: #0을 뽑기위해선 인풋을 int로 적용시켜야함
	print(rock)
	if choice==1:
		print(paper)
		if choice==2:
			print(scissors) #넘 길어

radom= random.randint(0,2)
print("Computer choose" + list[radom])
```
정답
```python
list=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(list[choice]) #if 3줄을 한줄로 줄이는 방법

radom= random.randint(0,2)
print("Computer choose" + list[radom])

if choice==0 and radom==0:
	print("it's draw")
if choice==0 and radom==2:
	print("you win") .....
  ```
  CONSOLE
  ```
  What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
0

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer choose #RANDOM
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

it's draw
```
---
for in 반복문 (IN에 속한 값 수만큼 반복이 돌아야 끝남)
```python
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) 
# 🚨 Don't change the code above 👆

height_total = 0
for height in student_heights: 
 height_total = height_total + height #+height를 통해서 ex)140+160+180 이렇게 반복되어 더해짐
print(height_total)

number=0
for student in student_heights:
 number = number + 1 # +1을 통해서 140+160+180의 숫자만큼 1씩만 더해진다. (input값과 상관없이)

 print(round(height_total/number))

```
CONSOLE<BR>
Input a list of student heights<BR> 100 200 300 100<BR>
700<BR>
4<BR>S
175

---
```python
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()  #리스트로만듬 ["37","90","100"]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n]) #숫자로바꾸는작업
print(student_scores) # [37, 90, 100]

#Write your code below this row 👇
scoretotal =0
for score in student_scores:
	if score > scoretotal: # >를 통해 값을 쭉 비교하고
		scoretotal = score # =를 통해 score > scoretotal 이 성립할시 값을 바꿔준다
print(f"the score is :{scoretotal} .") #궁금한점 PRINT를 앞에붙히는것과 띄어쓰기해서 나온값이 다르던데 왜그런것인가?? for문 프린트가 되서 반복이 된것임.
```
CONSOLE<BR>
Input a list of student scores 140 150 187 100 195<BR>
[140, 150, 187, 100, 195]<BR>
the score is :195 .<BR>
<BR><BR><BR>

---
for in range 사용해서 값 전체더하기 (짝수만)
```
total = 0
for number in range(2,101,2): #2씩 커지게
	total = total+number
print(total)
```
``` 
total = 0
for number in range(2,101,2): 
	if number %2 == 0:  #나머지=0 인 값을 찾기=짝수
  total += number
print(total)
```
CONSOLE<BR>
2550
<BR><BR>

---
FOR IN RANGE + IF 함수 <BR>
오답
```
#Write your code below this row 👇
for number in range(1,101):
	if number %3==0 :
		print("Fizz")
	elif number % 5 == 0:
		print("buzz")
	elif number %3==0 and number %5==0 :
		print("fizzbuzz")
print(number)		#들어쓰기 틀림
```
```python
for number in range(1,101):
	if (number %3==0) and number %5==0 : #조건이 많은걸 먼저쓰는건가? 많은걸 먼저 써줘야 밑에서 안걸림 예시로 %5==0: 를 먼저쓰면 15 가 한바퀴 돌때 5에서 걸리고 %3과 %5 에서 걸리지 못함.
		print("fizzbuzz")
	elif number % 5 == 0:
		print("buzz")
	elif number %3==0 :
		print("fizz")
	else:
		print(number) #적용할게 없을땐 그대로 써주기


CONSOLE<BR>
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17 ....
```

```python
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
```
오답 easy case
```
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

random2 = random.randint(0,2)   #랜덤만 써선 못하나??
print(letters[random2] + "is gppd.")
```
정답 easy case
```py
password = "" #문장만들기위해 공란으로

for char in range (0,nr_letters):  #nr_letters INPUT 넣은회수만큼 돌게됨 -> 원하는 자릿수가 있다면 for in range로 나올 자릿수를 정해줘야함 
#궁금한건 char 은 그냥이름, 여기선 변수가 안쓰이고 반복만쓰임
	password = password + random.choice(letters)
	
for char in range (0,nr_symbols): 
	password = password + random.choice(symbols)
	
for char in range (0,nr_numbers): 
	password = password + random.choice(numbers)

 print(password)

 ---
CONSOLE
Welcome to the PyPassword Generator!
How many letters would you like in your password?
3
How many symbols would you like?
3
How many numbers would you like?
3
dAw%!!592
```
오답 hard case
```py
password_list = []

for char in range(0,nr_letters): 
	password_list.append(random.choice(letters))
	
for char in range(0,nr_symbols): 
	password_list = password_list + random.choice(symbols)
	# list + str => 에러가 남 그냥 다 append로 써줘야 리스트로 넣어짐
for char in range(0,nr_numbers): 
	password_list = password_list + random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

```
```
for _ char in enumerate(xxx)
1 a
2 b
3 c
4 d
```


3/22<br>
함수가이드 = pep8<br>

```
1.리펙터링(함수를 간단히 다시 만드는거)
함수 기존의걸 이용해서 새로만들기
def 함수이름():
	합칠함수()
	합칠함수()

함수이름 #시행됨

2. 파라미터	
def 함수이름(변수이름):
	print("쓰고싶은말 {변수이름}" ) #보여주는용도라서 이용안됨
	return #실제내보내는용도

print(함수이름)

함수이름{넣고싶은거}

출력: 쓰고싶은말 + 넣고싶은거
```
<br><br>

---

https://reeborg.ca/reeborg.html<br>
허들게임 난이도1 풀이
```py
def turn_right(): #def 다음줄은 무조건 띄어쓰기
    turn_left()
    turn_left()
    turn_left()

 #시행시에는 끝에 붙혀서 함수이름써서 호출

def one():
    move()
    turn_left()
    move()
    turn_right() #함수안에 함수
    move()
    turn_right()
    move()
    turn_left()

def 예시():
    a = 3
    if a > 2:
      print("a가2보다 클경우 프린트해야함") #프린트도 함수의 기능이기때문에 위 if 줄보다 더 안쪽으로 작성한다.
console
def()
:a가2보다 클경우 프린트해야함





i = 0    
while i < 6: # 5까지 5번 반복
    one()
    i += 1  # 위 one 이라는 함수를 5번 반복시킴

while True: # 무한반복

```
<br>
허들게임 난이도3 풀이

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():

    #일단 가 (앞이 뚫려있으면) 막혀있으면 가지말고..
    if front_is_clear():
        move()


    # 벽을 만났는데 오른쪽이 막혀있을경우 turn_left
    if (not front_is_clear()) and wall_on_right():
        turn_left() #if를 같은 열 위치에 두번쓸경우 : 두 if전부 실행시킴


    # 앞이 뚫려있고, 오른쪽이 막혀있음.
    elif front_is_clear() and (not wall_on_right()):
        turn_right() #if 열 위치에 elif 를 쓸경우 : 위의 if 가 해당하지 않을때 elif 로 내려옴 => 조건의 중요도를 부여해서 차례로 쓰는게 중요함

    # 앞이 막혀있고, 오른쪽은 ~~~
    elif (not front_is_clear()) and (not wall_on_right()):
        turn_right()
	```

  <br>
허들게임 난이도4 풀이

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn left()       #왼쪽으로돌아서
    while wall_on_right(): #오른쪽에 벽이 있는동안에는
        move()        #계속가라 
    turn_right()   #오른쪽을 봐라 (벽이없는순간이 와야 이 행의 함수가 실행됨 맞나용??)
    move()          #한칸앞 
    turn_right()    #다시 오른쪽
    while front_is_clear(): #앞이 비어있는동안에는
          move()            #직진
    turn left()    #왼쪽을 봐라(앞이 막혀있으면 이함수가 실행됨 . ?)
    
    #다시 위로 반복하면 어떠한 허들도 다 뛰어넘을수잇는 함수가 됨
    
while not at_goal(): 
    if wall_in_front():
        jump()
    else:
        move()

**나중에 day6 에스케이핑더 메이즈 프젝하기!!
```



<br><br> HANGMAN GAME<br>
3/23-day7<Br>구상화시키기

step1 

```py
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
choose = random.choice(word_list)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("gets a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for a in choose : #choose로 랜덤선택된 단어들이 쪼개져서 a로 들어가는게 신기함 -> str 이 들어가면 하나하나 들어가지는것인가용??
	if a == guess :
		print("right")
	else:
		print("worng")
		
```
step 2
```py

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []  
length = len(chosen_word)
for _ in range(length):
	display += "_" #display 라는 리스트 [] 안에 "_"를 추가해주는 단계 ????
print(display)

#list comprehension 리스트에 하나씩 추가

guess = input("Guess a letter: ").lower()


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(length): 
	letter = chosen_word[position] #chose_word 단어의 첫번째 알파벳이 letter 이 된다
	if letter == guess: #letter알파벳과 guess에넣은 알파벳하나가 같다면! 아까 그 display "-""-" 이 자리를 letter 알파벳으로 바꿔치고 아니면 말아라
		display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

```
step3
```py
#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")
```

step4
``` py
#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word: #너가 input한 알파벳인 guess가 chosen word에 포함되지 않으면  생명이 하나 깎임. 근데 포함되면 밑에 join이 프린트됨
        lives -= 1 
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}") #join은 리스트안에 한단어씩을 ''부분이 딱붙어서 나옴 
    #f스트링{} 안에 display 를 조인해주기위해서 ()가로를 씀

my_set = {"kim","park"} 셋(집합)은 순서가없음
print(" ".join(my_set)) -> 무작위로 조인됨, 조인시 결과물 : kim park

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
```

while 게임이 끝날때까지:<br>
 if<br>if<br>
 (게임이 끝날때를 정의해줘야함)<br>
 게임 조건 순서를 구상화시키는게 중요하다

*반복문 명령어*<br>
 continue : 해당 부분 다음 loop은 계속 진행<br>
 pass : 그냥 쭉 진행 <br>
 break : 멈춰줌 <br>

 ---
 <br><br><br>
 3/26<br>
 1.def 사용법<br>
 ```py
def add(a, b):
    return a + b  # add 라는 함수를 또 이용해서 쓰고싶으면 return값으로 정의해주기.

num1 = 1
num2 = 2

c = add(num1, num2)
c+1
 ```
2.def 응용법 (def 안에 for, if, enumerate, index)
```py
#def는 내가 원하는 조건을 넣어 만드는 함수, 여기서는 3개의 파라미터를 만들고, 해당된느 각각 조건을 만들어, 나만의 함수를 만들었다. : 목적: 알파벳 순서 원하는만큼 밀기

n_list=["a","b","c","d","e","f"]

# cbd -> edf
# 2

def number(text, n, what): #text는 변환하려는 알파벳이고, n은 움직이고싶은 숫자이며, what은 앞으로갈지 뒤로갈지 정하는것으로 하고싶다. 이제 함수를 만들어보자~


step1
    index_list = [] #먼저 리스트를 생성했음
    for alphabet in text: #사람으로부터 받은 text를 alphabet에 넣고. 
        index_list.append(n_list.index(alphabet))
    #반복문을 이용해 그 alphabet이 n_list에 있는 모든순서를 뽑음 (숫자는 -> index이용해서 추출)
    #ex) c면 n_list 에서 2번째, b면 1번째 이렇게 뽑고 append를 이용해 index_list에 뒤로 붙히고,  for문이 반복되면서 하나씩 채워진다 
    print(index_list) #프린트된 결과는 [2,1,3]

    #이렇게 1번째 피라미터인 text 에 대해 조건을 걸었다. text에 넣는 알파벳을 숫자로 변환시키기.
step2
    for index, i in enumerate(index_list): #그 index_list를 enumerate를 통해 숫자(index)와 i 로 변경한다.
        if what == "e": #여기서 파라미터3번째 조건 what을 생성한다. e 값을 넣을경우 바로 아래 함수가 실행된다.
            index_list[index] = i + n  
        else:
            index_list[index] = i - n #근데 난 d를 넣어서 이게 실행됨. 
            #ex) [2,1,3] 의[0]번째 = 2 - 1 = 1
            #ex) [2,1,3] 의[1]번째 = 1 - 1 = 0 ....

    print(index_list) #[1, 0, 2]
  #바꾸는 이유는? 움직이고 싶은 자리의 알파벳을 구하려면 자리수를 먼저 알아야하니까.

step3   
    decode_text = "" #알파벳으로 만들건데 일단 공란을 만들어줌
    for i in index_list: #마지막으로 완성된 index_list [1, 0, 2] 는 차례로 i로 들어간다
        decode_text += n_list[i] #그 i의 숫자는 아까 초기에 n_list에 해당되어 실제 알파벳으로 다시 변한이된다
    print(decode_text) #프린트하면 완성


#실제 사용자가 넣는 조건 : cbd 를 1칸씩 뒤로 옮겨주세요!  
number(text="cbd", n=1, what="d")
```
```
console

[2, 1, 3]
[1, 0, 2]
bac
```
<br><br><br>
3.+ index 개념
```py
my_list = ["a","b","c","d"]

my_list.index("a")
```
<br>console<br>
0<br><br><br>
4. def응용법2 (def 안에 while 넣기)<br>
```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 게임의 끝을 정하기 위해 while 넣어 go,stop을 결정합니다.

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter) #뽑은 알파벳을 숫자로변환해서 position에 담음
        if cipher_direction == "decode":
            shift_amount = shift_amount * -1 #오류부분이있음
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"here's the {cipher_direction}d result: {end_text}")



while True:
    ed = input("encode?decode:")
    test = input("input text:")
    shift = int(input("input shift:"))
    caesar(test, shift, ed)
    
    user_input = input("한번더?")
    if user_input == "yes":
        pass
    elif user_input == "no":
        break
```

---
<br><br><br>
3/29 day9
<Br>
```py
student_scores = {
  "Harry": 81,  #한키에는 하나의 value 만!
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores : #student_scores의 key부분인 이름이 뽑힘
	score = student_scores[student] #81=student_scores[harry] 
	if score > 90:
		student_grades[student] = "Outstanding"
	elif score > 80:
		student_grades[student] = "exptable"
	elif score > 70:
		student_grades[student] = "acceptable"
	elif score :
		student_grades[student] = "fail"

print(student_grades)

```
```
console
{'Harry': 'exptable', 'Ron': 'acceptable', 'Hermione': 'Outstanding', 'Draco': 'acceptable', 'Neville': 'fail'}
```
<br>
<br><br>

```py
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
	new_country = {}
	new_country["country"] = country_visited 
    #"country":"russia"
	new_country["visits"] = times_visited
    #"visits" : 2
	new_country["cities"] = cities_visited
	travel_log.append(new_country) 
    #위에 뽑힌 "country":"russia" 와 "visits" : 2 가 travel.log 뒤에 하나씩 붙혀짐
	

def 로 함수를 만든건
아래처럼 직접써주거나 

or

return 값을 써서 이용
ex) print(def이름(input(a,b)))


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


```
```
console 

[{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}] 
```
<br><br><br>

*딕셔너리 퀴즈* <br>

```
1. add하는법 정리
리스트["c"]=내용 
= = = x  
.append()  는 딕셔너리에서 사용 불가능. 리스트만 가능


2. 오류 정리<br>

dict = {"a" : 1
"b" : 2
"c" : 3
}
for key in dict:
    dict[key] +=1

console : a:2   b:3   c:4

3. 원하는거 출력하는 방법
```

```py
Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},

방법 : print(order["main"][2][0])
# [2]는 key 이름 , [0]은 불러올 내용의 순서
```


AUCTION PROGRAM
```py

from replit import clear #???????
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)


def bid(name, price)
    bids = {} 
	bids["이름"] = name
	bids["돈"] = price
    bids.append(bid)


while True:
    name = input("what is your name?")
    price = input("what is your bids?")
    continu = input("wanna go? yes or no")
    bid(name, price)
    

    if ucontinu == "yes":
        pass
    elif continu == "no":
        #여기서 제일높은 name과 price 의 가격을 추출할수있는 조건을 걸면 됨.
        break

```

```py
*딕셔너리에 중요한 규칙*

1. 콤마로 구분한다

my_dict = {
    "key" : value, #콤마로 구분
    "key2": value,
        ...
}



2. for문을 그냥 돌리면 키만 나온다.

for key in my_dict : 
    print(key)

console : "key" , "key2"




3. items를 쓰고 for문을 돌리면 키,value가 같이 나온다.

for key,value in my_dict.items(): # .items() 쓰면 key값과 value값이 같이 나옴
    print(key, value)

console : "key" : value, "key2": value,



4. 딕셔너리안에 원하는걸 추출하는 방법

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

Steak 추출하는법은
order["main"][2][0] #메인리스트에서 2번째리스트에 0번째단어를 추출함

```   

<br><br><br>
3/30 day10<br>
def 안에 if,return 넣기

```py
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()  #title은 Yerin 처럼 앞자리만 대문자로 바꿔줌
  formated_l_name = l_name.title()
  f"Result: {formated_f_name} {formated_l_name}"

#Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
```

```py
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(year, month):
	if is_leap(year) and month == 2:   #is_leap(year)이 true , month=2 true 일경우에만 29를 리턴해줌.
		return 29
	return month_days [month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```
```
console
Enter a year: 2020
Enter a month: 2
29
```
<br><br>

**퀴즈**

```py
1.What would you predict to be the result of running the following code?

def outer_function(a, b):
    def inner_function(c, d): #2. 그리고 밑에  inner_function 을 return을 해서 바로 이 똑같은 함수가 시행이 되는듯 ???
        return c + d
    return inner_function(a, b) #1. outer_function(a, b)에 대한 return값인 이줄이 바로 실행되는듯 ???
 
result = outer_function(5, 10)
print(result)

console=15




2.What will be printed in the console after running the following code?

def my_function(a):
    if a < 40:
        return   #return 다음에 바로 있어야되는데 없어서 none값!!
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

console=none

```

계산기문제
```py
def add(n1,n2):
	return n1 + n2

def sub(n1,n2):
	return n1-n2

def mul(n1,n2):
	return n1*n2

def div(n1,n2):
	return n1/n2

# if choose == '+' :
# 	add(add_1,add_2)
#딕셔너리 만들기!!
calculate={
	"+":add,
	"-":sub,
	"*":mul,
	"/":div
}

num1=int(input("what 1?"))  #input은 str 으로 받아져서 오류남 int 넣기!!
num2=int(input("what 2?"))

choose=input("what do u want?")
#for symbol in calculate:
symbol = calculate[choose] 
print(symbol)   
result = symbol(num1, num2)
print(result)
```

<br><br>
계산기문제 완성본
```py
from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(): #def calculator 안에 for 문과 while 문을 넣음, 보면 밑에 calculator()를 따로 써줘야 이 함수가 시행됨
  

  num1 = float(input("What's the first number?: ")) #num1 만 따로 빼놓음
  for symbol in operations:
    print(symbol)
  should_continue = True  #true로 가정함으로써 while문이 시행된건가? ㅇㅇ
#for문으로 꼭 돌리지 않아도 while 반복을 위해선 true 라는 가정이 필요한거. 그러니까 calculaator()이 함수에 ture 란 스위치를 바로 넣어두됨
 
  while should_continue: #이상태는 true
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y': #밑에게 false 니까 자동으로 이 y는 true가 됨
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
```
<br><br>
혼자 만들어봄
```py


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

#num1 , num2 , 사람이 원하면 계산된거에서 식과 num2만 바꿔서 쭉 진행시키고파

def calculator():
	num1 = float(input("what is yout first number??"))
	go = True # =대신 : 써서 틀림
	
	while go:
		symbol = input("what symbol?") #와일문안에 띄어쓰기안해서 틀림
		oper_2 = operations[symbol]
		num2 = float(input("what is yout second number??")) #float 안써서틀림
		result = oper_2(num1,num2)
		print(f"{num1} {symbol} {num2} = {result}")
		if input("you want keep y or n") == 'y' :  # y ''로 안감싸서 틀림
			num1 = result
		else :
			go : False
	
calculator()

```
<br><br><br>
4/1 blackjak game
```py

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random



def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card



#위치틀렸음  score 위에서 있어야 밑에 점수를 가지고 함수가 사용이 된다 
def compare(computer_score,user_score):  #에러뜸 -> 안에 파라미터 빠짐
	if computer_score == user_score :     #파라미터이름은 함수안에서 동일함, 받아오는 파라미터의 이름은 달라도 상관없음 ex. compare(a,b)
		return "draw" #return 빼먹음
	elif computer_score == 0 :	
		return "lose, opponent has blacjak"
	elif  user_score == 0 :	
		return "win, has blacjak"
	elif  user_score > 21 :	
		return "loose"
	elif  computer_score > 21 :	
		return "you win"
	elif computer_score < user_score :
		return "you win"
	else:
		return "you loose"

def calculate_score(cards):
	#user_card 이건 그냥 (cards) 자리에 두면 되는거!!
	if sum(cards) == 21 and len(cards) == 2:
		return 0	
	if 11 in cards and sum(cards) > 21 : #11 in cards and이거 빼먹음
		cards.remove(11)	#return 1이라고 틀림
		cards.append(1)

	return sum(cards) 

def play_game():
	user_cards = []
	computer_cards = []
	is_game_over = False 
	
	#게임 end 는 스위치로 for문 밑에 넣는다
	
	for _ in range(2): #반복해서 리스트에 추가만 할 용도
		pick = deal_card()	#여기틀림
		user_cards.append(pick)  # += 은 리스트만 가능, pick과 같이 하나의 수는 append를 이용!
		computer_cards.append(deal_card()) #이렇게 축약문도 가능
	
	while not is_game_over :	#is_game_over 이 true 가 될 때 반복을 멈춘다.	
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f" your cards : {user_cards} , score is {user_score}")
		print(f" computer first cards : {computer_cards[0]} ")
		
		
		if user_score == 0 or computer_score ==0 or user_score > 21 : #이거 만들고 폴문 위에 true false 스위치 키 만들기
			is_game_over = True #true면 게임 오벌되는것. 위에가 false 인것만으로도 게임이 끝날수가있나?ㄴㄴ while문에 넣기! ??
		else:
			y = input("'y' to get another card, 'n' to pass ")
			if y == 'y' :
				pick = deal_card()	
				user_cards.append(pick)  # 또 리스트 뒤에 한장 추가
			else :
				is_game_over : True #빼먹음
	
	while computer_score != 0 and computer_score < 17 : #stop은 17보다 클때 ?
		computer_cards.append(deal_card())  #17보다 작으면 한장 더 뽑는건가?
		computer_score = calculate_score(computer_cards)  
				b
	print(compare(computer_score, user_score))
		
#반복하고싶을때는 지금까지 한 모든 함수들을 또 반복시키는 함수에 집어넣으면됨. ex play_game()

while input("you waana paly? 'y' is connet ") == "y" :  #if로 잘못씀&시작부분이라 앞에붙히기
	play_game()
```
<br><br><br>
4/2 local , global scope 개념 퀴즈
```py
1.def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)

답: name error

```


```py
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list) #def 안에만 있는 상태

mutate([1,2,3,5,8,13])
```
```
console
[2, 4, 6, 10, 16, 26]
```
<br><br>
4/4 숫자맞추기게임
```py
import random


type = input("welcome , choose type 'easy' or 'hard'.")

random2=int(random.randint(1,101))
print(random2)
number = int(input("make a guess."))

if type == 'easy':
	attempts = 5
if type == 'hard':   #위 if문에 속하게 되면 type으로 hard를 넣었을경우 easy만 읽고 넘어가서 attempts는 없는게 됨
	attempts = 10

for _ in range(0,int(attempts)):
	attempts = attempts-1
	if random2>number : 
		print(f"too low.  you have {attempts} attempts.")
	elif random2<number :
		print(f"too higt. you have {attempts} attempts.")
	elif random2==number :    #elif*
		print("good.")
		break   
	number = int(input("make a guess."))

print("You've run out of guesses, you lose.") #빼먹음

  ```
```
console

welcome , choose type 'easy' or 'hard'.easy
98
make a guess.99
too higt. you have 4 attempts.
make a guess.97
too low.  you have 3 attempts.
make a guess.98
good.
```

<br><br>
선생님버전
```py
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns): 
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()

  guess = 0
  while guess != answer: #두개가 다른한 true 니까 계속 반복
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)  #turns 에 넣은 print값이 나올것.
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

```
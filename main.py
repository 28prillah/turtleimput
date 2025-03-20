import turtle
import random

screen = turtle.Screen()
screen.screensize(500, 500)
screen.bgcolor("black")

t=turtle.Turtle()

t.penup()
t.goto(0, 200 )
t.pendown()
t.pencolor("white")
t.write("background color", font=("arial", 30,"normal"), align= "center")

t.penup()
t.goto(-75, 100 )
t.pendown()
t.pencolor("tan")
t.write("1. Tan", font=("arial", 30,"normal"), align= "center")

t.penup()
t.goto(-75, 50 )
t.pendown()
t.pencolor("azure")
t.write("2. azure", font=("arial", 30,"normal"), align= "center")

t.penup()
t.goto(-75, 0 )
t.pendown()
t.pencolor("aquamarine")
t.write("3. aquamarine", font=("arial", 30,"normal"), align= "center")

t.penup()
t.goto(-75, -50 )
t.pendown()
t.pencolor("darkkhaki")
t.write("4. darkkhaki", font=("arial", 30,"normal"), align= "center")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("Black")
t.write("Enter your name", font=("arial",30, "normal"),align= "center")

choose = int(input("Chose one: "))
if choose == 1:
    screen.bgcolor("tan")
elif choose == 2:
    screen.bgcolor("azure")
elif choose == 3:
    screen.bgcolor("aquamarine")
elif choose == 4:
    screen.bgcolor("darkhaki")

t.penup()
t.goto(0,0)
t.pencolor("black")
t.write()

name=input("Enter a name: ")
# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter another number: "))
opperation = random.randint(1,4)

if opperation == 1:
    symbol = "+"
    number1=random.randint(-100,100)
    number2= random.randint(-100, 100)
    solution = number1 + number2

elif opperation == 2:
    symbol = "-"
    number1=random.randint(-100,100)
    number2= random.randint(-100, 100)
    solution = number1 - number2

elif opperation == 3:
    symbol = "*"
    number1=random.randint(-10,10)
    number2= random.randint(-10,10)
    solution =number1*number2

elif opperation == 4:
    symbol = "/"
    number1=random.randint(-10,10)
    number2= random.randint(1,10)
    sign=random.randint(1,2)

t.penup()
t.goto(0,150)
t.pendown()
t.pencolor("purple")
t.write(name,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("purple")
t.write(number1,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("purple")
t.write("+",font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("purple")
t.write(number2,font=("arial",30,"normal"),align="center")


t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("purple")
t.write("=",font=("arial",30,"normal"),align="center")

answer = int(input("Enter Answer: "))


t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("purple")
t.write(sum,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("black")
t.write("Your answer is: "+str(answer),font=("arial",30,"normal"),align="center")

if sum == answer:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor("black")
    t.write("Correct " + str(answer), font=("arial", 30, "normal"), align="center")
    
else:
    screen.bgcolor("darkorange")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor("black")
    t.write("incorrect " + str(answer), font=("arial", 30, "normal"), align="center")


turtle.done()

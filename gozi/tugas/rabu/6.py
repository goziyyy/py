import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")  
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("white") 

pen.penup()  
pen.goto(0, -200)  
pen.pendown()  

pen.begin_fill()
pen.circle(200) 
pen.end_fill()

pen2 = turtle.Turtle()
pen2.shape("turtle")
pen2.color("blue") 
pen2.penup() 
pen2.goto(0, -170) 
pen2.pendown() 

pen2.begin_fill()
pen2.circle(170)  
pen2.end_fill()

text = "SEKOLAH MENENGAH KEJURUAN PRESTASI PRIMA"
pen3 = turtle.Turtle()
pen3.penup()
pen3.hideturtle()
pen3.color("black")

radius = 100
num_chars = len(text)
angle = 360 / num_chars

for i, char in enumerate(text):
    angle_rad = math.radians(i * angle)
    x = radius * math.sin(angle_rad)
    y = -radius * math.cos(angle_rad)
    pen3.goto(x, y)
    pen3.write(char, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()
import turtle

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gambar_fibonacci_tree(turtle, n, length, angle):
    if n <= 0:
        return
    else:
        turtle.forward(length)
        turtle.left(angle)
        gambar_fibonacci_tree(turtle, n-1, length * 0.7, angle)
        turtle.right(angle * 2)
        gambar_fibonacci_tree(turtle, n-2, length * 0.7, angle)
        turtle.left(angle)
        turtle.backward(length)

window = turtle.Screen()
window.title("Pohon Fibonacci")

pen = turtle.Turtle()
pen.color("blue")

n = 10 
length = 100  
angle = 30 

pen.penup()
pen.goto(0, -200)
pen.pendown()

gambar_fibonacci_tree(pen, n, length, angle)

window.exitonclick()
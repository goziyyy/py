import turtle

def draw_custom_shape():

    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()


turtle.speed(1)

draw_custom_shape()

turtle.exitonclick()
import turtle


def drawSquare(size, color):
    turtle.speed(1)
    turtle.color(color)
    turtle.begin_fill()

    def move():
        turtle.forward(size)
        turtle.left(90)

    for _ in range(4):
        move()

    turtle.end_fill()


# drawSquare(100, "blue")
# turtle.goto(200, 200)
# drawSquare(100, "red")


# ================================================================

def drawHeart(size, color):
    turtle.speed(1)
    turtle.color(color)
    turtle.begin_fill()

    turtle.left(140)
    turtle.forward(size)

    turtle.circle(-size / 2, 200)

    turtle.left(120)
    turtle.circle(-size / 2, 200)

    turtle.forward(size)

    turtle.end_fill()


# drawHeart(150, "pink")

# turtle.penup()
# turtle.goto(250, 0)
# turtle.setheading(0)
# turtle.pendown()

# drawHeart(100, "pink")

# ================================================================


def drawFlower(size, color, petals, center_color):
    turtle.speed(3)
    turtle.color(color)
    turtle.begin_fill()

    for _ in range(petals):
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.left(120)

        turtle.left(360 / petals)

    turtle.end_fill()
    turtle.dot(40, center_color)


# drawFlower(80, "red", 8, "yellow")
# turtle.penup()
# turtle.goto(250, 0)
# turtle.setheading(0)
# turtle.pendown()
# turtle.setheading(0)

# drawFlower(80, "orange", 8, "yellow")

# ================================================================

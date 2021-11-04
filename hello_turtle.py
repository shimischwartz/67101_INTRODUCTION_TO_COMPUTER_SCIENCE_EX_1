"""This code should draw a bed with 3 flowers on the screen"""
import turtle


def draw_petal():
    """a function that draws a petal"""
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)


def draw_flower():
    """a function that draws a flower"""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)


def draw_flower_advance():
    """a function that draws a flower and moves the turtle to the next flower spot"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """a function that draws on the screen a bed with 3 flowers"""
    turtle.up()
    turtle.forward(250)
    turtle.left(180)
    turtle.down()
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()
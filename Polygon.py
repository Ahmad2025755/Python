import turtle

turtle.Screen().bgcolor("Green")

pen = turtle.Turtle()



# Triangle

pen.forward(100)

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

# Square

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)



# First triangle for star
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(150)

# Second triangle for star
pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.foward(100)


turtle.done()
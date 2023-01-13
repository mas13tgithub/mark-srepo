import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Create the chihuahua's body
my_turtle.color("brown")
my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()

# Create the chihuahua's head
my_turtle.color("white")
my_turtle.begin_fill()
my_turtle.circle(30)
my_turtle.end_fill()

# Create the chihuahua's ears
my_turtle.color("brown")
my_turtle.begin_fill()
my_turtle.left(90)
my_turtle.forward(30)
my_turtle.right(90)
my_turtle.forward(40)
my_turtle.right(90)
my_turtle.forward(30)
my_turtle.right(90)
my_turtle.forward(40)
my_turtle.end_fill()

# Create the chihuahua's eyes
my_turtle.color("black")
my_turtle.begin_fill()
my_turtle.left(90)
my_turtle.forward(10)
my_turtle.right(90)
my_turtle.forward(10)
my_turtle.right(90)
my_turtle.forward(10)
my_turtle.right(90)
my_turtle.forward(10)
my_turtle.end_fill()

# Keep the turtle window open until the user closes it
turtle.done()

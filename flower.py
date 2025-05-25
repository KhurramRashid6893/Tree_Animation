import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Flower Drawing")

# Create the turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)

# Function to draw a petal
def draw_petal():
    for _ in range(2):
        flower.circle(100, 60)  # Draw an arc
        flower.left(120)       # Rotate to draw the other side

# Function to draw the flower
def draw_flower(petals):
    for _ in range(petals):
        draw_petal()
        flower.right(360 / petals)

# Draw the stem
def draw_stem():
    flower.color("green")
    flower.pensize(5)
    flower.right(90)
    flower.forward(300)

# Draw the flower
flower.color("red", "yellow")  # Outline and fill color
flower.begin_fill()
draw_flower(6)  # Number of petals
flower.end_fill()

# Position for the stem
flower.setheading(270)
flower.penup()
flower.goto(0, -100)
flower.pendown()

# Draw the stem
draw_stem()

# Finish
flower.hideturtle()
screen.mainloop()

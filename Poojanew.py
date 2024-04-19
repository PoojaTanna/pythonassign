import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Create a turtle for displaying the name
pooja_turtle = turtle.Turtle()
pooja_turtle.color("white")
pooja_turtle.hideturtle()
pooja_turtle.penup()
pooja_turtle.speed(500)

# Define a function to move the turtle randomly and display "Pooja"
def display_pooja():
    while True:
        # Clear the turtle's drawing
        pooja_turtle.clear()
        
        # Move the turtle to a random position on the screen
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        pooja_turtle.goto(x, y)
        
        # Write the name "Pooja" at the current position
        pooja_turtle.write("Pooja", font=("Arial", 24, "bold"))
        
        # Pause for a short time to allow the text to be seen
        turtle.time.sleep(1)

# Call the function to start displaying "Pooja"
display_pooja()

# Keep the window open
turtle.done()

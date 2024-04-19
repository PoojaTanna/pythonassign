# Pooja-Thakkar
Importing Modules
The program starts by importing the turtle and random modules.
import turtle: This module is used to create graphical drawings and animations using turtles.
import random: This module allows you to generate random numbers and values.
Setting Up the Screen
A turtle graphics screen (screen) is created using turtle.Screen().
The screen size is set to 600 pixels wide and 600 pixels high using the screen.setup() method.
The background color of the screen is set to black using screen.bgcolor("black").
Creating the Turtle
A turtle named pooja_turtle is created using turtle.Turtle().
The turtle's color is set to white using the pooja_turtle.color("white") method.
The turtle is hidden from view using pooja_turtle.hideturtle() method.
The turtle's pen is lifted up using pooja_turtle.penup() method so that it doesn't draw lines while moving.
The turtle's speed is set very high (500) using pooja_turtle.speed(0).
Function Definition
A function display_pooja() is defined to move the turtle randomly across the screen and display the name "Pooja" at each position.
The display_pooja() Function
The function contains a while loop that continues running indefinitely (while True).
Inside the loop:
The pooja_turtle.clear() method is called to clear any existing drawings from the turtle.
The turtle moves to a random position on the screen:
Random x and y coordinates are chosen within the range of -300 to 300 using random.randint(-300, 300).
The turtle moves to the randomly chosen position using pooja_turtle.goto(x, y).
At the new position, the name "Pooja" is written using pooja_turtle.write("Pooja", font=("Arial", 24, "bold")).
The function pauses for one second using turtle.time.sleep(1) to keep the text visible for a while.
Running the Animation
At the end of the program, the display_pooja() function is called to start the animation.
The animation runs indefinitely, displaying "Pooja" randomly on the screen.
turtle.done() is called to keep the window open and allow the animation to continue running.

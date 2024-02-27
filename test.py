import turtle

# Create a function to pause the turtle
def pause():
  turtle.onkeypress(None, "space") # Disable spacebar key press
  turtle.listen() # Start listening for key presses

# Create a function to resume the turtle
def resume():
  turtle.onkeypress(pause, "space") # Enable spacebar key press
  turtle.listen() # Start listening for key presses

# Start the turtle
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Draw a square
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

# Pause the turtle
pause()

# Wait for the user to press the spacebar
turtle.mainloop()

# Resume the turtle
resume()

# Draw a circle
turtle.circle(50)

# Finish the turtle
turtle.hideturtle()
turtle.done()
import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    sally = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    sally.shape('turtle')
    # Set your turtle's speed using .speed(10)
    sally.speed(10)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    sally.color('green')
    sally.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    sally.color('yellow')
    sally.pencolor('black')
    sally.begin_fill()
    for i in range(4):
        sally.forward(1)
        sally.right(90)
    sally.end_fill()
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    x = 0
    y = 0
    sally.goto(x, y)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    sally.color('purple')
    sally.begin_fill()
    sally.circle(radius=150, steps=30)
    sally.end_fill()
    sally.color('green')
    sally.pencolor('blue')
    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

import turtle as t
import math

# Define the width and height of the screen
WIDTH = 640
HEIGHT = 480

# Define a purple gradient color palette
# This list contains tuples representing RGB values for different shades of purple
palette = [
    (148, 0, 211), (138, 0, 138), (153, 50, 204), (147, 112, 219), 
    (139, 0, 139), (148, 0, 138), (153, 50, 153), (147, 112, 147), 
    (139, 0, 100), (148, 0, 80)
]

# Set up the screen
# Create a screen object and set its background color and size
wn = t.Screen()
wn.bgcolor("#2b3e50")  # Set the background color to a dark blue
wn.setup(width=WIDTH, height=HEIGHT)  # Set the screen size to 640x480

# Create a turtle object
# This object will be used to draw the Pythagoras tree
p = t.Turtle()
p.speed(0)  # Set the drawing speed to the fastest
p.setheading(90)  # Set the initial direction of the turtle to upwards

# Define the recursive function to draw the Pythagoras tree
def tree(s, level):
    """
    This function recursively draws the Pythagoras tree.
    :param s: The length of the side of the square.
    :param level: The recursion depth (number of levels to draw).
    """
    if level < 1:
        return  # Base case: if the level is less than 1, stop recursion
    quadrat(s)  # Draw a square with side length s
    if level == 1:
        return
    # Left side
    ls = s * math.sqrt(3) / 2  # Calculate the length of the left subtree
    p.forward(s)  # Move forward by the length of the side
    p.left(90)  # Turn left by 90 degrees
    p.forward(s)  # Move forward by the length of the side
    p.right(150)  # Turn right by 150 degrees
    p.forward(ls)  # Move forward by the length of the left subtree
    p.left(90)  # Turn left by 90 degrees
    tree(ls, level - 1)  # Recursively draw the left subtree

    # Right side
    rs = s / 2  # Calculate the length of the right subtree
    p.right(180)  # Turn right by 180 degrees
    p.forward(rs)  # Move forward by the length of the right subtree
    p.left(90)  # Turn left by 90 degrees
    tree(rs, level - 1)  # Recursively draw the right subtree
    p.left(60)  # Turn left by 60 degrees
    p.back(s)  # Move backward by the length of the side

# Define the function to draw a square
def quadrat(s):
    """
    This function draws a square with the given side length.
    :param s: The length of the side of the square.
    """
    # Set the color of the square using the palette
    p.color(palette[int(s - 2) % 10], palette[int(s - 2) % 10])
    p.begin_fill()  # Start filling the square
    for _ in range(4):  # Draw four sides of the square
        p.forward(s)  # Move forward by the length of the side
        p.left(90)  # Turn left by 90 degrees
    p.end_fill()  # End filling the square

# Move the turtle to the starting position
p.penup()  # Lift the pen to move without drawing
p.setpos(120, -HEIGHT / 2 + 60)  # Set the starting position
wn.tracer(0)  # Turn off screen updates to speed up drawing
p.pendown()  # Put the pen down to start drawing

# Draw the Pythagoras tree with a recursion depth of 14
tree(85, 10)  # Call the tree function with initial side length 85 and recursion depth 14
p.hideturtle()  # Hide the turtle cursor
wn.update()  # Update the screen to show the drawing

# Keep the window open until it is closed by the user
wn.mainloop()  # Start the main loop to keep the window open
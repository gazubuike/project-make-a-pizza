import turtle
BACKGROUND_COLOR = "#9EC388" # Constants (green)
CRUST_COLOR = "#ECA84F" # Begins executing crust color
SAUCE_COLOR = "#AD0509" # Begins executing sauce color
CHEESE_COLOR = "#FBC70F" # Begins executing cheese color
PEPPERONI_LOCATIONS = [ # List of locations where pepperoni will be placed
    [-70, 105], # location[0], location[1]
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 120],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150]
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR) # Passing in constant set for background color
screen.title("My Pizza")

my_turtle = turtle.Turtle() # Creating the pen, calling it my_turtle
my_turtle.pensize(5)
my_turtle.shape("circle")

def draw_circle(radius, line_color, fill_color): # The three things we need to draw a circle passed in as arguments
    my_turtle.color(line_color) # Changing line color to whatever we want 
    my_turtle.fillcolor(fill_color) # Whatever is passed in as the fill color
    my_turtle.begin_fill()
    my_turtle.circle(radius) # Draw circle with radius passed in
    my_turtle.end_fill()

# Moves our turtle with out drawing on the screnn
def move_turtle(x, y): # Passed in x and y coordinate
    my_turtle.up() # Lift pen off the screen (also written as .penup)
    my_turtle.goto(x, y) # Moves the turtle
    my_turtle.down() # Moves the pen back down (also written as .pendown)

draw_circle(150, CRUST_COLOR, CRUST_COLOR) # Circle drawn with radius of 150 pixels, crust colored line, crust colored fill
move_turtle(0, 25) # Picks up the pen by 25 pixels
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR) # Sets a circle being drawn with 125 radius, sauce color as line color and cheese color as fill color

# Drawing the pepperoni
for location in PEPPERONI_LOCATIONS: # Loop for amount of times drawn
    move_turtle(location[0], location[1]) # List of lists, following set coordinates on where to move the pen
    draw_circle(10, SAUCE_COLOR, SAUCE_COLOR) # Sets circles drawn with radius 10, sauce color as line color and sauce color as fill color

# Move the pen back to the center and change it to the same color as background
move_turtle(0, 150)
my_turtle.color(BACKGROUND_COLOR)
my_turtle.pensize(2)

# Loop through 8 times: put our pen down, turn 45 degrees, move out 150 pixels, pick up our pen then bring it back by 150 the same amt
for x in range(0, 8):
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(150)
    my_turtle.penup()
    my_turtle.backward(150)

turtle.done()


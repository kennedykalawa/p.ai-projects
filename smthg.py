import turtle
import colorsys

# Set up the screen
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")  # Set background to black for a dramatic effect
t.speed(0)  # Set the fastest drawing speed
n = 50  # Number of segments in the helix
h = 0  # Starting hue value

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1) # Convert HSV color to RGB
    t.pencolor(c) # Set the pen color
    t.begin_fill() # Start filling the shape
    h += 1/n # Increment the hue for the next segment
    t.circle(i, 45) # Draw a circle arc
    t.right(140) # Turn right
    t.circle(i, 45) # Draw another circle arc
    t.end_fill() # Stop filling and fill the shape

turtle.done() # Keep the window open until you close it
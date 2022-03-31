import turtle # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def change_to_red():
    tess.fillcolor("red")

def change_to_green():
    tess.fillcolor("green")

def change_to_blue():
    tess.fillcolor("blue")

def increase_pen_size():
    _,__,pen_size = tess.shapesize()
    if pen_size < 20:
        tess.shapesize(3, 3, pen_size + 1)
    print(tess.shapesize()[2])

def decrease_pen_size():
    _,__,pen_size = tess.shapesize()
    if pen_size > 1:
        tess.shapesize(3, 3, pen_size - 1)
    print(tess.shapesize()[2])

# This variable holds the current shape of the machine
shape_num = 0

def advance_shape_machine():
    global shape_num
    if shape_num == 0: # Transition from state 0 to state 1
        tess.shape("square")
        shape_num = 1
    elif shape_num == 1: # Transition from state 1 to state 2
        tess.shape("triangle")
        shape_num = 2
    else:  # Transition from state 2 to state 0
        tess.shape("circle")
        shape_num = 0
    
# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

# Bind the color functions to its keys.
wn.onkey(change_to_red, "r")
wn.onkey(change_to_green, "g")
wn.onkey(change_to_blue, "b")

# Bind the size functions to its keys.
wn.onkey(increase_pen_size, "plus")
wn.onkey(decrease_pen_size, "minus")

# Bind the shape function to its key.
wn.onkey(advance_shape_machine, "s")

wn.listen() # Listen for events
wn.mainloop()
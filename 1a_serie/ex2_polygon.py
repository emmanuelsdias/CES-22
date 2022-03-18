import turtle
PINK = (1, 106/255, 180/255)

def draw_poly(t, n, sz):
    """ Make turtle t draw a regular polygon of n sides sz """
    theta = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(theta)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.width(3)
tess.color(PINK)

draw_poly(tess, 8, 50)

wn.mainloop()

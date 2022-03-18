import turtle
PINK = (1, 106/255, 180/255)

def draw_squares(t, n, sz):
    """ Make turtle t draw n squares of sides (1, 2, ..., n) sz """
    for i in range(n):
        side = sz*(i+1)
        for j in range(4):
            t.forward(side)
            t.left(90)
        t.up()
        t.goto(t.pos()-(sz/2, sz/2))
        t.down()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

ana = turtle.Turtle()
ana.width(3)
ana.color(PINK)

draw_squares(ana, 5, 20)

wn.mainloop()

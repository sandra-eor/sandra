from turtle import *
def circle():
    c = Turtle()
    c.begin_fill()
    c.setheading(505)
    c.circle(35,360)
    c.fillcolor("yellow")
    c.end_fill()


def petalo_1():
    p = Turtle()
    p.begin_fill()
    p.setheading(505)
    p.color("pink")
    p.goto(-35,140)
    p.circle(60,180)
    p.left(45)


    p.end_fill()
    #petalo1.hiderturtle 

def hoja():
    h = Turtle()
    h.begin_fill()
    h.fillcolor("green")
    h.setheading(505)
    h.color("green")
    h.left(80)
    h.circle(90,180)
    h.left(80)
    h.circle(90,180)
    h.right(35)
    h.forward(100)

    h.end_fill()

    





def petalo_2():
    p2 = Turtle()
    p2.begin_fill()
    p2.setheading(0)
    p2.color("pink")
    p2.goto(35,0)
    p2.circle(60,180)
    p2.right(45)


    p2.end_fill()
    #petalo2.hiderturtle 


def another_flower():
        af= Turtle ()
        af.begin_fill()
        af.color("red")
        af.left(30)
        af.forward(30)
        af.circle(30,180)
        af.right(30)
        af.forward(30)
        af.right(30)
        af.circle(30, 180)
        af.right(30)
        af.forward(30)
        af.left(180)
        af.forward(30)

        af.circle(30,180)
        af.right(30)
        af.forward(30)
        af.right(30)
        af.circle(30, 180)
        af.right(30)
        af.forward(30)
        af.left(180)
        af.forward(30)

        af.circle(30,180)
        af.right(30)
        af.forward(30)
        af.right(30)
        af.circle(30, 180)
        af.right(30)
        af.forward(30)
        af.left(180)
        af.forward(30)

        af.circle(30,180)
        af.right(30)
        af.forward(30)
        af.right(30)
        af.circle(30, 180)
        af.right(30)
        af.forward(30)

        af.end_fill()

     
if __name__== "__main__":
    hoja()
    another_flower()
    circle()
    exitonclick()
  

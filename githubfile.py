from turtle import *
from random import random
def circle():
    c = Turtle()
    c.speed(0)
    c.begin_fill()
    c.color("black")
    c.setheading(505)
    c.penup()
    c.circle(35,360)
    c.fillcolor("yellow")
    c.end_fill()


def petalo_1():
    p = Turtle()
    p.speed(0)
    p.begin_fill()
    p.setheading(200)
    p.color("green")
    p.goto(35,-140)
    p.circle(60,180)
    p.left(45)


    p.end_fill()
    #petalo1.hiderturtle 

def hoja():
    h = Turtle()
    h.speed(0)
    h.begin_fill()
    h.pendown()
    h.fillcolor("green")
    h.setheading(505)
    h.color("green")
    h.left(80)
    h.circle(90,180)
    h.left(80)
    h.circle(90,180)
    h.pendown()
    h.right(35)
    h.forward(100)

    h.end_fill()

    





def petalo_2():
    p2 = Turtle()

    p2.begin_fill()
    p2.setheading(0)
    p2.color("green")
    p2.goto(-50,0)
    p2.circle(60,180)
    p2.right(30)


    p2.end_fill()
    #petalo2.hiderturtle 


def another_flower():
        af= Turtle ()
        af.speed(0)
        af.begin_fill()
        af.color("red")
        af.pendown()
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

def signature ():
     s = Turtle()
     s.penup()
     s.pensize(35)
     s.begin_fill()
     s.goto(100,100)
     s.write("∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒƸ̵̡Ӝ̵̨̄Ʒ 𝒮𝒶𝓃𝒹𝓇𝒶 💙𝓇𝓉𝒾𝓏 Ƹ̵̡Ӝ̵̨̄Ʒ ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ")
     s.end_fill()
     
if __name__== "__main__":
    hoja()
    petalo_2()
    another_flower()
    circle()
    signature()
    exitonclick()
  

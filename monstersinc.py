

from turtle import * 
from random import randint, choice

############# DEFINE CLASSES AND FUNCTIONS #############
def road():
    r = Turtle()
    r.hideturtle()
    r.speed(0)
    r.goto(-260,500)
    r.fillcolor("black")
    r.begin_fill()
    r.goto(260,500)
    r.goto(260,-500)
    r.goto(-260,-500)
    r.end_fill()

class Car(Turtle):
    '''
    Constructor
    '''
    def __init__(self,shape,x,y):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto( x ,y )
        self.setheading(270)
    '''
    drive() Method
    '''
    def drive(self):
         self.forward(10)
    '''
    relocate() Method
    '''
    def relocate(self):
        if self.ycor()<-500:
            self.goto(randint(-150,150),500)

    def collide(self,player):
        distSq = (self.xcor() - player.xcor())** 2 + (self.ycor() - player.ycor())**2
        dist = distSq ** 0.5

        if dist < 30:
            print("collide")
            return True
        return False
    
    
class Player (Turtle):

    def __init__(self,shape,x,y):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto( x ,y )

        self.screen.onkeypress(self.go_right,'d')
        self.screen.onkeypress(self.go_left,'a')
        self.screen.listen()

    def go_right(self):
        print("right")
        self.goto(self.xcor()+15 ,self.ycor())

    def go_left(self):
        print("left")


        self.goto(self.xcor()-15,self.ycor())

############# YOUR PROGRAM  #############
screen = Screen()
screen.tracer(0)
screen.bgcolor("pink")
road()
screen.register_shape("boo.gif")
screen.register_shape("randall.gif")
screen.register_shape("solivan.gif")
screen.register_shape("wazoski.gif")
screen.register_shape("monster1.gif")
screen.tracer(1)

images = ["boo.gif", "randall.gif", "solivan.gif", "wazoski.gif", "monster1.gif"]

#c = Car("one.gif",100,100)
#d = Car("two.gif",100,100)
cars =[]
for i in range (5):
    temp = Car (images[i], randint(-150,150),randint(300,300))
    cars.append(temp)

player = Player("boo.gif",0,-200)

running = True
while running:
    for car in cars:
        car.drive()
        car.relocate()
        if car.collide(player):
            running = False
            break


screen.mainloop()
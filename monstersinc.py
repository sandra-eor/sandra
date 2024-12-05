
from turtle import Turtle, Screen 


class Car(Turtle):
    def __init__(self):
        super() .__init__()
        self.shape("car.gif")

s=Screen()
s.register_shape("car.gif")


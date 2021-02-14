import turtle
from random import *
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
l = []

def set_direction(n):
    for i in range(n):
        if i == n:
            l[i].setheading(l[i].towards(l[0]))
        else:
            l[i-1].setheading(l[i - 1].towards(l[i]))

def forward_l(n,step):
    for i in range(n):
        l[i].forward(step)

def setturt(n):
    for i in range(n):
        R = random()
        G = random()
        B = random()
        l.append(turtle.Turtle())
        l[i].pencolor(R, G, B)
        l[i].write(alphabet[i], False, 'left', ('Times new roman', 8, 'normal'))

def drawpolygon(n):
    for i in range (n):
        l[i].penup()
        for j in range(i):
            l[i].forward(200)
            l[i].left(360/n)
        l[i].pendown()


def main():
    totaldistance = 0
    n2 = eval(input("Please enter the number of sides you want your polygon to have: "))
    setturt(n2)
    drawpolygon(n2)

    distance = l[0].distance(l[1])
    '''print("distance between l[2] and l[1]",l[2].distance(l[1]))
    print("distance between l[0] and l[1]",distance)
    print("distance between l[0] and l[2]",l[2].distance(l[0]))'''

    while distance >= 0.1:
        step = 0.2
        if distance <= 10:
            print ("WE HAVE ENTERED THE IF")
            step = 0.1
        forward_l(n2, step)
        totaldistance += step
        set_direction(n2)
        distance = l[0].distance(l[1])
        print(distance)
    print(totaldistance, "is the total distance.")
main()
screen = turtle.Screen()
screen.tracer(0)
screen.exitonclick()
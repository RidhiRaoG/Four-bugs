import turtle
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()

a.penup()
a.goto (200, 200)
a.pendown()

b.penup()
b.goto(200, -200)
b.pendown()

c.penup()
c.goto(-200, -200)
c.pendown()

d.penup()
d.goto(-200, 200)
d.pendown()

screen = turtle.getscreen()
screen.bgcolor ("black")

#a.shape ('turtle')
a.pencolor ("red")
a.color ("red")
a.write("Alpher", False, 'left', ('Times new roman', 8, 'normal'))

#b.shape ('turtle')
b.pencolor ("orange")
b.color ("orange")
b.write("Bethe", False, 'left', ('Times new roman', 8, 'normal'))

#c.shape ('turtle')
c.pencolor ("yellow")
c.color ("yellow")
c.write("Gamow", False, 'left', ('Times new roman', 8, 'normal'))

#d.shape ('turtle')
d.pencolor ("green")
d.color ("green")
d.write("Dyson", False, 'left', ('Times new roman', 8, 'normal'))

a.setheading (a.towards (b))
b.setheading (b.towards (c))
c.setheading (c.towards (d))
d.setheading (d.towards (a))

print (a.towards (b))
print (b.towards (c))
print (c.towards (d))
print (d.towards (a))

distance = a.distance(b)
da = 0
db = 0
dc = 0
dd = 0
while distance > 0.1:
    step = 0.5
    if distance <= 10:
        print ("WE HAVE ENTERED THE IF")
        step = 0.1
    #a.write(distance, False, 'left', ('Times new roman', 8, 'normal'))
    a.forward (step)
    b.forward (step)
    c.forward(step)
    d.forward(step)
    da += step
    '''db += 10
    dc += 10
    dd += 10'''
    #print(da)

    a.setheading(a.towards(b))
    b.setheading(b.towards(c))
    c.setheading(c.towards(d))
    d.setheading(d.towards(a))
    distance = a.distance(b)
    print(distance)

print("The final distance is",da)

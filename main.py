import turtle
import random
okno= turtle.Screen()

BOK = 600
x=300
y=300
okno.setup(BOK,BOK)
okno.title("Tik Tak Toe")
okno.bgcolor("blue")
pen = turtle.Turtle()
pen.color("orange")
pen.pensize(7)
pen.speed(0)
pen.hideturtle()
tab =[[None,None,None],
[None,None,None],
[None,None,None]]

kolejka = random.choice(["X","O"]) 
odstep=int(BOK/3)

for a in [1,2]:
  pen.penup()
  pen.goto(x+a*odstep, y)
  pen.pendown()
  pen.goto(x+a*odstep, -y)
  pen.penup()
  pen.goto(x,y-a*odstep)
  pen.pendown()
  pen.goto(-x,y-a*odstep)

def clik(x,y):
  pass


okno.onclick(clik)
okno.listen()
okno.mainloop()
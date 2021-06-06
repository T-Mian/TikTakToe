import turtle
import random
import time

okno= turtle.Screen()

BOK = 600
x=300
y=300

okno.setup(BOK,BOK)
okno.title("Tik Tak Toe")
okno.bgcolor("blue")

pen = turtle.Turtle()
pen.color("orange")
pen.pensize(4)
pen.speed(0)
pen.hideturtle()

tab =[[None,None,None],
[None,None,None],
[None,None,None]]

kolejka = random.choice(["X","O"]) 
ODSTEP = int(BOK/3)

for a in [1,2]:
  pen.penup()
  pen.goto(x+ a* ODSTEP, y)
  pen.pendown()
  pen.goto(x+ a * ODSTEP, -y)
  pen.penup()
  pen.goto(x, y-a*ODSTEP)
  pen.pendown()
  pen.goto(-x, y-a* ODSTEP)

def sprawdzam():
  #po skosie
  if tab[0][0]==tab[1][1]==tab[2][2]: return tab[2][2]
  if tab[0][2]==tab[1][1]==tab[2][0]: return tab[2][0]
  # wiersze
  for w in range(2):
    if tab[w][0]==tab[w][1]==tab[2][0]: return tab[w][2]
  
  # kolumny
  for k in range(2):
    if tab[0][k]==tab[1][k]==tab[2][k]: return tab[2][k]

def clik(z,v):
  global kolejka
  kolumna= 0
  wiersz= 0 

  if z< x + ODSTEP: kolumna =0
  elif z>x + ODSTEP : kolumna = 2
  else : kolumna =1
  
  if v< y - 2 * ODSTEP : wiersz=2
  elif v > y - ODSTEP : wiersz =0
  else: wiersz= 1

  print(wiersz,kolumna)

  if tab [wiersz][kolumna] != None: return


  kolumna_centrum = (kolumna*ODSTEP + ODSTEP/2)-BOK/2
  wiersz_centrum = (-wiersz*ODSTEP -ODSTEP/2) + BOK/2

  pen.penup()
  pen.goto(kolumna_centrum-25,wiersz_centrum-25)
  if kolejka=="X": pen.write("X", font=("Arial",50) )
  else : pen.write("O", font=("Arial",50) )

  tab[wiersz][kolumna]=kolejka
  if kolejka =="O":
    kolejka="X"
  else: kolejka= "O"

  if sprawdzam()!=None:
    pen.penup()
    pen.goto(-150,0)
    pen.clear()
    time.sleep(1)
  if sprawdzam()!=None:
    pen.write("Wygrały : "+sprawdzam(), font=("Arial",100))
    


okno.onclick(clik)
okno.listen()
okno.mainloop()
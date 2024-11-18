from cs1graphics import*

#ICELAND
IL=Canvas(800,600,"sky blue","ICELAND")

#LAND

R=Rectangle(800,100)
R.setFillColor("white")
R.moveTo(400,550)
R.setDepth(100)
IL.add(R)


peng= Layer()


W1=Ellipse(120,90)
W1.setFillColor("black")
W1.moveTo(600,450)
W1.rotate(90)
W1.scale(1.5)

peng.add(W1)


w2= W1.clone()
w2.setFillColor("white")
w2.scale(0.5)
w2.setDepth(-100)
w2.moveTo(600,480)
peng.add(w2)


##EYE

e= Circle(10, Point(580, 400))
e.setFillColor("white")
peng.add(e)

e2= e.clone()
e2.moveTo(620, 400)
peng.add(e2)

e3=Circle(5, Point(580,400))
e3.setFillColor("black")
peng.add(e3)

e4= e3.clone()
e4.moveTo(620, 400)
peng.add(e4)

##NOSE

n= Polygon(Point(50, 50), Point(70,50),Point(60,60))
n.setFillColor("yellow")
n.moveTo(590, 410)
n.setDepth(-100)
peng.add(n)

##############RIVAN
r= n.clone()
r.setFillColor("red")
r.rotate(90)
r.moveTo(610,425)
peng.add(r)

r2= r.clone()
r2.rotate(180)
r2.moveTo(590,445)
peng.add(r2)

#####HAND
W4=Ellipse(120,50)
W4.setFillColor("black")
W4.moveTo(530,450)
W4.rotate(110)
W4.scale(0.5)
peng.add(W4)

h= W4.clone()
h.rotate(120)
h.moveTo(670,450)
peng.add(h)


#LEG

l=W4.clone()
l.setFillColor("yellow")
l.moveTo(570,520)
l.rotate(60)
l.setDepth(90)
peng.add(l)

l2=W4.clone()
l2.setFillColor("yellow")
l2.moveTo(630,520)
l2.rotate(-95)
l2.setDepth(90)
peng.add(l2)

IL.add(peng)

for i in range(500):
    peng.move(-1, 0)
for i in range(400):
    peng.move(1, 0)

               

import math
print("enter how many benches u want!")
n=int(input())
l=[]
d=[]
a=[]
for k in range(n):
    print(f"enter length, width and angle from horizontal in degrees of bench number {k+1} ")
    l.append(float(input()))
    d.append(float(input()))
    a.append(float(input()))
print("Enter the length of the fault from the first bench")
l1 = float(input())

print("Enter the angle of the fault with horizontal")
angle_1 = float(input())


print("Enter the Density of the material")
d1 = float(input())
print("Enter the cohesive factor of the benches")
c = float(input())
print("Enter the angle of friction")
angle_2 = float(input())

angle1 = (angle_1*3.141592654)/180
angle2 = (angle_2*3.141592654)/180
print(angle1)
print(angle2)


import turtle
wn= turtle.Screen()
wn.bgcolor("white")
t=turtle.Turtle()
t.color("black")
x=[[]]
y=[[]]

xf=[[]]
yf=[[]]

wid=0
dep=0
sum=0
fdbkx=[]
fdbky=[]
turtle.left(180)
for pl in range(n):
    if pl>=1:
        x[pl].append(fdbkx[pl-1])
        y[pl].append(fdbky[pl-1])
    else:
        x[pl].append(turtle.xcor())
        y[pl].append(turtle.ycor())

    if angle_1!=90:
        xf[pl].append(   (y[pl][0]-(math.tan((3.14*(180-angle_1))/180))*(l[0]-l1))/(math.tan((3.14*(180-angle_1))/180)))
        yf[pl].append(y[pl][0])
    else:
        xf[pl].append(-(l[0]-l1))
        yf[pl].append(y[pl][0])
    #turtle.left(180)
    turtle.forward(l[pl])
    turtle.left(180-a[pl])

    x[pl].append(turtle.xcor())
    y[pl].append(turtle.ycor())

    xf[pl].append(turtle.xcor())
    yf[pl].append(turtle.ycor())

    if a[pl]!=90:
        turtle.forward(d[pl]/(math.cos((3.14*(a[pl]-90))/180)))
    else:
        turtle.forward(d[pl])
    turtle.left(a[pl])
    x[pl].append(turtle.xcor())
    y[pl].append(turtle.ycor())

    xf[pl].append(turtle.xcor())
    yf[pl].append(turtle.ycor())


    if a[pl]!=90:
        turtle.forward(l[pl]+(d[pl]*(math.tan((3.14*(a[pl]-90))/180))))
    else:
        turtle.forward(l[pl])


    if pl>=1:
        turtle.pendown()
        turtle.goto(x[0][0],y[pl-1][3]-d[pl])

    x[pl].append(turtle.xcor())
    y[pl].append(turtle.ycor())

    fdbkx.append(turtle.xcor())
    fdbky.append(turtle.ycor())

    if angle_1!=90:
        xf[pl].append((y[pl][2]-(math.tan((3.14*(180-angle_1))/180))*(l[0]-l1))/(math.tan((3.14*(180-angle_1))/180)))
        yf[pl].append(y[pl][2])
    else:
        xf[pl].append(-(l[0]-l1))
        yf[pl].append(y[pl][2])
    turtle.left(180)

    x[pl].append(x[pl][0])
    y[pl].append(y[pl][0])

    xf[pl].append(xf[pl][0])
    yf[pl].append(yf[pl][0])

    if a[pl]!=90:
        turtle.pendown()
        turtle.goto(x[pl][2],y[pl][2])

    else:
        turtle.pendown()
        turtle.goto(x[pl][2],y[pl][2])

    turtle.end_fill()

    area=0
    m=len(x[pl])-1
    i1=0
    #print(len(x[pl]))
    while m:
        area=area+((x[pl][i1]*y[pl][i1+1]-x[pl][i1+1]*y[pl][i1])/2)
        i1+=1
        m-=1
    area=abs(area)
    print(area)

    x.append([])
    y.append([])


    areaf=0
    mf=len(xf[pl])-1
    i1f=0
    #print(len(x[pl]))
    while mf:
        areaf=areaf+((xf[pl][i1f]*yf[pl][i1f+1]-xf[pl][i1f+1]*yf[pl][i1f])/2)
        i1f+=1
        mf-=1
    areaf=abs(areaf)
    sum=sum+areaf
    print(areaf,"    this is fault area")

    xf.append([])
    yf.append([])



    print('loop1 end')

turtle.done()

a=sum

w = 9.81*(l[0]-l1)*a #a is the area
FOS = ((c*a)+ w*(math.cos(angle1))*(math.tan(angle2)))/(w*(math.sin(angle1)))
print(FOS)
# print("Enter the length of the fault from the last bench")
# l2 = float(input())
# d1 = [l[0]-l1]#storing the coordinate in an array where l[0] is the length of first bench
# d2 = [l[n-1]-l2]#same applied here

# 期中大作业 崔若瑶 
# 化学与分子工程学院 学号：1800011755
import turtle
import math


a=math.pi
wn = turtle.Screen() 
wn.bgcolor("black")
turtle.setup(width=1.0,height=1.0)
sun= turtle.Turtle() 
sun.speed(0)
sun.penup()
sun.setpos(32,0)
sun.pendown()
sun.dot(35,"yellow")


venus = turtle.Turtle()
mercury = turtle.Turtle()
earth = turtle.Turtle()
mars = turtle.Turtle()
jupiter = turtle.Turtle()
saturn = turtle.Turtle()

def planets(name,color,pos,size):
	return(name.color(color),
		name.speed(0),
		name.turtlesize(size),
		name.shape("circle"),
		name.penup(), 
		name.setpos(pos,0),
		name.pendown())
    
planets(mercury,"purple",60,0.3)
planets(venus,"orange",113.7,0.9)
planets(earth,"blue",157.9,0.92)
planets(mars,"red",240.0,0.45)
planets(jupiter,"green",400,1)
planets(saturn,"brown",600,0.87)

# mercury venus earth mars 轨道比例与真实比例近似 
# 而jupiter和saturn若按照真实比例的话 画不下 所以并非为真实比例



def orbit(name,c,b,d):
	x =c *( math.cos( (d/250)*a ) )
	y =b *( math.sin( (d/250)*a ) )
	name.setpos(x,y)


for i in range (1000):
	orbit(mercury, 60, 50.75, 4.17*i)
	orbit(venus, 113.7, 109.1, 1.626*i)
	orbit(earth, 157.9, 154.6, i)
	orbit(mars,240.0,237.85, 0.532*i)
	orbit(jupiter,400,398.72, 0.0843*i)
	orbit(saturn,600, 599.15, 0.034*i)


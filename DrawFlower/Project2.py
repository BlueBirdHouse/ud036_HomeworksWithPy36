import turtle

def Quadrilateral(Brad):
    Brad.forward(100)
    Brad.left(30)
    Brad.forward(100)
    Brad.left(150)
    Brad.forward(100)
    Brad.left(30)
    Brad.forward(100)
    Brad.left(150)

def Square(Brad):
    for i in range(4):
        Brad.forward(100)
        Brad.left(90)


#配置屏幕
Window = turtle.Screen()
Window.bgcolor("red")

#配置画笔
Brad = turtle.Turtle()
Brad.shape("turtle")
Brad.color("green")
Brad.speed(2)

#画出来一朵花
for i in range(24):
    Quadrilateral(Brad)
    Brad.left(15)

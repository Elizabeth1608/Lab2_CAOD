import turtle
import random

def tree(branchLen, t):
    if branchLen > 5:
        #толщина
        t.pensize(branchLen / 10)
        
        #цвет
        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")
        
        t.forward(branchLen)
        
        #случайный угол
        angle = random.randint(15, 45)
        t.right(angle)
        
        #случайное уменьшение
        tree(branchLen - random.randint(5, 15), t)
        
        t.left(angle * 2)
        tree(branchLen - random.randint(5, 15), t)
        
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.bgcolor("lightblue")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(0)
    tree(75, t)
    myWin.exitonclick()

main()
import turtle
import random

def draw_mountain(p1, p2, depth, t):
    if depth == 0:
        t.penup()
        t.goto(p1[0], p1[1])
        t.pendown()
        t.goto(p2[0], p2[1])
        return
    
    mid_x = (p1[0] + p2[0]) / 2
    mid_y = (p1[1] + p2[1]) / 2
    offset = random.randint(20, 80) * (depth / 6)
    mid_y += offset
    
    draw_mountain(p1, (mid_x, mid_y), depth - 1, t)
    draw_mountain((mid_x, mid_y), p2, depth - 1, t)

def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("Фрактальные горы")
    screen.bgcolor("lightblue")
    screen.setup(width=800, height=600)
    t.speed(0)
    t.hideturtle()
    t.pencolor("black")
    
    start = (-350, -200)
    end = (350, -200)
    
    draw_mountain(start, end, 6, t)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
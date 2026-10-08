import turtle

def draw_triangle(points, color, t):
    """Вспомогательная функция: рисует залитый треугольник по трём точкам."""
    t.fillcolor(color)
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def get_mid(p1, p2):
    """Находит середину между двумя точками."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, t):
    """Рекурсивная функция построения треугольника Серпинского."""
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    
    draw_triangle(points, colormap[degree], t)
    
    if degree > 0:
        mid1 = get_mid(points[0], points[1])
        mid2 = get_mid(points[1], points[2])
        mid3 = get_mid(points[2], points[0])
        
        sierpinski([points[0], mid1, mid3], degree - 1, t)
        sierpinski([mid1, points[1], mid2], degree - 1, t)
        sierpinski([mid3, mid2, points[2]], degree - 1, t)

def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("Треугольник Серпинского")
    t.speed(0)
    t.hideturtle()
    
    my_points = [[-200, -100], [0, 200], [200, -100]]
    sierpinski(my_points, 4, t)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
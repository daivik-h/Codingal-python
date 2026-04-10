import turtle

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")
car = turtle.Turtle()
car.speed(3)

def draw_car():
    # 1. Draw the main rectangular body
    car.penup()
    car.goto(-100, 0)
    car.pendown()
    car.color("blue")
    car.begin_fill()
    for _ in range(2):
        car.forward(200)
        car.left(90)
        car.forward(50)
        car.left(90)
    car.end_fill()

    # 2. Draw the roof (cabin)
    car.penup()
    car.goto(-60, 50)
    car.pendown()
    car.color("lightblue")
    car.begin_fill()
    car.goto(-30, 90)
    car.goto(30, 90)
    car.goto(60, 50)
    car.goto(-60, 50)
    car.end_fill()

    # 3. Draw the wheels
    def draw_wheel(x, y):
        car.penup()
        car.goto(x, y)
        car.setheading(0)
        car.pendown()
        car.color("black")
        car.begin_fill()
        car.circle(20)
        car.end_fill()

    draw_wheel(-60, -20)
    draw_wheel(60, -20)

    # Hide turtle and keep window open
    car.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_car()

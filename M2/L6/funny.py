

import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(3)

colors = ["red", "yellow", "lime", "cyan", "magenta", "white"]

# Normal square... or is it?
for i in range(4):
    t.forward(100)
    t.right(90)

time.sleep(1)

# Suddenly... chaos mode
t.clear()
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(200):
    t.color(random.choice(colors))
    t.forward(random.randint(10, 100))
    t.right(random.randint(0, 360))

# Wait a bit
time.sleep(1)

# Then... it ESCAPES 😳
t.penup()
for i in range(100):
    t.goto(random.randint(-300, 300), random.randint(-300, 300))

# Final message
t.goto(0, 0)
t.color("white")
t.write("I AM FREE 🐢", align="center", font=("Arial", 24, "bold"))

turtle.done()
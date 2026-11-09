import math
import turtle

def draw_tree(pen, length, level):
    if level == 0:
        return

    pen.forward(length)

    child_length = length / math.sqrt(2)

    pen.left(45)
    draw_tree(pen, child_length, level - 1)

    pen.right(90)
    draw_tree(pen, child_length, level - 1)

    pen.left(45)
    pen.backward(length)    

def main():
    try:
        level = int(input("Enter the level of the tree (from 1 to 12): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if not 1 <= level <= 12:
        print("Level out of range. Please enter a value between 1 and 12.")
        return

    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.title(f"Fractal Tree - level {level}")
    screen.tracer(0)
    
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pencolor("firebrick")
    pen.pensize(1)
    pen.penup()
    pen.goto(0, -300)
    pen.setheading(90)
    pen.pendown()

    draw_tree(pen, 150, level)

    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()
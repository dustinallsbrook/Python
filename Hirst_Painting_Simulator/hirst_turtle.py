import turtle as t
import random
import colorgram


# Generate colors for turtle to paint
colors = colorgram.extract('image.jpg', 20)
color_list = []
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    color = (r, g, b)
    color_list.append(color)

# # Pre-made color list
# color_list = [(223, 221, 228), (218, 173, 125), (159, 181, 190), (134, 73, 53), (50, 103, 154),
#               (118, 81, 92), (179, 142, 152), (162, 104, 151), (42, 47, 66), (128, 174, 115),
#               (83, 96, 183), (67, 9, 27), (82, 133, 107), (52, 63, 78), (228, 189, 141),
#               (194, 91, 72), (220, 226, 221), (62, 49, 38)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
tim.goto(-200, -200)


def mov_fwd():
    for _ in range(10):
        tim.dot(20,random.choice(color_list))
        tim.fd(40)


def turn_left():
    tim.color(random.choice(color_list))
    tim.dot(20)
    tim.left(90)
    tim.fd(40)
    tim.left(90)


def turn_right():
    tim.color(random.choice(color_list))
    tim.dot(20)
    tim.right(90)
    tim.fd(40)
    tim.right(90)


def main():
    for _ in range(5):
        mov_fwd()
        turn_left()
        mov_fwd()
        turn_right()


main()

screen = t.Screen()
screen.exitonclick()

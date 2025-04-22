###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_add = (r,g,b)
#     rgb_colors.append(color_add)

import turtle as t
import random

hirst_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
picasso = t.Turtle()
picasso.speed("fastest")
picasso.shape("turtle")
picasso.penup()
t.colormode(255)



def draw_hirst(canvas_size):
    picasso.setheading(225)
    picasso.forward(500)
    picasso.setheading(180)
    picasso.forward(100)
    picasso.setheading(0)
    for _ in range(canvas_size):
        for _ in range(canvas_size):
            picasso.dot(20,random.choice(hirst_colors))
            picasso.forward(50)
        picasso.left(90)
        picasso.forward(30)
        picasso.left(90)
        picasso.forward(50*canvas_size)
        picasso.right(180)

#Start picasso on bottom left

draw_hirst(20)



screen = t.Screen()
screen.exitonclick()

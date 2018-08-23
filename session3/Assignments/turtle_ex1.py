from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

step = 100

for i in range(len(colors)):
    pencolor(colors[i])

    for _ in range(i + 3):

        forward(step)
        angle = ((i + 1) * 180) / (i + 3)
        left(180 - angle)

mainloop()
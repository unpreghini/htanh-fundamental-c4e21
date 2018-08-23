from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
colors_size = len(colors)
vertical = 100
horizontal = 250

for i in range(colors_size - 1, -1, -1):
    
    color(colors[i])
    begin_fill()

    for _ in range(4):        
        if _ % 2:
            forward(vertical)
        else: 
            forward(horizontal)
        right(90)
        
    end_fill() 
    horizontal -= 50
      

mainloop()
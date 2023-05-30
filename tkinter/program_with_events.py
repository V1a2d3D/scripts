import tkinter
import random

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400, bg="black")
canvas.pack()
colors = ("DarkOrchid1", "DarkSeaGreen3", "DarkTurquoise", "DeepPink",
          "firebrick1", "DarkOliveGreen2", "DarkRed", "grey", "DarkSlateBlue")


def my_click(event):
    radius = random.randint(10, 50)
    canvas.create_oval(event.x - radius, event.y - radius,
                       event.x + radius, event.y + radius, fill=random.choice(colors))
    print(event)


canvas.bind('<Button-1>', my_click)
window.mainloop()

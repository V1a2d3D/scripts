import tkinter
import random
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400, bg="black")
canvas.pack()

circles = []
colors = ("DarkOrchid1", "DarkSeaGreen3", "DarkTurquoise", "DeepPink",
          "firebrick1", "DarkOliveGreen2", "DarkRed", "grey", "DarkSlateBlue")


for another_circle in range(15):
    circle = {}
    radius = random.randint(10, 40)
    coordinate_x = random.randint(40, 360)
    coordinate_y = random.randint(40, 360)
    circle["dx"] = random.randint(-10, 10)
    circle["dy"] = random.randint(-10, 10)
    circle["id"] = canvas.create_oval(
        coordinate_x - radius, coordinate_y - radius,
        coordinate_x + radius, coordinate_y + radius,
        fill=random.choice(colors))
    circles.append(circle)

while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])

        if x0 <= 0 or x1 >= 400:
            circle["dx"] = - circle["dx"]
        if y0 <= 0 or y1 >= 400:
            circle["dy"] = - circle["dy"]

        canvas.move(circle["id"], circle["dx"], circle["dy"])
    time.sleep(0.04)
    canvas.update()

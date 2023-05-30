import time
import tkinter
import random

colors = ('green', 'light sea green', 'light coral',
          'SlateGray4', 'CadetBlue3', 'medium purple', 'orange')

c_of_laps = 0

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400, bg='white')
canvas.pack()

x = random.randint(0, 400)
y = random.randint(0, 400)

while c_of_laps != 8:
    x0 = x - 150
    y0 = y - 150
    x1 = x + 150
    y1 = y + 150
    for e, l in enumerate(range(x1, x1 + 31, 5)):
        canvas.create_oval(x0, y0, x1, y1, outline=colors[e])
        canvas.update()
        time.sleep(0.10)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
        if c_of_laps == 7:
            canvas.delete('all')
            c_of_laps = 0
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    c_of_laps += 1
    c_of_colors = 0

window.mainloop()

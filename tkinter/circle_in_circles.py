import tkinter
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
x0 = 150
y0 = 95
x1 = 160
y1 = 105

for digit in range(90, 181, 5):
    if digit % 2 == 0:
        canvas.create_oval(x0, y0, x1, y1, outline="grey")
        canvas.update()
        time.sleep(0.05)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
    else:
        canvas.create_oval(x0, y0, x1, y1, outline="red")
        canvas.update()
        time.sleep(0.05)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

window.mainloop()
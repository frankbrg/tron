
import tkinter
from tkinter import messagebox
import time

__WIDTH = 800
__HEIGHT = 800

rectangleX = 10
rectangleY = 100
rectangleSize = 4
stepX = 5
stepY = 0

def bounceX(event=0):
    global stepX
    stepX *= -1

def bounceY(event=0):
    global stepY
    stepY *= -1

def up(event=0):
    global stepX
    global stepY
    stepY = -5
    stepX = 0

def down(event=0):
    global stepX
    global stepY
    stepY = 5
    stepX = 0

def left(event=0):
    global stepX
    global stepY
    stepY = 0
    stepX = -5

def right(event=0):
    global stepX
    global stepY
    stepY = 0
    stepX = 5

window = tkinter.Tk()
window.title('Coucou')
window.geometry(str(__WIDTH) + 'x' + str(__HEIGHT))

canvas = tkinter.Canvas(window)
canvas.pack(fill='both', expand='True')
canvas.configure(bg='black')




window.bind('<KeyPress-Left>', left)
window.bind('<KeyPress-Down>', down)
window.bind('<KeyPress-Up>', up)
window.bind('<KeyPress-Right>', right)
gameProgress = True

while gameProgress:
    rectangleX += stepX
    rectangleY += stepY

    elements = canvas.find_overlapping(rectangleX, rectangleY, rectangleX + rectangleSize, rectangleY + rectangleSize)

    for element in elements:
        if canvas.itemcget(element, 'fill') == 'red':
            messagebox.showinfo('Crash', 'End !')
            gameProgress = False

    canvas.create_rectangle(rectangleX, rectangleY, rectangleX + rectangleSize, rectangleY + rectangleSize, fill='red', outline='red')
    
    if rectangleX <= 0 :
        rectangleX = __WIDTH - 1

    if rectangleX >= __WIDTH:
        rectangleX = 0

    if rectangleY <= 0 :
        rectangleY = __HEIGHT - 1

    if rectangleY >= __HEIGHT:
        rectangleY = 0

    window.update()

    time.sleep(0.02)

window.mainloop()
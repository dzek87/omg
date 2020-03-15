from tkinter import *

x = [1,2]
y = [1,2]
a = False

def test(event):
    global x
    global y
    global a
    if a == False:
        x[0] = event.x
        y[0] = event.y
        a = True
        print("a test")
    else:
        x[1] = event.x
        y[1] = event.y
        paint_line(event,x[0],y[0],x[1],y[1])
        a = False
        print("b test")
def line(event):
    global x
    global y
    global a
    if a == False:
        x[0] = event.x
        y[0] = event.y
        #print("a")
        #a == True
    else:
        x[1] = event.x
        y[1] = event.y
        #print("b")
        #a = False
def paint_line(event,x1,y1,x2,y2):
    canvas.create_line(x1,y1,x2,y2,fill = "black")
    canvas.create_oval(x1-3,y1-3,x1+3,y1+3, fill = "black")
    canvas.create_oval(x2-3,y2-3,x2+3,y2+3, fill = "black")
 
window = Tk()

canvas = Canvas(window,width = 500, height = 500, bg = "white")
canvas.bind("<Button-1>", test)
canvas.pack()
window.mainloop()


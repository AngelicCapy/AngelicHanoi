from tkinter import Canvas
import tkinter as tk
from time import sleep
# Create the windowmain 
root = tk.Tk()
root.title("Tour De Hanoi")
height = 600
width = 800
root.geometry(f"{width}x{height}")
NbrDeDisque = tk.Entry(root)
button = tk.Button(root, text="Click me")
cnv=tk.Canvas(root, width=width, height=height, bg="#111111")
cnv.create_rectangle(150,height,200,50,fill="#6D4714")
cnv.create_rectangle(width//2-25,height,width//2+25,50,fill="#6D4714")
cnv.create_rectangle(width-200,height,width-150,50,fill="#6D4714")
NbrDeDisque.pack()
button.pack()

def boutonNbrDeDisque():
    button.pack_forget()
    NbrDeDisque.pack_forget()
    cnv.pack()
    return main(int(NbrDeDisque.get()))

button.config(command=boutonNbrDeDisque)

def main(disque):
    t1 = [i for i in range(1,disque+1)]
    t2 = []
    t3 = []
    def hanoi_liste(n, depart, arrivee, intermediaire):
        [cnv.create_rectangle(125+(i*2),height-50*t1.index(i),225-(i*2),height-50*(t1.index(i)+1)+2,fill="red") for i in t1]
        [cnv.create_rectangle(350+(i*2),height-50*t3.index(i),450-(i*2),height-50*(t3.index(i)+1)+2,fill="red") for i in t3]
        [cnv.create_rectangle(575+(i*2),height-50*t2.index(i),675-(i*2),height-50*(t2.index(i)+1)+2,fill="red") for i in t2]
        cnv.update()
        sleep(0.5)
        cnv.delete("all")
        cnv.create_rectangle(150,height,200,50,fill="#6D4714")
        cnv.create_rectangle(width//2-25,height,width//2+25,50,fill="#6D4714")
        cnv.create_rectangle(width-200,height,width-150,50,fill="#6D4714")
        if n == 1:
            arrivee.append(depart.pop())
        else:
            hanoi_liste(n-1, depart, intermediaire, arrivee)
            hanoi_liste(1, depart, arrivee, intermediaire)
            hanoi_liste(n-1, intermediaire, arrivee, depart)

    hanoi_liste(disque, t1, t2, t3)
    [cnv.create_rectangle(575+(i*2),height-50*t2.index(i),675-(i*2),height-50*(t2.index(i)+1)+2,fill="red") for i in t2]
    cnv.update()

root.mainloop()




import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def lahenda_võrrand():
    try:
        a = float(sisse1.get())
        b = float(sisse2.get())
        c = float(sisse3.get())
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + np.sqrt(D)) / (2*a)
            x2 = (-b - np.sqrt(D)) / (2*a)
            result_label.config(text=f"Lahendus: x1 = {x1:.2f}, x2 = {x2:.2f}", fg='green')
        elif D == 0:
            x = -b / (2*a)
            result_label.config(text=f"Lahendus: x = {x:.2f}", fg='green')
        else:
            result_label.config(text="Pole reaalseid lahendusi.", fg='green')
    except:
        result_label.config(text="Sisesta õiged väärtused.", fg='red')

def joonista_graafik():
    try:
        a = float(sisse1.get())
        b = float(sisse2.get())
        c = float(sisse3.get())

        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='green')
        plt.axhline(0, color='black', linewidth=1)
        plt.title('Graafik: Ruutvõrrandi f(x)')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError:
        result_label.config(text="Sisesta õiged väärtused.", fg='red')

aken = Tk()
aken.title('Ruutvõrrandi lahendamine')
aken.geometry('500x400')
aken.configure(bg='lightgrey')
pealkiri = Label(aken, text='Ruutvõrrandi lahendamine', bg='lightblue', font=('Arial', 16), fg='green')
pealkiri.place(x=120, y=20)

sisse1 = Entry(aken, font=("Arial", 15), bg="lightblue", fg="green", width=4)
sisse1.place(x=10, y=100)
kiri1 = Label(aken, text="x² +", font=("Arial", 15), bg="lightgrey", fg="green")
kiri1.place(x=60, y=100)
sisse2 = Entry(aken, font=("Arial", 15), bg="lightblue", fg="green", width=4)
sisse2.place(x=100, y=100)
kiri2 = Label(aken, text="x +", font=("Arial", 15), bg="lightgrey", fg="green")
kiri2.place(x=160, y=100)
sisse3 = Entry(aken, font=("Arial", 15), bg="lightblue", fg="green", width=4)
sisse3.place(x=200, y=100)
kiri3 = Label(aken, text="= 0", font=("Arial", 15), bg="lightgrey", fg="green")
kiri3.place(x=260, y=100)
sisse4 = Button(aken, text="Lahenda", font=("Arial", 15), bg="darkgreen", fg="white", relief="raised", width=10, command=lahenda_võrrand)
sisse4.place(x=320, y=90)

result_label = Label(aken, text="= ?", font=("Arial", 15), bg="lightyellow", fg="green")

result_label.place(x=100, y=200)

sisse5 = Button(aken, text="Joonista graafik", font=("Arial", 15), bg="darkgreen", fg="white", relief="raised", width=15, command=joonista_graafik)
sisse5.place(x=320, y=150)


aken.mainloop()

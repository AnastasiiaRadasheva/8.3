import smtplib
import ssl
from email.message import EmailMessage
from tkinter import *
from tkinter import filedialog, messagebox
import random
from epost_module1 import *


aken = Tk()
aken.title('e-kirja saatmine')
aken.geometry('650x550')
aken.configure(bg='lightgrey')

pealkiri = Label(aken, text='E-KIRI', font=("Showcard Gothic", 20), bg='lightgrey')
pealkiri.place(x=225, y=15)

Label(aken, text="EMAIL:", font=("Showcard Gothic", 18), bg="darkred", fg="white").place(x=15, y=60)
Label(aken, text="TEEMA:", font=("Showcard Gothic", 18), bg="darkred", fg="white").place(x=15, y=100)
Label(aken, text="LISA:", font=("Showcard Gothic", 18), bg="darkred", fg="white").place(x=15, y=140)
Label(aken, text="KIRI:", font=("Showcard Gothic", 18), bg="darkred", fg="white").place(x=15, y=250)
sisse1 = Entry(aken, font=("Showcard Gothic", 18), bg="lightgrey", fg="white", width=20)
sisse1.place(x=135, y=60)
sisse2 = Entry(aken, font=("Showcard Gothic", 18), bg="lightgrey", fg="white", width=20)
sisse2.place(x=135, y=100)
tekstikast = Text(aken, height=4, width=35, font=("Showcard Gothic", 14), bg="lightgrey", fg="white")
tekstikast.place(x=135, y=200)
l_lisatud = Label(aken, text="", font=("Showcard Gothic", 10), bg="lightgrey", fg="white")
l_lisatud.place(x=135, y=140)

Button(aken, text="LISA PILT", command=vali_pilt, font=("Showcard Gothic", 14), bg="darkred", fg="white").place(x=135, y=375)
Button(aken, text="SAADA", command=saada_kiri, font=("Showcard Gothic", 14), bg="darkred", fg="white").place(x=255, y=375)
Button(aken, text="UUS TEMMA", command=teema, font=("Showcard Gothic", 14), bg="darkred", fg="white").place(x=345, y=375)
Button(aken, text="SAVE TO FILE", command=forms, font=("Showcard Gothic", 14), bg="lightgrey", fg="white").place(x=135, y=300)
Button(aken, text="PUHASTA VORM", command=clear_form, font=("Showcard Gothic", 14), bg="lightgrey", fg="white").place(x=135, y=450)
Button(aken, text="ОТКРЫТЬ ФАЙЛ", command=open_file, font=("Showcard Gothic", 14), bg="lightgrey", fg="white").place(x=255, y=450)
aken.mainloop()

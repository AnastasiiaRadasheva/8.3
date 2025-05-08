import smtplib
import ssl
from email.message import EmailMessage
from tkinter import *
from tkinter import filedialog, messagebox
import random

thems_fail = 'thems.txt'

def save(kellele, teema, kiri, file_name=None):
    with open(thems_fail, "a", encoding="utf-8") as f:
        f.write(f'e post: {kellele} teema: {teema} Kiri: {kiri}\n')
        if file_name:
            f.write(f'Attachment: {file_name}\n')
    print("Email saved to file.")

def forms():
    kellele = sisse1.get()
    teema = sisse2.get()
    kiri = tekstikast.get("1.0", END).strip()
    save(kellele, teema, kiri)

file = None  

def vali_pilt():
    global file
    file = filedialog.askopenfilename(title='Vali fail', filetypes=[('Kõik failid', '*.*')])
    l_lisatud.configure(text=file)
    return file

def saada_kiri():
    kellele = sisse1.get()
    teema = sisse2.get()
    kiri = tekstikast.get("1.0", END).strip()
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    kellelt = 'eha20082@gmail.com'
    salasõna = 'pjuj tvvc ogta dxkb'  

    msg = EmailMessage()
    msg['Subject'] = teema
    msg['From'] = kellelt
    msg['To'] = kellele

    text_sisu = kiri
    html_sisu = f"""\
    <html>
      <body>
        <h1 style="color:#ff0000;">{teema}</h1>
        <p>{kiri}</p>
      </body>
    </html>
    """
    msg.set_content(text_sisu)
    msg.add_alternative(html_sisu, subtype='html')

    attachment_name = None
    if file:
        try:
            with open(file, 'rb') as f:
                file_data = f.read()
                attachment_name = f.name.split('/')[-1]
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=attachment_name)
        except Exception as e:
            messagebox.showerror("Faili viga", f"Manuse lisamine ebaõnnestus:\n{e}")
            return

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(kellelt, salasõna)
            server.send_message(msg)
        messagebox.showinfo("Edukalt saadetud", "Kiri on saadetud!")
    except Exception as e:
        messagebox.showerror("Viga", f"Kiri saatmine ebaõnnestus:\n{e}")


teemad = ['grey', 'darkgrey', 'darkred', 'darkblue', 'green', 'black', 'darkgreen', 'lightyellow', 'lightblue', 'lightgreen']

def teema():
    selected_theme = random.choice(teemad)
    selected_fg = random.choice(teemad)
    aken.configure(bg=selected_theme)  
    pealkiri.configure(bg=selected_theme)  
    while True:
        if selected_theme == selected_fg:
            selected_fg = random.choice(teemad)
        else:
            Label(aken, text="EMAIL:", font=("Showcard Gothic", 18), bg=selected_theme, fg=selected_fg).place(x=15, y=60)
            Label(aken, text="TEEMA:", font=("Showcard Gothic", 18), bg=selected_theme, fg=selected_fg).place(x=15, y=100)
            Label(aken, text="LISA:", font=("Showcard Gothic", 18), bg=selected_theme, fg=selected_fg).place(x=15, y=140)
            Label(aken, text="KIRI:", font=("Showcard Gothic", 18), bg=selected_theme, fg=selected_fg).place(x=15, y=250)
            l_lisatud = Label(aken, text="", font=("Showcard Gothic", 10), bg=selected_theme, fg=selected_fg)
            l_lisatud.place(x=135, y=140)

            Button(aken, text="LISA PILT", command=vali_pilt, font=("Showcard Gothic", 14), bg=selected_theme, fg=selected_fg).place(x=135, y=375)
            Button(aken, text="SAADA", command=saada_kiri, font=("Showcard Gothic", 14), bg=selected_theme, fg=selected_fg).place(x=255, y=375)
            Button(aken, text="UUS TEMMA", command=teema, font=("Showcard Gothic", 14), bg=selected_theme, fg=selected_fg).place(x=345, y=375)
            break


def clear_form():
    sisse1.delete(0, END)
    sisse2.delete(0, END)
    tekstikast.delete("1.0", END)
    l_lisatud.configure(text="")
    global file
    file = None



def open_file():
    try:
        with open(thems_fail, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        file_window = Toplevel(aken)
        file_window.title("Thems")
        file_window.geometry("600x400")
        text_box = Text(file_window, wrap=WORD, width=70, height=20, font=("Showcard Gothic", 12))
        text_box.pack(padx=10, pady=10)
        text_box.insert(END, file_content)  
        text_box.config(state=DISABLED)  

    except :
        print("Viga ")






























aken = Tk()
aken.title('e-kirja saatmine')
aken.geometry('650x510')
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
Button(aken, text="SALVESTA MUSTAND", command=forms, font=("Showcard Gothic", 14), bg="lightgrey", fg="white").place(x=135, y=300)
Button(aken, text="PUHASTA KÕIK", command=clear_form, font=("Showcard Gothic", 14), bg="lightgrey", fg="white").place(x=480, y=300)
Button(aken, text="MUSTANDS", command=open_file, font=("Showcard Gothic", 14), bg="lightgrey", fg="white").place(x=350, y=300)





aken.mainloop()

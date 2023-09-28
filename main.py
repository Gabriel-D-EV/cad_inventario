from tkinter import *
from tkinter import Tk, StringVar
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date



#Cores

co0 = '#6A5ACD' #roxo medio
co1 = '#D8CEF6' #roxo claro
co2 = '#483D8B' #roxo escuro
co3 = '#000000' #preto
co4 = '#F8F8FF' #b ghost
co5 = '#191970' #azul
co6 = '#4B0082' #roxao
co7 = '#38576b' #valor
co8 = '#403d3d' #letra
co9 = '#e06636' #- profit

#janela

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#frames
frameh = Frame(janela, width=1045, height=50, bg=co4, relief=FLAT)
frameh.grid(row=0, column=0)

framem = Frame(janela, width=1045, height=310, bg=co1, pady=20, relief=FLAT)
framem.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

framef = Frame(janela, width=1045, height=300, bg=co1, relief=FLAT)
framef.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#FRAMEH
#imagem]
app_img = Image.open('imagens/list.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

logo = Label(frameh,image=app_img, text=' Inventário!', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Arial 20 bold'), bg=co4, fg=co3)
logo.place(x=0,y=0)

#FRAMEM
#inputs
#nome
lnome = Label(framem, text='Nome', height=1, anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co3)
lnome.place(x=12,y=10)

enome = Entry(framem, width=40, justify='left', relief=SOLID)
enome.place(x=100, y=12)

#descrição
ldesc = Label(framem, text='Descrição', height=1, anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co3)
ldesc.place(x=12,y=40)

edesc = Entry(framem, width=40, justify='left', relief=SOLID)
edesc.place(x=100, y=42)

#marca
lmarca = Label(framem, text='Marca', height=1, anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co3)
lmarca.place(x=12,y=70)

emarca = Entry(framem, width=40, justify='left', relief=SOLID)
emarca.place(x=100, y=72)

#data
ldata = Label(framem, text='Data', height=1, anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co3)
ldata.place(x=12,y=100)

edata = DateEntry(framem, width=15, Background=co1, bordewidth=2, year=2023)
edata.place(x=100, y=102)

#valor
lvalor = Label(framem, text='Valor', height=1, anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co3)
lvalor.place(x=12,y=130)

evalor = Entry(framem, width=40, justify='left', relief=SOLID)
evalor.place(x=100, y=132)

'''#imagem
lnome = Label(framem, text='Nome', height=1, anchor=NW, font=('Arial 10 bold'), bg=co4, fg=co3)
lnome.place(x=12,y=10)

enome = Entry(framem, width=40, justify='left', relief=SOLID)
enome.place(x=60, y=12)'''




janela.mainloop()


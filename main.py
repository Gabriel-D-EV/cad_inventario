from tkinter import *
from tkinter import Tk, StringVar
from tkinter import ttk
from PIL import Image, ImageTk



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

#imagem]
app_img = Image.open('imagens/list.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

logo = Label(frameh,image=app_img, text=' Inventário!', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Arial 20 bold'), bg=co4, fg=co3)
logo.place(x=0,y=0)

janela.mainloop()


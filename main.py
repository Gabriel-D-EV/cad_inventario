from tkinter import *
from tkinter import Tk, StringVar
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter import filedialog as fd

#import view
from view import *



#Cores

co0 = '#AB82FF' #roxo 1
co1 = '#8968CD' #roxo 2
co2 = '#5D478B' #roxo 3
co3 = '#000000' #preto
co4 = '#F8F8FF' #branco
co5 = '#4B0082' #roxao
co6 = '#48D1CC' #turqusa
co7 = '#403d3d' #letra
co8 = '#e06636' #- profit

#janela

janela = Tk()
janela.title('')
janela.iconbitmap('./imagens/favicon.ico')
janela.geometry('800x600')
janela.configure(background=co0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#frames
frameh = Frame(janela, width=1045, height=50, bg=co4, relief=FLAT)
frameh.grid(row=0, column=0)

framem = Frame(janela, width=1045, height=290, bg=co0, pady=20, relief=FLAT)
framem.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

framef = Frame(janela, width=1045, height=320, bg=co0, relief=FLAT)
framef.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#BACK-END
global tree
global img, img_str, l_img

#inserir
def inserir():
    global img, img_str, l_img

    nome = enome.get()
    desc = edesc.get()
    marca = emarca.get()
    data = edata.get()
    valor = evalor.get()
    img = img_str

    lst_inserir = [nome, desc, marca, data, valor, img]

    for i in lst_inserir:
        if i == '':
            messagebox.showerror('Erro','Preencha todos os campos')
            return

    inserir_form(lst_inserir)
    messagebox.showinfo('Sucesso','Dados inseridos')

    enome.delete(0,'end')
    edesc.delete(0,'end')
    emarca.delete(0,'end') 
    edata.delete(0,'end')
    evalor.delete(0,'end')
   
    mostrar()

#atualizar
def att():
    try:
        global img, img_str, l_img
        treevd = tree.focus()
        treevdic = tree.item(treevd)
        treevl = treevdic['values']

        valor = treevl[0]

        enome.delete(0,'end')
        edesc.delete(0,'end')
        emarca.delete(0,'end') 
        edata.delete(0,'end')
        evalor.delete(0,'end')

        id = int(treevl[0])

        enome.insert(0,treevl[1])
        edesc.insert(0,treevl[2])
        emarca.insert(0,treevl[3]) 
        edata.insert(0,treevl[4])
        evalor.insert(0,treevl[5])
        img_str = treevl[6]
        def up():
            global img, img_str, l_img

            nome = enome.get()
            desc = edesc.get()
            marca = emarca.get()
            data = edata.get()
            valor = evalor.get()
            img = img_str

            lst_att = [nome, desc, marca, data, valor, img, id]

            if img == '':
                img = evalor.insert(0,treevl[5])
            
            for i in lst_att:
                if i =='':
                    messagebox.showerror('ERRO!', 'Preencha todos os campos')
                    return
            att_form(lst_att)
            messagebox.showinfo('SUCESSO','Os dados foram atualizados')

            enome.delete(0,'end')
            edesc.delete(0,'end')
            emarca.delete(0,'end') 
            edata.delete(0,'end')
            evalor.delete(0,'end')

            bconf.destroy()

            mostrar()

        
        bconf = Button(framem, command=up, text='Confirmar', width=14, height=2, overrelief=RIDGE, font=('Arial 8 bold'), bg=co2, fg=co4)
        bconf.place(x=123,y=194)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados!')
#deletar
def deletar():
    try:
        
        treevd = tree.focus()
        treevdic = tree.item(treevd)
        treevl = treevdic['values']

        valor = treevl[0]

        del_form([valor])
        messagebox.showinfo('SUCESSO', 'Dados deletados')
        mostrar()
    except IndexError:
        messagebox.showerror('ERRO', 'Selecione um dos dados!')

#escolher img   
def escolher_img():
    global img, img_str, l_img

    img = fd.askopenfilename()
    img_str = img

    img = Image.open(img)
    img = img.resize((150,150))
    img = ImageTk.PhotoImage(img)
    
    l_img = Label(framem,image=img, bg=co0, fg=co3)
    l_img.place(x=615,y=10)
    treevd = tree.focus()
    treevdic = tree.item(treevd)
    treevl = treevdic['values']

#Ver item
def ver_img():
    global img, img_str, l_img


    treevd = tree.focus()
    treevdic = tree.item(treevd)
    treevl = treevdic['values']

    valor = [int(treevl[0])]
    item = ver_item(valor)
    img = item[0][6]

    img = Image.open(img)
    img = img.resize((150,150))
    img = ImageTk.PhotoImage(img)
    
    l_img = Label(framem,image=img, bg=co0, fg=co3)
    l_img.place(x=615,y=10)

#FRAMEH
#imagem
app_img = Image.open('imagens/list.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)
#imagem add att del
add_img = Image.open('imagens/add.png')
add_img = add_img.resize((20,20))
add_img = ImageTk.PhotoImage(add_img)

att_img = Image.open('imagens/att.png')
att_img = att_img.resize((20,20))
att_img = ImageTk.PhotoImage(att_img)

del_img = Image.open('imagens/del.png')
del_img = del_img.resize((20,20))
del_img = ImageTk.PhotoImage(del_img)


logo = Label(frameh,image=app_img, text=' Inventário!', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Arial 20 bold'), bg=co4, fg=co3)
logo.place(x=0,y=0)

#FRAMEM
#inputs
#nome
lnome = Label(framem, text='Nome:', height=1, anchor=NW, font=('Arial 10 bold'), bg=co0, fg=co3)
lnome.place(x=12,y=10)

enome = Entry(framem, width=40, justify='left', relief=SOLID)
enome.place(x=100, y=12)

#descrição
ldesc = Label(framem, text='Descrição:', height=1, anchor=NW, font=('Arial 10 bold'), bg=co0, fg=co3)
ldesc.place(x=12,y=40)

edesc = Entry(framem, width=40, justify='left', relief=SOLID)
edesc.place(x=100, y=42)

#marca
lmarca = Label(framem, text='Marca:', height=1, anchor=NW, font=('Arial 10 bold'), bg=co0, fg=co3)
lmarca.place(x=12,y=70)

emarca = Entry(framem, width=40, justify='left', relief=SOLID)
emarca.place(x=100, y=72)

#data
ldata = Label(framem, text='Data:', height=1, anchor=NW, font=('Arial 10 bold'), bg=co0, fg=co3)
ldata.place(x=12,y=100)

edata = DateEntry(framem, width=15, Background=co1, bordewidth=2, year=2023)
edata.place(x=100, y=102)

#valor
lvalor = Label(framem, text='Valor:', height=1, anchor=NW, font=('Arial 10 bold'), bg=co0, fg=co3)
lvalor.place(x=12,y=130)

evalor = Entry(framem, width=40, justify='left', relief=SOLID)
evalor.place(x=100, y=132)

#imagem botao
limg = Label(framem, text='Imagem:', height=1, anchor=NW, font=('Arial 10 bold'), bg=co0, fg=co3)
limg.place(x=12,y=160)

bimg = Button(framem, width=22, command=escolher_img, text='Carregar Imagem', height=1, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Arial 8 bold'), bg=co4, fg=co3)
bimg.place(x=100,y=162)

#botao adicionar
badd = Button(framem, command=inserir, image=add_img,text='   Adicionar', width=100,  height=32, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Arial 8 bold'), bg=co2, fg=co4)
badd.place(x=12,y=194)

#botao atualizar
batt = Button(framem, command=att, image=att_img, text='   Atualizar', width=100, height=32, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Arial 8 bold'), bg=co2, fg=co4)
batt.place(x=123,y=194)

#botao deletar
bdel = Button(framem, command=deletar, image=del_img, text='   Deletar', width=100, height=32, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Arial 8 bold'), bg=co2, fg=co4)
bdel.place(x=234,y=194)

#botao ver item
bvimg = Button(framem, command=ver_img, width=10, text='Ver Imagem', height=1, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Arial 8 bold'), bg=co1, fg=co3)
bvimg.place(x=264,y=162)

#Labels de quantidade e valores
#totv
ltotv = Label(framem, text='gg', width=13, height=2, anchor=CENTER, font=('Arial 18 bold'), bg=co6, fg=co2)
ltotv.place(x=380,y=30)

ltotv1 = Label(framem, text='   Valor Total dos Itens:             ', height=1, anchor=NW, font=('Arial 10 bold'), bg=co2, fg=co4, relief=SOLID)
ltotv1.place(x=380,y=10)

#totq
ltotq = Label(framem, text='gg', width=13, height=2, anchor=CENTER, font=('Arial 18 bold'), bg=co6, fg=co2)
ltotq.place(x=380,y=120)

ltotq1 = Label(framem, text='  Quantidade de Itens:              ', height=1, anchor=NW, font=('Arial 10 bold'), bg=co2, fg=co4, relief=SOLID)
ltotq1.place(x=380,y=100)

#tabela do banco de dados
def mostrar():
    global tree
    tabela_head = ['#Item','Nome', 'Descrição', 'Marca', 'Data', 'Valor']

    lista_itens = ver_form()



    tree = ttk.Treeview(framef, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(framef, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(framef, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    framef.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center"]
    h=[60,160,170,150,120,120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    
    numeric_quantidade = []

    for item in lista_itens:
        try:
            numeric_value = float(item[5])
            numeric_quantidade.append(numeric_value)
        except ValueError:
            pass

 
    Total_valor = sum(numeric_quantidade)
    Total_itens = len(numeric_quantidade)

    ltotv['text'] = 'R$ {:,.2f}'.format(Total_valor)
    ltotq['text'] = Total_itens

mostrar()

janela.mainloop()


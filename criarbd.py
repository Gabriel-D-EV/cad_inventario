import sqlite3 as lite

#criar conexao
cx = lite.connect('dados.db')

#criar banco de dados
with cx:
    cur = cx.cursor()
    cur.execute("CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT, Descrição TEXT, Marca TEXT, Data DATE, Valor DECIMAL, Imagem TEXT)")
    print("Banco de Dedos criado com Sucessso!!")

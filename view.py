import sqlite3 as lite

#criar conexao
cx = lite.connect('dados.db')

#CRUD

#inserir dados
def inserir_form(i):
    with cx:
        cur = cx.cursor()
        query = "INSERT INTO Inventario(Nome, Descrição, Marca, Data, Valor, Imagem) VALUES(?,?,?,?,?,?)"
        cur.execute(query,i)
        print('dados inseridos com sucesso')

#atualizando
def att_form(i):
    with cx:
        cur = cx.cursor()
        query = "UPDATE Inventario SET Nome=?, Descrição=?, Marca=?, Data=?, Valor=?, Imagem=? WHERE id=?"
        cur.execute(query,i)

#deletar dados
def del_form(i):
    with cx:
        cur = cx.cursor()
        query = "DELETE FROM Inventario WHERE id=?"
        cur.execute(query,i)

#ver dados
def ver_form():
    ver_dados = []
    with cx:
        cur = cx.cursor()
        query = "SELECT * FROM Inventario"
        cur.execute(query)

        linhas = cur.fetchall()
        for l in linhas:
            ver_dados.append(l)
    return ver_dados

#ver dados individuais
def ver_item(id):
    ver_dados_ind = []
    with cx:
        cur = cx.cursor()
        query = "SELECT * FROM Inventario WHERRE id=?"
        cur.execute(query,id)

        linhas = cur.fetchall()
        for l in linhas:
            ver_dados_ind.append(l)



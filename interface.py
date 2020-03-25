from tkinter import *
import servidor
import json
import cliente

def click():
    entered_text = textentry.get()
    saida.delete(0.0,END)
    print(entered_text)
    iarquivo = {}
    iarquivo['ip'] = entered_text
    with open('iarquivo.json', 'w', encoding='utf-8') as f:
        json.dump(iarquivo, f)


    cl = cliente.cliente()
    tipo = cl.tipo()
    definicao = tipo
    print(definicao)
    saida.insert(END,definicao) # saida na tela // Reposta do servidor tem que vir aqui

#main
window = Tk()
window.title("App_Josie_Roberto")
window.configure(background = 'white')

#Inserir foto na interface
photo1 = PhotoImage(file = 'giphy.gif')
Label(window,image = photo1,bg = 'black').grid(row = 0 ,column = 0 ,sticky = W )

#Criar Label
Label(window, text = 'Digite o seu número de IP:',bg = 'white',fg = 'black',font = 'none 12 bold').grid(row = 1,column = 0,sticky = W)

#Entrada de texto
textentry = Entry(window,width = 20, bg = 'white')
textentry.grid(row = 2,column = 0,sticky = W)

#Botão de enviar
Button(window, text = 'ENVIAR', width = 6,command = click).grid(row = 3,column = 0,sticky = W)

#Criar outra label
Label(window, text = 'Definição:', bg = 'white', fg = 'black',font = 'none 12 bold').grid(row = 4,column = 0, sticky = W)

#caixa de texto
saida = Text(window,width = 60, height = 6, wrap = WORD , background = 'white')
saida.grid(row = 5,column = 0, columnspan = 2 , sticky = W)

#Dicionário
#my_compdicionario = {'algoritimo' : 'Conjunto de passos para realizar determinada tarefa','bug': 'pedaço de código que ocasiona uma falha'}

#função de saída
def close_window():
    window.destroy()
    exit()

#Encerrar
Label(window,text = 'Clique para encerrar a conexão',bg = 'white' , fg = 'black' , font = 'none 12 bold' ).grid(row = 6,column = 0,sticky = W)
Button(window,text = 'Encerrar', width = 14 , command = close_window).grid(row = 7 , column = 0, sticky = W)

#Rodar o código
window.mainloop()

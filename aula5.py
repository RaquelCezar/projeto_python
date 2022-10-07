
from tkinter import *
janela = Tk()
janela ["bg"] = "#FC970A"
app = Frame(janela)
app.grid()


def escrever():
    print("Meu nome é",entrynome.get(),", e minha idade é",entryidade.get(),".")


Labeltitle = Label (janela, text="FOTOGRAIA 2022", bg='#FC970A', foreground="white")
Labeltitle.place(x=500, y=10)

labelnome = Label (janela, text="Insira seu nome: ", font="Times", bg= "#FC970A", foreground="white")
labelnome.place(x=100, y=50)
entrynome = Entry(janela)
entrynome.place(x=210, y=50)

labelidade = Label (janela, text="Insera sua idade: ", font="Times", bg= "#FC970A", foreground="white")
labelidade.place(x=100, y=100)
entryidade = Entry (janela)
entryidade.place(x=210, y=100)

btnclicar = Button (janela, width=20, text="Clicar", command=escrever,  bg= "#FC5D0A", foreground="white" )
btnclicar.place(x=180, y=150)

title = "Documentos fotografia"
janela.title(title)
janela.geometry("1200x1500")
janela.resizable(True, True)
janela.mainloop()
janela.destroy()

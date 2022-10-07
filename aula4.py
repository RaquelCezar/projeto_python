from tkinter import *
janela = Tk()
janela ["bg"] = '#F0AD30'
app = Frame(janela)
app.grid()

labelMsg = Label(janela,text= "Testar", font= "Times", bg="white", foreground="black")
labelMsg.place(x=450, y=250)

title= "Sistema Tarumã"
janela.title(title)
janela.geometry("1300x768")
janela.resizable(True,True)
janela.mainloop()
janela.destroy()


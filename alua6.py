import tkinter as tk

def cadrastrarProduto():
    cadrastoproduto = tk.Toplevel(app)
    cadrastoproduto.title("Cadrasto do Produto")
    cadrastoproduto.geometry("800x600")
    labelProdutoLabel = tk.Label (app, text="Insera seu nome: ", font="Times", bg= "#FC970A", foreground="white")
    labelProdutoLabel.place(x=100, y=100)
    entrynome = tk.Entry (app)
    entrynome.place(x=210, y=100)



def cadrastrarUsuario():
    cadrastousuario = tk.Toplevel(app)
    cadrastousuario.title("Cadrasto do Usuário")
    cadrastousuario.geometry("800x600")
    labelCadrastoLabel = tk.Label (app, text="Insera seu nome: ", font="Times", bg= "#FC970A", foreground="white")
    labelCadrastoLabel.place(x=100, y=100)
    entryidade = tk.Entry (app)
    entryidade.place(x=210, y=100)

app = tk.Tk()
app ['bg'] = "#FC970A", 
menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)


fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Produto", command=cadrastrarProduto)
fileMenu.add_command(label="Usuário", command=cadrastrarUsuario)
menuPrincipal.add_cascade(label="Cadrastar", menu=fileMenu)

title = "Sistema Assis"
app.title(title)
app.geometry("1200x1500")
app.resizable(True, True)
app.mainloop()
app.destroy()

#butttonExemple = tk.Button(app, text="CADRASTOS", bg="#FC5D0A", command=cadrastrarProduto)

#butttonExemple.place(x=100, y=50)


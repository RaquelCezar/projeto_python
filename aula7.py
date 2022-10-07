import tkinter as tk


def cadrastrarProduto():
    cadrastoproduto = tk.Toplevel(app)
    cadrastoproduto.title("Cadrasto do Produto")
    cadrastoproduto.geometry("800x600")

    labelProdutoLabel = tk.Label (cadrastoproduto, text="Insera seu nome: ", font="Times", bg= "#FC970A", foreground="white")
    labelProdutoLabel.place(x=50, y=100)
    entrynome = tk.Entry (cadrastoproduto)
    entrynome.place(x=170, y=100)

    labelSobrenomeLabel = tk.Label (cadrastoproduto, text="Insera seu Sobre nome: ", font="Times", bg= "#FC970A", foreground="white")
    labelSobrenomeLabel.place(x=50, y=130)
    entrySobrenome = tk.Entry (cadrastoproduto)
    entrySobrenome.place(x=210, y=130)

    labeldatanaciLabel = tk.Label(cadrastoproduto, text="Informe sua data de nascimento: ", font="Times", bg= "#FC970A", foreground="white")
    labeldatanaciLabel.place(x=50, y=160)
    enterdata = tk.Entry (cadrastoproduto )
    enterdata.place(x=260,y=160)

    labelSexoLabel = tk.Label (cadrastoproduto, text="Insera seu Sexo: ", font="Times", bg= "#FC970A", foreground="white")
    labelSexoLabel.place(x=50, y=190)
    entrySexo = tk.Entry (cadrastoproduto)
    entrySexo.place(x=170, y=190)

    cidade = tk.Label (cadrastoproduto, text="Informe sua cidade", bg="#FC970A", font="Times", foreground="white")
    cidade.place(x=50, y=220)
    entrycidade = tk.Entry(cadrastoproduto)
    entrycidade.place(x=180, y= 220)

    estado = tk.Label(cadrastoproduto, text="Estado: ", font="Times", bg="#FC970A", foreground="white" )
    estado.place(x=50, y=250)
    entryestado = tk.Entry(cadrastoproduto)
    entryestado.place(x=120, y=250)


    def salvarproduto():
        print("O nome informado foi: ", entrynome.get())
        print("O Sobre nome informado foi: ", entrySobrenome.get())
        print("A data de nascimento informada foi: ", enterdata.get())
        print("O sexo informado foi :", entrySexo.get() )
        print("A cidade informada foi: ", entrycidade.get())
        print("O estado informado foi: ", entryestado.get())

    btnproduto = tk.Button(cadrastoproduto, bg="#FC970A",command=salvarproduto, text="Enviar")
    btnproduto.place(x=100, y=400)
    




def cadrastrarUsuario():
    cadrastousuario = tk.Toplevel(app)
    cadrastousuario.title("Cadrasto do Usuário")
    cadrastousuario.geometry("800x600")
    labelCadrastoLabel = tk.Label (cadrastousuario, text="Insera seu nome: ", font="Times", bg= "#FC970A", foreground="white")
    labelCadrastoLabel.place(x=100, y=100)
    entryidade = tk.Entry (cadrastousuario)
    entryidade.place(x=210, y=100)

app = tk.Tk()
app ['bg'] = "#FC970A"
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

#github
#echo "# projeto_python" >> README.md 
#git init 
#git add README.md 
#git commit -m "primeiro commit" 
#git branch -M main 
#git remote add origin https://github.com/RaquelCezar/projeto_python.git
#git push - u origem principal
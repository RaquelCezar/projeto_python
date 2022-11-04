import tkinter as tk
import mysql.connector 

class usuarios():
    def __init__(self,id, nome, sobrenome, cidade, estado, data_nascimento):
        self.id = id,
        self.nome = nome,
        self.sobrenome = sobrenome,
        self.cidade = cidade,
        self.estado = estado,
        self.data_nascimento = data_nascimento,

def desconectar(conexao):
    if conexao:
        conexao.close()

def selecionarUsuario():
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USUARIOS")
    table = cursor.fetchall()
    print('\n Usuarios')
    for row in table:
            print("id: ", row[0], end="\n")
            print("Nome: ", row[1], end="\n")
            print("Sobrenome: ", row[2], end="\n")
            print("Cidade: ", row[3], end="\n")
            print("Estado: ", row[4], end="\n")
            print("Nascimento: ", row[5], end="\n")
           
def inserirUsuario(usuario):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO usuarios(id, nome, sorenome, cidade, estado, data_nascimento)" f"VALUES('{usuario.id}','{usuario.nome}',' '{usuario.sobreonome}','{usuario.cidade}','{usuario.estado}','{usuario.data_nascimento}')")
    con.commit()
    desconectar(con)


def conexao():
    try:
            conexao = mysql.connector.connect(
                    host = "localhost", 
                    user = "root",
                    passwd = "",
                    db = "banco_python"
            )
            print("conectado")
            return conexao
    except mysql.connector.Error as erro:
            print(f'Erro ao conectar no Servidor Mysql: {erro}')

def abrirTelaProduto():
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

    estado = tk.Label(cadrastoproduto, text="Estado: ", font="Times", bg="#FC970A", foreground="white" )
    estado.place(x=50, y=250)
    entry_datanascimento = tk.Entry(cadrastoproduto)
    entry_datanascimento.place(x=120, y=250)


    def salvarproduto():
        print("O nome informado foi: ", entrynome.get())
        print("O Sobre nome informado foi: ", entrySobrenome.get())
        print("A data de nascimento informada foi: ", enterdata.get())
        print("O sexo informado foi :", entrySexo.get() )
        print("A cidade informada foi: ", entrycidade.get())
        print("O estado informado foi: ", entryestado.get())
        print("O data de nascimento informado foi: ", entry_datanascimento.get())

    btnproduto = tk.Button(cadrastoproduto, bg="#FC970A",command=salvarproduto, text="Enviar")
    btnproduto.place(x=100, y=400)




def abrirTelaUsuaios():
    cadrastousuario = tk.Toplevel(app)
    cadrastousuario.title("Cadrasto do Usuário")
    selecionarUsuario(cadrastousuario)

    lblld = tk.Label(cadrastousuario, text="Inorme o id= ", font="black",  bg= "#FC970A", foreground="white")
    lblld.place(x=100,y=230)
    entryId = tk.Entry(cadrastousuario)
    entryId.place(x=100=,y=235)  
    
    labelusuarioLabel = tk.Label (cadrastousuario, text="Insera seu nome: ", font="Times", bg= "#FC970A", foreground="white")
    labelusuarioLabel.place(x=50, y=250)
    entrynome = tk.Entry (cadrastousuario)
    entrynome.place(x=170, y=255)

    labelSobrenomeLabel = tk.Label (cadrastousuario, text="Insera seu Sobrenome: ", font="Times", bg= "#FC970A", foreground="white")
    labelSobrenomeLabel.place(x=50, y=275)
    entrySobrenome = tk.Entry (cadrastousuario)
    entrySobrenome.place(x=210, y=275)

    labeldatanaciLabel = tk.Label(cadrastousuario, text="Informe sua data de nascimento: ", font="Times", bg= "#FC970A", foreground="white")
    labeldatanaciLabel.place(x=50, y=300)
    enterdata = tk.Entry (cadrastousuario )
    enterdata.place(x=260,y=300)

    cidade = tk.Label (cadrastousuario, text="Informe sua cidade", bg="#FC970A", font="Times", foreground="white")
    cidade.place(x=50, y=325)
    entrycidade = tk.Entry(cadrastousuario)
    entrycidade.place(x=180, y= 325)

    estado = tk.Label(cadrastousuario, text="Informe seu estado: ", font="Times", bg="#FC970A", foreground="white" )
    estado.place(x=50, y=350)
    entryestado = tk.Entry(cadrastousuario)
    entryestado.place(x=120, y=350)

    btnSalvar = tk.Button(abrirTelaUsuaios, bg="#FC970A",command=salvarUsuario, text="Salvar")
    btnSalvar.place(x=100, y=400)

def salvarUsuario():
    usuario = usuarios(None, entrynome.get(), entrySobrenome.get(), enterdata.get(),entrySexo.get(), entrycidade.get(),  entryestado.get(), entry_datanascimento.get())
    inserirUsuario(usuario)

app = tk.Tk()
app ['bg'] = "#FC970A"
menuPrincipal = tk.Menu(app) 
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Produto", command=abrirTelaProduto)
fileMenu.add_command(label="Usuário", command=abrirTelaUsuaios)
menuPrincipal.add_cascade(label="Função", menu=fileMenu)

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
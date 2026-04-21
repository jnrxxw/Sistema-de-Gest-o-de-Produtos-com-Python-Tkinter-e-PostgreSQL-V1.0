import tkinter as tk
from tkinter import ttk
from appBD import AppBD


class PrincipalBD:
    def __init__(self , root , db): 
        self.root = root
        self.db = db
        self.root.title("Gestao de Produtos")


        self.lblCodigo = tk.Label(root, text="Codigo:")
        self.lblCodigo.grid(row=0, column=0, padx=5, pady=5)
        self.txtCodigo = tk.Entry(root)
        self.txtCodigo.grid(row=0, column=1, padx=5, pady=5)


        self.lblNome = tk.Label(root, text="Nome:")
        self.lblNome.grid(row=1, column=0, padx=5, pady=5)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1, padx=5, pady=5)

        self.lblPreco = tk.Label(root, text="Preco:")
        self.lblPreco.grid(row=2, column=0, padx=5, pady=5)
        self.txtPreco = tk.Entry(root)  
        self.txtPreco.grid(row=2, column=1, padx=5, pady=5)

        self.btnCadastrar = tk.Button(root, text="Cadastrar", command=self.fCadastrar_produto)
        self.btnCadastrar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.btnAtualizar = tk.Button(root, text="Atualizar", command=self.fAtualizarProduto)
        self.btnAtualizar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.btnExcluir = tk.Button(root, text="Excluir", command=self.fExcluir_produto)
        self.btnExcluir.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.btnLimpar = tk.Button(root, text="Limpar", command=self.fLimparTela)
        self.btnLimpar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


        self.tree = ttk.Treeview(root, columns=("Codigo", "Nome", "Preco"), show="headings")
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preco", text="Preco")
        self.tree.grid(row=0, column=2, rowspan=7, padx=5, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        self.carregarDadosIniciais()

    
    def fCadastrar_produto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.inserir_dados(nome, preco)
        self.tree.insert("", "end", values=(codigo, nome, preco))
        self.fLimparTela()

    

    def fAtualizarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.atualizar_dados(codigo, nome, preco)
        self.fLimparTela()
        self.carregarDadosIniciais()

    def fExcluir_produto(self):
        codigo = self.txtCodigo.get()
        self.db.excluir_dados(codigo)
        self.fLimparTela()
        self.carregarDadosIniciais()

    def fLimparTela(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)

    def apresentarRegistrosSelecionados(self, event):
        selecao = self.tree.selection()

        if not selecao:
         return  # não faz nada se nada estiver selecionado

        item = selecao[0]
        valores = self.tree.item(item, "values")

        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.insert(tk.END, valores[0])

        self.txtNome.delete(0, tk.END)
        self.txtNome.insert(tk.END, valores[1])

        self.txtPreco.delete(0, tk.END)
        self.txtPreco.insert(tk.END, valores[2])


    def carregarDadosIniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        registros = self.db.selecionar_dados()
        for registro in registros:
            self.tree.insert("", "end", values=registro)


root = tk.Tk()
app_bd = AppBD()
app_gui = PrincipalBD(root, app_bd)
root.mainloop()

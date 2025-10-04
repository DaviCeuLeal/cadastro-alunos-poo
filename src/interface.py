import tkinter as tk
from tkinter import messagebox

class SistemaCadastroAlunos:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Cadastro de Alunos - TechEduca")
        self.master.geometry("420x420")
        self.master.configure(bg="#f1b7e3")
        self.master.resizable(False, False)

        # Ícone da janela (opcional)
        try:
            self.master.iconbitmap("logo.ico")
        except:
            pass

        # Título principal
        tk.Label(
            self.master,
            text="Cadastro de Alunos",
            font=("Garamond", 16, "bold"),
            bg="#f1b7e3",
            fg="#333"
        ).pack(pady=15)

        # Campos de entrada
        self.criar_campos()

        # Botões
        self.criar_botoes()

        # Rodapé
        tk.Label(
            self.master,
            text="© 2025 TechEduca - Sistema de Cadastro de Alunos",
            bg="#f1b7e3",
            fg="#555",
            font=("Arial", 8)
        ).pack(side="bottom", pady=10)

    def criar_campos(self):
        """Cria os campos de entrada de dados"""
        tk.Label(self.master, text="Nome do Aluno:", bg="#f1b7e3", anchor="w").pack()
        self.entrada_nome = tk.Entry(self.master, width=40)
        self.entrada_nome.pack(pady=5)

        tk.Label(self.master, text="CPF:", bg="#f1b7e3", anchor="w").pack()
        self.entrada_cpf = tk.Entry(self.master, width=40)
        self.entrada_cpf.pack(pady=5)

        tk.Label(self.master, text="Status (Ativo/Inativo):", bg="#f1b7e3", anchor="w").pack()
        self.entrada_status = tk.Entry(self.master, width=40)
        self.entrada_status.pack(pady=5)

    def criar_botoes(self):
        """Cria os botões principais"""
        frame_botoes = tk.Frame(self.master, bg="#f1b7e3")
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Cadastrar", width=15, bg="#FF009D", fg="white", command=self.cadastrar).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_botoes, text="Atualizar", width=15, bg="#FF009D", fg="white", command=self.atualizar).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_botoes, text="Excluir", width=15, bg="#FF009D", fg="white", command=self.excluir).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame_botoes, text="Consultar", width=15, bg="#FF009D", fg="white", command=self.consultar).grid(row=1, column=1, padx=5, pady=5)

    # ====== Métodos dos botões ======
    def cadastrar(self):
        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        status = self.entrada_status.get()

        if nome and cpf and status:
            messagebox.showinfo("Cadastro", f"Aluno {nome} cadastrado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos antes de cadastrar.")

    def atualizar(self):
        messagebox.showinfo("Atualizar", "Função de atualização ainda não implementada.")

    def excluir(self):
        messagebox.showinfo("Excluir", "Função de exclusão ainda não implementada.")

    def consultar(self):
        messagebox.showinfo("Consultar", "Função de consulta ainda não implementada.")


# ====== Ponto de entrada do sistema ======
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaCadastroAlunos(root)
    root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox
import os


class EditorNotas(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Editor de Notas")
        self.geometry("800x600")
        self.arquivo_atual = None
        self.modificado = False

        # Centralizar janela
        self.centralizar_janela()

        # Criar toolbar
        self.criar_toolbar()

        # Criar área de texto
        self.texto_area = tk.Text(self, wrap=tk.WORD, font=("Arial", 11), undo=True)
        self.texto_area.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.texto_area.bind("<KeyRelease>", self._marcar_modificado)

        # Criar status bar
        self.criar_statusbar()

        # Criar menu
        self.criar_menu()

    def centralizar_janela(self):
        """Centraliza a janela na tela"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 800) // 2
        y = (self.winfo_screenheight() - 600) // 2
        self.geometry(f"+{x}+{y}")

    def criar_toolbar(self):
        """Cria barra de ferramentas com botões"""
        toolbar = tk.Frame(self, bg="#f0f0f0", height=50)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)

        # Botão Novo
        btn_novo = tk.Button(toolbar, text="📄 Novo", command=self.novo_arquivo, 
                             bg="white", relief=tk.RAISED)
        btn_novo.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Abrir
        btn_abrir = tk.Button(toolbar, text="📁 Abrir", command=self.abrir_arquivo,
                              bg="white", relief=tk.RAISED)
        btn_abrir.pack(side=tk.LEFT, padx=2, pady=2)

        # Botão Salvar
        btn_salvar = tk.Button(toolbar, text="💾 Salvar", command=self.salvar_arquivo,
                               bg="white", relief=tk.RAISED)
        btn_salvar.pack(side=tk.LEFT, padx=2, pady=2)

        # Separador
        sep = tk.Frame(toolbar, bg="gray", width=2)
        sep.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        # Botão Sair
        btn_sair = tk.Button(toolbar, text="❌ Sair", command=self.on_closing,
                             bg="white", relief=tk.RAISED)
        btn_sair.pack(side=tk.LEFT, padx=2, pady=2)

    def criar_statusbar(self):
        """Cria barra de status na parte inferior"""
        self.statusbar = tk.Label(self, text="Pronto", bg="#e0e0e0", 
                                  relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def criar_menu(self):
        """Cria menu com atalhos de teclado"""
        menubar = tk.Menu(self)
        
        # Menu Arquivo
        arquivomenu = tk.Menu(menubar, tearoff=0)
        arquivomenu.add_command(label="Novo", command=self.novo_arquivo, accelerator="Ctrl+N")
        arquivomenu.add_command(label="Abrir", command=self.abrir_arquivo, accelerator="Ctrl+O")
        arquivomenu.add_command(label="Salvar", command=self.salvar_arquivo, accelerator="Ctrl+S")
        arquivomenu.add_command(label="Salvar Como...", command=self.salvar_como_arquivo)
        arquivomenu.add_separator()
        arquivomenu.add_command(label="Sair", command=self.on_closing, accelerator="Ctrl+Q")
        
        # Menu Editar
        editar_menu = tk.Menu(menubar, tearoff=0)
        editar_menu.add_command(label="Desfazer", command=lambda: self.texto_area.edit_undo(), accelerator="Ctrl+Z")
        editar_menu.add_command(label="Refazer", command=lambda: self.texto_area.edit_redo(), accelerator="Ctrl+Y")
        editar_menu.add_separator()
        editar_menu.add_command(label="Selecionar tudo", command=lambda: self._select_all(), accelerator="Ctrl+A")

        # Menu Ajuda
        ajuda_menu = tk.Menu(menubar, tearoff=0)
        ajuda_menu.add_command(label="Sobre", command=self._mostrar_sobre)

        menubar.add_cascade(label="Arquivo", menu=arquivomenu)
        menubar.add_cascade(label="Editar", menu=editar_menu)
        menubar.add_cascade(label="Ajuda", menu=ajuda_menu)

        self.config(menu=menubar)

        # Vincular atalhos de teclado
        self.bind("<Control-n>", lambda e: self.novo_arquivo())
        self.bind("<Control-o>", lambda e: self.abrir_arquivo())
        self.bind("<Control-s>", lambda e: self.salvar_arquivo())
        self.bind("<Control-q>", lambda e: self.on_closing())
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def _marcar_modificado(self, event=None):
        """Marca o documento como modificado"""
        if not self.modificado:
            self.modificado = True
            titulo = self.title()
            if not titulo.startswith("*"):
                self.title(f"*{titulo}")
            self.atualizar_statusbar()

    def _select_all(self):
        """Seleciona todo o texto"""
        self.texto_area.tag_add(tk.SEL, "1.0", tk.END)
        self.texto_area.event_generate("<<Change>>")

    def _mostrar_sobre(self):
        """Mostra janela de informações"""
        messagebox.showinfo("Sobre", "Editor de Notas v1.0\n\nUm editor de texto simples e prático.")

    def atualizar_statusbar(self):
        """Atualiza informações da barra de status"""
        conteudo = self.texto_area.get(1.0, tk.END)
        linhas = len(conteudo.split("\n")) - 1
        caracteres = len(conteudo) - 1
        
        status = f"Linhas: {linhas} | Caracteres: {caracteres}"
        if self.arquivo_atual:
            status += f" | Arquivo: {os.path.basename(self.arquivo_atual)}"
        
        self.statusbar.config(text=status)

    def novo_arquivo(self):
        """Cria um novo arquivo"""
        if self.modificado:
            resposta = messagebox.askyesnocancel(
                "Salvar alterações?",
                "Documento modificado. Deseja salvar antes de criar um novo?"
            )
            if resposta is None:  # Cancelar
                return
            elif resposta:  # Sim
                self.salvar_arquivo()

        self.texto_area.delete(1.0, tk.END)
        self.arquivo_atual = None
        self.modificado = False
        self.title("Editor de Notas")
        self.atualizar_statusbar()
        self.statusbar.config(text="Novo arquivo criado")

    def abrir_arquivo(self):
        """Abre um arquivo existente"""
        if self.modificado:
            resposta = messagebox.askyesnocancel(
                "Salvar alterações?",
                "Documento modificado. Deseja salvar antes de abrir outro?"
            )
            if resposta is None:
                return
            elif resposta:
                self.salvar_arquivo()

        filepath = filedialog.askopenfilename(
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )

        if not filepath:
            return

        try:
            with open(filepath, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.texto_area.delete(1.0, tk.END)
                self.texto_area.insert(tk.END, conteudo)
            
            self.arquivo_atual = filepath
            self.modificado = False
            self.title(f"Editor de Notas - {os.path.basename(filepath)}")
            self.atualizar_statusbar()
            self.statusbar.config(text=f"Arquivo aberto: {filepath}")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")
            self.statusbar.config(text="Erro ao abrir arquivo")

    def salvar_arquivo(self):
        """Salva o arquivo atual ou abre dialog se novo"""
        if self.arquivo_atual:
            self._salvar_em(self.arquivo_atual)
        else:
            self.salvar_como_arquivo()

    def salvar_como_arquivo(self):
        """Salva o arquivo com um novo nome"""
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )

        if filepath:
            self._salvar_em(filepath)

    def _salvar_em(self, filepath):
        """Função auxiliar para salvar em um caminho específico"""
        try:
            conteudo = self.texto_area.get(1.0, tk.END)
            with open(filepath, "w", encoding="utf-8") as arquivo:
                arquivo.write(conteudo)
            
            self.arquivo_atual = filepath
            self.modificado = False
            self.title(f"Editor de Notas - {os.path.basename(filepath)}")
            self.atualizar_statusbar()
            self.statusbar.config(text=f"Arquivo salvo: {filepath}")
            messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo: {e}")
            self.statusbar.config(text="Erro ao salvar arquivo")

    def on_closing(self):
        """Trata o fechamento da janela"""
        if self.modificado:
            resposta = messagebox.askyesnocancel(
                "Salvar alterações?",
                "Documento modificado. Deseja salvar antes de fechar?"
            )
            if resposta is None:  # Cancelar
                return
            elif resposta:  # Sim
                self.salvar_arquivo()

        self.quit()


if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()
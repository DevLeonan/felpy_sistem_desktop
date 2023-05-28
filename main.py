from tkinter import ttk
import PIL.Image
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3 as db


# criando funções
def cadastrar():
    janela_principal.withdraw()  # Oculta a janela principal
    janela_cadastrar.deiconify()  # Exibe a janela cadastrar

def criar():
    janela_cadastrar.withdraw()  # Oculta a janela cadastrar
    janela_principal.deiconify()  # Exibe a janela principal

def home():
    janela_principal.withdraw()  # Oculta a janela principal
    janela_home.deiconify()  # Exibe a janela home

def caixa():
    janela_home.withdraw() # Oculta a janela home
    janela_caixa.deiconify()  # Exibe a janela caixa

def estoque():
    janela_home.withdraw()  # Oculta a janela principal
    janela_estoque.deiconify()  # Exibe a janela estoque

def sair():
    janela_home.withdraw()  # Oculta a janela home
    janela_principal.deiconify()  # Exibe a janela principal

def voltar_caixa():
    janela_caixa.withdraw()  # Oculta a janela caixa
    janela_home.deiconify()  # Exibe a janela home

def voltar_estoque():
    janela_estoque.withdraw()  # Oculta a janela estoque
    janela_home.deiconify()  # Exibe a janela home

def voltar_cadastrar():
    janela_cadastrar.withdraw()  # Oculta a janela cadastrar
    janela_principal.deiconify()  # Exibe a janela principal

def voltar_fechamento():
    janela_fechamento.withdraw()  # Oculta a janela cadastrar
    janela_home.deiconify()  # Exibe a janela principal

def fechamento():
    janela_home.withdraw()  # Oculta a janela home
    janela_fechamento.deiconify()  # Exibe a janela fechamento


# configurando janela principal
janela_principal = ctk.CTk()
janela_principal.geometry('700x400')
janela_principal.resizable(False, False)
janela_principal.title('Felpy_Sistem')
janela_principal.iconbitmap('icon.ico')

# configurando janela cadastrar
janela_cadastrar = ctk.CTk()
janela_cadastrar.geometry('400x600')
janela_cadastrar.resizable(False, False)
janela_cadastrar.title('Cadastrar')
janela_cadastrar.iconbitmap('icon.ico')

# configurando janela home
janela_home = ctk.CTk()
janela_home.geometry('800x600')
janela_home.resizable(False, False)
janela_home.title('Home')
janela_home.iconbitmap('icon.ico')

# configurando janela caixa
janela_caixa = ctk.CTk()
janela_caixa.attributes('-fullscreen', True)
janela_caixa.resizable(False, False)
janela_caixa.title('CAIXA')
janela_caixa.iconbitmap('icon.ico')

# configurando janela estoque
janela_estoque = ctk.CTk()
janela_estoque.attributes('-fullscreen', True)
janela_estoque.resizable(False, False)
janela_estoque.title('ESTOQUE')
janela_estoque.iconbitmap('icon.ico')

# configurando janela fechamento
janela_fechamento = ctk.CTk()
janela_fechamento.attributes('-fullscreen', True)
janela_fechamento.resizable(False, False)
janela_fechamento.title('FECHAMENTO')
janela_fechamento.iconbitmap('icon.ico')


# ========================== INICIO JANELA PRINCIPAL ========================== #

# tratando imagens janela principal
img = PhotoImage(file='Felpy.png')
label_img = ctk.CTkLabel(master=janela_principal, image=img)
label_img.place(x=5, y=0)

img_login = PhotoImage(file='login.png')
label_login = ctk.CTkLabel(master=janela_principal, image=img_login)
label_login.place(x=465, y=10)


# criando fontes personalizadas
fonte_personalizada = ctk.CTkFont(family='verdana', size=30, underline= False)
fonte_personalizada2 = ctk.CTkFont(family='verdana', size=15, underline= False)
fonte_personalizada3 = ctk.CTkFont(family='italic', size=80, underline= False)

# adicionando labels na janela principal
label_usuario = ctk.CTkLabel(master=janela_principal, text='Usuário:', font=fonte_personalizada2, text_color="white")
label_usuario.place(x=420, y=170)

label_senha = ctk.CTkLabel(master=janela_principal, text='Senha:', font=fonte_personalizada2, text_color="white")
label_senha.place(x=420, y=210)

# adicionando entrys na janela principal
entry_usuario = ctk.CTkEntry(master=janela_principal, placeholder_text="Digite seu usuário...")
entry_usuario.place(x=500, y=170)

entry_senha = ctk.CTkEntry(master=janela_principal, placeholder_text="Digite sua Senha...")
entry_senha.place(x=500, y=210)

# adicionando botoes na janela principal
btn_logar = ctk.CTkButton(master=janela_principal, text="LOGAR", text_color='white', bg_color='#0000CD', width=260, corner_radius=0, command=home)
btn_logar.place(x=400, y=320)

btn_cadastrar = ctk.CTkButton(master=janela_principal, text="CADASTRAR", text_color='white', bg_color='#0000CD', width=260, corner_radius=0, command=cadastrar)
btn_cadastrar.place(x=400, y=360)

# adicionando checkbox na janela principal
check_principal = ctk.CTkCheckBox(master=janela_principal, text='Lembrar Login')
check_principal.place(x=400, y=280)

# ========================== FIM DA JANELA PRINCIPAL ========================== #
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ========================== INICIO DA JANELA CADASTRAR ========================== #

# criando labels janela cadastrar
label_usuario_cadastrar = ctk.CTkLabel(janela_cadastrar, text="""
CADASTRAR
USUÁRIO
""",
font=fonte_personalizada, text_color="white")
label_usuario_cadastrar.place(x=110, y=0)

label_email_cadastrar = ctk.CTkLabel(janela_cadastrar, text='E-mail:', font=fonte_personalizada2, text_color="white")
label_email_cadastrar.place(x=50, y=200)

label_usuario_cadastrar = ctk.CTkLabel(janela_cadastrar, text='Usuário:', font=fonte_personalizada2, text_color="white")
label_usuario_cadastrar.place(x=50, y=250)

label_senha_cadastrar = ctk.CTkLabel(janela_cadastrar, text='Senha:', font=fonte_personalizada2, text_color="white")
label_senha_cadastrar.place(x=50, y=300)

label_senha_cadastrar = ctk.CTkLabel(janela_cadastrar, text='Confirmar Senha:', font=fonte_personalizada2, text_color="white")
label_senha_cadastrar.place(x=50, y=350)

# adicionando entrys na janela cadastrar
entry_usuario_cadastrar = ctk.CTkEntry(janela_cadastrar, placeholder_text="Digite seu E-mail...", width=240)
entry_usuario_cadastrar.place(x=130, y=200)

entry_senha_cadastrar = ctk.CTkEntry(janela_cadastrar, placeholder_text="Digite seu Usuário...", width=240)
entry_senha_cadastrar.place(x=130, y=250)

entry_usuario_cadastrar = ctk.CTkEntry(janela_cadastrar, placeholder_text="Digite sua Senha...", width=240)
entry_usuario_cadastrar.place(x=130, y=300)

entry_usuario_cadastrar = ctk.CTkEntry(janela_cadastrar, placeholder_text="Confirme sua Senha...", width=170)
entry_usuario_cadastrar.place(x=200, y=350)

entry_cargo_cadastrar = ctk.CTkOptionMenu(janela_cadastrar, width=320, height=20, values=["Caixa", "Gerente"])
entry_cargo_cadastrar.set('Selecionar Cargo')
entry_cargo_cadastrar.place(x=50, y=400)

# adicionando botoes na janela cadastrar
btn_cadastrar_criar = ctk.CTkButton(janela_cadastrar, text="CRIAR", text_color='white', bg_color='#0000CD', width=320, height=15, corner_radius=0, command=criar)
btn_cadastrar_criar.place(x=50, y=500)

btn_cadastrar_voltar = ctk.CTkButton(janela_cadastrar, text="VOLTAR", text_color='white', width=320, height=15, corner_radius=0, fg_color='#8B0000', hover=True, hover_color='#FF0000', command=voltar_cadastrar)
btn_cadastrar_voltar.place(x=50, y=550)

# ========================== FIM DA JANELA CADASTRAR ========================== #
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ========================== INICIO JANELA HOME ========================== #

# adicionando botoes na janela home
btn_home_caixa = ctk.CTkButton(janela_home, text="CAIXA", text_color='white', width=215, height=200, corner_radius=0, fg_color='#1E90FF', hover=True, hover_color='#0000FF', font=fonte_personalizada, command=caixa)
btn_home_caixa.place(x=150, y=50)

btn_home_estoque = ctk.CTkButton(janela_home, text="ESTOQUE", text_color='white', width=215, height=200, corner_radius=0, fg_color='#1E90FF', hover=True, hover_color='#0000FF', font=fonte_personalizada, command=estoque)
btn_home_estoque.place(x=500, y=50)

btn_home_fechamento = ctk.CTkButton(janela_home, text=
"""
FECHAMENTO
DE
CAIXA
""", text_color='white', width=200, height=200, corner_radius=0, fg_color='#1E90FF', hover=True, hover_color='#0000FF', font=fonte_personalizada, command=fechamento)
btn_home_fechamento.place(x=150, y=300)

btn_home_sair = ctk.CTkButton(janela_home, text="SAIR", text_color='white', width=215, height=200, corner_radius=0, fg_color='#8B0000', hover=True, hover_color='#FF0000', font=fonte_personalizada, command=sair)
btn_home_sair.place(x=500, y=300)

# ========================== FIM DA JANELA HOME ========================== #
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ========================== INICIO JANELA CAIXA ========================== #

# criando labels janela caixa
caixa_label = ctk.CTkLabel(janela_caixa, text='CAIXA LIVRE', font=fonte_personalizada3)
caixa_label.place(x=100, y=50)

produto_label = ctk.CTkLabel(janela_caixa, text='PRODUTOS:', font=fonte_personalizada2)
produto_label.place(x=130, y=165)

barras_label = ctk.CTkLabel(janela_caixa, text='CODIGO DE BARRAS:', font=fonte_personalizada2)
barras_label.place(x=130, y=265)

quantidade_label = ctk.CTkLabel(janela_caixa, text='QUANTIDADE:', font=fonte_personalizada2)
quantidade_label.place(x=130, y=365)

descricao_label = ctk.CTkLabel(janela_caixa, text='DESCRIÇÃO:', font=fonte_personalizada2)
descricao_label.place(x=130, y=465)

troco_label = ctk.CTkLabel(janela_caixa, text='TROCO:', font=fonte_personalizada3)
troco_label.place(x=130, y=650)

total_label = ctk.CTkLabel(janela_caixa, text='TOTAL:', font=fonte_personalizada3)
total_label.place(x=750, y=650)

# adicionando frame na janela caixa
troco_frame = ctk.CTkFrame(janela_caixa, width=250, height=100)
troco_frame.place(x=450, y=650)

total_frame = ctk.CTkFrame(janela_caixa, width=250, height=100)
total_frame.place(x=1050, y=650)

produtos_frame = ctk.CTkFrame(janela_caixa, width=600, height=400)
produtos_frame.place(x=700, y=150)

# adicionando entrys na janela caixa
entry_produto_caixa = ctk.CTkEntry(janela_caixa,placeholder_text="Produto", width=400, height=50)
entry_produto_caixa.place(x=130, y=190)

entry_barras_caixa = ctk.CTkEntry(janela_caixa, placeholder_text="Código de barras", width=400, height=50)
entry_barras_caixa.place(x=130, y=290)

entry_quantidade_caixa = ctk.CTkEntry(janela_caixa, placeholder_text="Quantidade", width=400, height=50)
entry_quantidade_caixa.place(x=130, y=390)

entry_quantidade_caixa = ctk.CTkEntry(janela_caixa, placeholder_text="Descrição", width=400, height=50)
entry_quantidade_caixa.place(x=130, y=490)

entry_pagamento_caixa = ctk.CTkOptionMenu(janela_caixa, width=600, height=30, values=["Cartão de credito", "Cartão de débito", "Pix", "Dinheiro"])
entry_pagamento_caixa.set("FORMA DE PAGAMENTO")
entry_pagamento_caixa.place(x=700,y=110)

# adicionar botão a janela caixa
btn_caixa_voltar = ctk.CTkButton(janela_caixa, text="Voltar", text_color='white', width=150, height=25, corner_radius=0, fg_color='#8B0000', hover=True, hover_color='#FF0000', font=fonte_personalizada, command=voltar_caixa)
btn_caixa_voltar.place(x=1000, y=50)

# adicionar Treeview a janela caixa
stilo = ttk.Style()
stilo.configure("mystyle.Treeview", font=fonte_personalizada, rowheight=500)
stilo.configure("mystyle.Treeview.Heading", font=fonte_personalizada)
stilo.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

treeview_caixa = ttk.Treeview(produtos_frame, columns=(1,2,3,4), show="headings", style="mystyle.Treeview", height=18)
treeview_caixa.heading("1",text="Produtos")
treeview_caixa.column("1", width=150)
treeview_caixa.heading("2",text="Descrição")
treeview_caixa.column("2", width=150)
treeview_caixa.heading("3",text="Quantidade")
treeview_caixa.column("3", width=150)
treeview_caixa.heading("4",text="Preço Total")
treeview_caixa.column("4", width=150)

treeview_caixa.pack()

# ========================== FIM DA JANELA CAIXA ========================== #
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ========================== INICIO JANELA ESTOQUE ========================== #

# adicionar botão a janela estoque
btn_estoque_voltar = ctk.CTkButton(janela_estoque, text="Voltar", text_color='white', width=150, height=25, corner_radius=0, fg_color='#8B0000', hover=True, hover_color='#FF0000', font=fonte_personalizada, command=voltar_estoque)
btn_estoque_voltar.place(x=1000, y=50)

btn_estoque_cadastrar = ctk.CTkButton(janela_estoque, text="CADASTRAR", text_color='white', width=200, height=50, corner_radius=0, fg_color='#1E90FF', hover=True, hover_color='#0000FF', font=fonte_personalizada)
btn_estoque_cadastrar.place(x=1000, y=300)

btn_estoque_deletar = ctk.CTkButton(janela_estoque, text="DELETAR", text_color='white', width=200, height=50, corner_radius=0, fg_color='#8B0000', hover=True, hover_color='#FF0000', font=fonte_personalizada)
btn_estoque_deletar.place(x=1000, y=450)

# adicionando frame na janela estoque
estoque_frame = ctk.CTkFrame(janela_estoque, width=800, height=500)
estoque_frame.place(x=100, y=150)

# criando labels janela estoque
estoque_label = ctk.CTkLabel(janela_estoque, text='ESTOQUE', font=fonte_personalizada3)
estoque_label.place(x=100, y=50)

# adicionar Treeview a janela estoque
stilo = ttk.Style()
stilo.configure("mystyle.Treeview", font=fonte_personalizada, rowheight=500)
stilo.configure("mystyle.Treeview.Heading", font=fonte_personalizada)
stilo.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

treeview_estoque = ttk.Treeview(estoque_frame, columns=(1,2,3,4), show="headings", style="mystyle.Treeview", height=25)
treeview_estoque.heading("1",text="Produtos")
treeview_estoque.column("1", width=180)
treeview_estoque.heading("2",text="Descrição")
treeview_estoque.column("2", width=180)
treeview_estoque.heading("3",text="Quantidade")
treeview_estoque.column("3", width=180)
treeview_estoque.heading("4",text="Preço Unidade")
treeview_estoque.column("4", width=180)

treeview_estoque.pack()
# ========================== FIM DA JANELA CAIXA ========================== #
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ========================== INICIO JANELA FECHAMENTO ========================== #

# adicionando labels na janela FECHAMENTO
fechamento_label = ctk.CTkLabel(janela_fechamento, text='FECHAMENTO DE CAIXA', font=fonte_personalizada3)
fechamento_label.place(x=100, y=10)

# adicionando frame na janela FECHAMENTO
fechamento_frame = ctk.CTkFrame(janela_fechamento, width=850, height=550)
fechamento_frame.place(x=100, y=100)

# adicionar botão a janela FECHAMENTO
btn_fechamento_voltar = ctk.CTkButton(janela_fechamento, text="Voltar", text_color='white', width=150, height=25, corner_radius=0, fg_color='#8B0000', hover=True, hover_color='#FF0000', font=fonte_personalizada, command=voltar_fechamento)
btn_fechamento_voltar.place(x=1000, y=500)

btn_fechamento_calcular = ctk.CTkButton(janela_fechamento, text="Calcular", text_color='white', width=150, height=25, corner_radius=0, fg_color='#1E90FF', hover=True, hover_color='#0000FF', font=fonte_personalizada, command=voltar_fechamento)
btn_fechamento_calcular.place(x=1000, y=200)

btn_fechamento_imprimir = ctk.CTkButton(janela_fechamento, text="imprimir", text_color='white', width=150, height=25, corner_radius=0, fg_color='#1E90FF', hover=True, hover_color='#0000FF', font=fonte_personalizada, command=voltar_fechamento)
btn_fechamento_imprimir.place(x=1000, y=300)

# adicionar Treeview a janela fechamento
stilo = ttk.Style()
stilo.configure("mystyle.Treeview", font=fonte_personalizada, rowheight=500)
stilo.configure("mystyle.Treeview.Heading", font=fonte_personalizada)
stilo.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

treeview_fechamento = ttk.Treeview(fechamento_frame, columns=(1,2,3,4), show="headings", style="mystyle.Treeview", height=25)
treeview_fechamento.heading("1",text="Produtos")
treeview_fechamento.column("1", width=180)
treeview_fechamento.heading("2",text="Descrição")
treeview_fechamento.column("2", width=180)
treeview_fechamento.heading("3",text="Quantidade")
treeview_fechamento.column("3", width=180)
treeview_fechamento.heading("4",text="Preço da Venda")
treeview_fechamento.column("4", width=180)

treeview_fechamento.pack()

janela_principal.mainloop()
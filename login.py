from tkinter import *
from sistemas import Sistema

class loginJanela:
    
    def __init__(self):

        self.Janela = Tk()
        self.Janela.title('IMOBILIÁRIA SK')
        self.Janela.iconbitmap('icone.ico')
    
        self.fontePadrao = ('Arial', "10")
        self.container1 = Frame(self.Janela)
        self.container1['pady'] = 20
        self.container1.pack()

        self.containerDados1 = Frame(self.Janela)
        self.containerDados1['padx'] = 50
        self.containerDados1.pack()

        self.containerDados2 = Frame(self.Janela)
        self.containerDados2['padx'] = 50
        self.containerDados2.pack()

        self.containerBotao = Frame(self.Janela)
        self.containerBotao['pady'] = 30
        self.containerBotao.pack()

        self.titulo = Label(self.container1, text='LOGIN')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.loginId = Label(self.containerDados1, text='ID:')
        self.loginId['font'] = self.fontePadrao
        self.loginId.pack()

        self.usuario = Entry(self.containerDados1)
        self.usuario["width"] = 30
        self.usuario.pack()

        self.loginSenha = Label(self.containerDados2, text='Senha:')
        self.loginSenha['font'] = self.fontePadrao
        self.loginSenha.pack()

        self.senha = Entry(self.containerDados2, show='*')
        self.senha.bind('<Return>', self.verificaSenhaEnter)
        self.senha["width"] = 30
        self.senha.pack()

        self.botao = Button(self.containerBotao, text='Entrar')
        self.botao['font'] = ('Calibri', '10')
        self.botao['width'] = 12
        self.botao['command'] = self.verificaSenhaClick
        self.botao.pack()
        self.mensagem = Label(self.containerBotao, text='', font=self.fontePadrao)
        self.mensagem.pack()

        self.Janela.mainloop()

    def abreSistema(self):

        self.Janela.destroy()
        Sistema()


    def verificaSenhaClick(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        if usuario == '' and senha == '':
            self.mensagem['text'] = 'Autenticado'
            self.abreSistema()

        else:
            self.mensagem['text'] = 'Erro na autenticação'



    def verificaSenhaEnter(self, event):
        usuario = self.usuario.get()
        senha = self.senha.get()
        if usuario == '' and senha == '':
            self.mensagem['text'] = 'Autenticado'
            self.abreSistema()

        else:
            self.mensagem['text'] = 'Erro na autenticação'


LJ = loginJanela()

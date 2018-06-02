from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from usuarios import Cliente
from imoveis import Imovel
from proprietarios import Proprietario
import subprocess
import datetime
import csv


class Sistema:
    def __init__(self):

        self.principal = Tk()
        self.principal.title('IMOBILIÁRIA SK')
        self.principal.iconbitmap('icone.ico')
        self.principal.wm_state('zoomed')
        self.fonte = ("Verdana", "8")
        
        dataatual = datetime.date.today()


###############################
###  Inicio do Menu Bar     ###
###############################

        self.menu = Menu(self.principal)

        self.menuPrincipal = Menu(self.menu)
        self.menuPrincipal.add_command(label='Sair', command=self.FechaSistemaMenu)
        self.menu.add_cascade(label='Principal', menu = self.menuPrincipal)

        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(label='Inquilinos', command=self.abreinquilinoMenu)
        self.menuCadastro.add_command(label='Proprietários', command=self.abreProprietarioMenu)
        self.menuCadastro.add_command(label='Imóveis', command=self.abreImoveisMenu)
        self.menu.add_cascade(label='Cadastro', menu = self.menuCadastro)

        self.menuPesquisar = Menu(self.menu)
        self.menuPesquisar.add_command(label='Pesquisar Inquilinos', command=self.abrePesquisa)
        self.menuPesquisar.add_command(label='Pesquisar Proprietários', command=self.abrePesquisa)
        self.menuPesquisar.add_command(label='Pesquisar Imóveis', command=self.abrePesquisa)
        self.menu.add_cascade(label='Pesquisar', menu = self.menuPesquisar)

        self.menuRelatorio = Menu(self.menu)
        self.menuRelatorio.add_command(label='Inquilino x Aluguel')
        self.menuRelatorio.add_command(label='Proprietário x Imóveis')
        self.menuRelatorio.add_command(label='Imóveis x Aluguel')
        self.menuRelatorio.add_command(label='Boletos emitidos')
        self.menuRelatorio.add_command(label='Alugueis em atraso')
        self.menuRelatorio.add_command(label='A receber')
        self.menu.add_cascade(label='Relatórios', menu = self.menuRelatorio)

        self.menuBoleto = Menu(self.menu)
        self.menuBoleto.add_command(label='Emissão de boleto')
        self.menu.add_cascade(label='Boleto', menu = self.menuBoleto)

        self.menuSuporte = Menu(self.menu)
        self.menuSuporte.add_command(label='Suporte Team Viewer', command=self.abreTeamViewer)
        self.menuSuporte.add_command(label='Suporte Email')
        self.menu.add_cascade(label='Suporte', menu = self.menuSuporte)

        self.principal.config(menu = self.menu)

        ##############################
        ###       FIM Menu Bar     ###
        ##############################

###################################
###     Inicio frames corpo     ###
###################################
        self.scrollbar = Scrollbar()
        self.scrollbar.grid(column=3, row=0, stick='NSEW')

        self.frameSuperior = Frame(self.principal)
        self.frameSuperior.grid_columnconfigure(1, weight=1)
        self.frameSuperior.grid(column=0,row=0, stick="NSEW")

        self.frameLateral = Frame(self.frameSuperior)
        self.frameLateral.grid(column = 0, row=0, stick='NSEW')

        background = PhotoImage(file ='SK.png')
        self.frameMeio = LabelFrame(self.frameSuperior)
        back = Label(self.frameMeio, image=background)
        back.place(x=0, y=0, relwidth=1, relheight=1)
        back.grid(column=1, stick='NSEW')
        self.frameMeio.grid_rowconfigure(0, weight = 1)
        self.frameMeio.grid_columnconfigure(1, weight = 1)
        self.frameMeio.grid(column= 1, row=0, stick='NSEW')

        ###################################
        ###      FIM frames corpo      ####
        ###################################

        
##################################
##   Inicio frame Status Bar    ##
##################################        

        self.statusBar = Label(self.principal, relief=SUNKEN, anchor=W)
        self.statusBar.grid(column=0 ,row=1, stick="NSEW")

        ###########################
        ##     FIM frame         ##
        ###########################
    
    
###########################################
###   Inicio frame Cadastro Imoveis     ###
###########################################
        self.frameImoveis = LabelFrame(self.frameMeio)
        self.frameImoveis.grid_columnconfigure(1, weight = 1)
        self.frameImoveis.grid_configure(columnspan=2)
        self.frameImoveis.grid(column=0, row=0, stick='NSEW')

        self.container1 = Frame(self.frameImoveis)
        self.container2 = Frame(self.frameImoveis)
        self.container3 = Frame(self.frameImoveis)
        self.container4 = Frame(self.frameImoveis)
        self.container5 = Frame(self.frameImoveis)
        self.container6 = Frame(self.frameImoveis)
        self.container7 = Frame(self.frameImoveis)
        self.container8 = Frame(self.frameImoveis)
        self.container9 = Frame(self.frameImoveis)
        self.container10 = Frame(self.frameImoveis)
        self.container11 = Frame(self.frameImoveis)
        self.container12 = Frame(self.frameImoveis)
        self.container13 = Frame(self.frameImoveis)
        self.container14 = Frame(self.frameImoveis)
        self.container15 = Frame(self.frameImoveis)
        self.container16 = Frame(self.frameImoveis)
        self.container17 = Frame(self.frameImoveis)

        self.container1["pady"] = 10
        self.container1.grid()
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.grid()
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.grid()
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.grid()
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.grid()
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.grid()
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.grid()
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.grid()
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.grid()

        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.grid()

        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.grid()

        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.grid()

        self.container13["padx"] = 20
        self.container13["pady"] = 5
        self.container13.grid()

        self.container14["padx"] = 20
        self.container14["pady"] = 5
        self.container14.grid()

        self.container17["padx"] = 20
        self.container17["pady"] = 5
        self.container17.grid()

        self.container15["padx"] = 20
        self.container15["pady"] = 10
        self.container15.grid()

        self.container16["pady"] = 15
        self.container16.grid()

        self.titulo = Label(self.container1, text="Cadastro de Imóveis:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.grid()
        
        self.lblIdImovel = Label(self.container2, text="ID Imovel:", font=self.fonte, width=30)
        self.lblIdImovel.grid(column=0,row=1)
        
        self.txtIdImovel = ttk.Entry(self.container2)
        self.txtIdImovel["width"] = 5
        self.txtIdImovel["font"] = self.fonte
        self.txtIdImovel.grid(column=1,row=1)
        
        self.btnBuscar = ttk.Button(self.container2, text="Buscar")
        self.btnBuscar["command"] = self.buscarImovel
        self.btnBuscar.grid(column=2,row=1, padx=10)
        
        self.lblDataCadastro = Label(self.container3, text="Data de cadastro:", font=self.fonte, width=30)
        self.lblDataCadastro.grid(column=0,row=2)
        
        self.txtDataCadastro = ttk.Entry(self.container3)
        self.txtDataCadastro["width"] = 40
        self.txtDataCadastro["font"] = self.fonte
        self.txtDataCadastro.grid(column=1,row=2)
        self.txtDataCadastro.delete(0, END)
        self.txtDataCadastro.insert(0, (f'{dataatual}'))
    

        self.lblIdProprietario = Label(self.container4, text="ID Proprietario:", font=self.fonte, width=30)
        self.lblIdProprietario.grid(column=0, row=3)


        self.txtIdProprietarioImovel = ttk.Entry(self.container4)
        self.txtIdProprietarioImovel["width"] = 40
        self.txtIdProprietarioImovel["font"] = self.fonte
        self.txtIdProprietarioImovel.grid(column=1, row=3)
        
        self.lblAreaUtil= Label(self.container5, text="Área util:", font=self.fonte, width=30)
        self.lblAreaUtil.grid(column=0, row=4)
        
        self.txtAreaUtil = ttk.Entry(self.container5)
        self.txtAreaUtil["width"] = 40
        self.txtAreaUtil["font"] = self.fonte
        self.txtAreaUtil.grid(column=1, row=4)
        
        self.lblAreaTotal = Label(self.container6, text="Área total:", font=self.fonte, width=30)
        self.lblAreaTotal.grid(column=0,row=5)
        
        self.txtAreaTotal = ttk.Entry(self.container6)
        self.txtAreaTotal["width"] = 40
        self.txtAreaTotal["font"] = self.fonte
        self.txtAreaTotal.grid(column=1,row=5)
        
        self.lblVlrVenda= Label(self.container7, text="Valor de venda:", font=self.fonte, width=30)
        self.lblVlrVenda.grid(column=0, row=6)
        
        self.txtVlrVenda = ttk.Entry(self.container7)
        self.txtVlrVenda["width"] = 40
        self.txtVlrVenda["font"] = self.fonte
        self.txtVlrVenda.grid(column=1, row=6)

        self.lblVlrAluguel = Label(self.container8, text="Valor de aluguel:", font=self.fonte, width=30)
        self.lblVlrAluguel.grid(column=0, row=7)
        
        self.txtVlrAluguel = ttk.Entry(self.container8)
        self.txtVlrAluguel["width"] = 40
        self.txtVlrAluguel["font"] = self.fonte
        self.txtVlrAluguel.grid(column=1, row=7)

        self.lblVlrIPTU = Label(self.container9, text="Valor do IPTU:", font=self.fonte, width=30)
        self.lblVlrIPTU.grid(column=0, row=8)
        
        self.txtVlrIPTU = ttk.Entry(self.container9)
        self.txtVlrIPTU["width"] = 40
        self.txtVlrIPTU["font"] = self.fonte
        self.txtVlrIPTU.grid(column=1, row=8)

        self.lblVlrCondominio= Label(self.container10, text="Valor do Condominio:", font=self.fonte, width=30)
        self.lblVlrCondominio.grid(column=0, row=9)
        
        self.txtVlrCondominio = ttk.Entry(self.container10)
        self.txtVlrCondominio["width"] = 40
        self.txtVlrCondominio["font"] = self.fonte
        self.txtVlrCondominio.grid(column=1, row=9)

        self.lblNumRelogioAES= Label(self.container11, text="Número do relógio AES:", font=self.fonte, width=30)
        self.lblNumRelogioAES.grid(column=0, row=10)
        
        self.txtNumRelogioAES = ttk.Entry(self.container11)
        self.txtNumRelogioAES["width"] = 40
        self.txtNumRelogioAES["font"] = self.fonte
        self.txtNumRelogioAES.grid(column=1, row=10)

        self.lblNumRelogioSABESP= Label(self.container12, text="Número do relógio SABESP:", font=self.fonte, width=30)
        self.lblNumRelogioSABESP.grid(column=0, row=11)
        
        self.txtNumRelogioSABESP = ttk.Entry(self.container12)
        self.txtNumRelogioSABESP["width"] = 40
        self.txtNumRelogioSABESP["font"] = self.fonte
        self.txtNumRelogioSABESP.grid(column=1, row=11)

        self.lblNumSeguro= Label(self.container13, text="Número do Seguro:", font=self.fonte, width=30)
        self.lblNumSeguro.grid(column=0, row=12)
        
        self.txtNumSeguro = ttk.Entry(self.container13)
        self.txtNumSeguro["width"] = 40
        self.txtNumSeguro["font"] = self.fonte
        self.txtNumSeguro.grid(column=1, row=12)

        self.lblApolice= Label(self.container14, text="Apólice:", font=self.fonte, width=30)
        self.lblApolice.grid(column=0, row=13)
        
        self.txtApolice = ttk.Entry(self.container14)
        self.txtApolice["width"] = 40
        self.txtApolice["font"] = self.fonte
        self.txtApolice.grid(column=1, row=13)

        self.lblTipo= Label(self.container17, text="Tipo: ", font=self.fonte, width=30)
        self.lblTipo.grid(column=0, row=14)
        
        TipoEscolhas = ['Venda e Aluguel','Aluguel','Venda','Reforma']

        self.txtTipo = ttk.Combobox(self.container17, values=TipoEscolhas)
        self.txtTipo["width"] = 35
        self.txtTipo["font"] = self.fonte
        self.txtTipo.grid(column=1, row=14)
        
        self.bntInsert = Button(self.container15, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirImovel
        self.bntInsert.grid (column=0, row=16)
        
        self.bntAlterar = Button(self.container15, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarImovel
        self.bntAlterar.grid (column=1, row=16)
        
        self.bntExcluir = Button(self.container15, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirImovel
        self.bntExcluir.grid(column=2, row=16)
        
        self.lblmsgimovel = Label(self.container16, text="")
        self.lblmsgimovel["font"] = ("Verdana", "9", "italic")
        self.lblmsgimovel.grid(column=0, row=18)


        ###########################################
        ###   fim  frame Cadastro imovel        ###
        ###########################################


############################################
###   Inicio frame Cadastro Proprietario ###
############################################

        self.frameProprietario = LabelFrame(self.frameMeio)
        
        self.frameProprietario.columnconfigure(1, weight = 1)
        self.frameProprietario.grid_configure(columnspan=2)
        self.frameProprietario.grid(column=0, row=0, stick='NSEW')

        self.container1 = Frame(self.frameProprietario)
        self.container2 = Frame(self.frameProprietario)
        self.container3 = Frame(self.frameProprietario)
        self.container4 = Frame(self.frameProprietario)
        self.container5 = Frame(self.frameProprietario)
        self.container6 = Frame(self.frameProprietario)
        self.container7 = Frame(self.frameProprietario)
        self.container8 = Frame(self.frameProprietario)
        self.container9 = Frame(self.frameProprietario)
        self.container10 = Frame(self.frameProprietario)
        self.container11 = Frame(self.frameProprietario)
        self.container12 = Frame(self.frameProprietario)
        self.container13 = Frame(self.frameProprietario)
        self.container1["pady"] = 10
        self.container1.grid()
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.grid()
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.grid()
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.grid()
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.grid()
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.grid()
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.grid()
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.grid()
        self.container9["padx"] = 20
        self.container9["pady"] = 10
        self.container9.grid()
        self.container10["padx"] = 20
        self.container10["pady"] = 10
        self.container10.grid()
        self.container11["padx"] = 20
        self.container11["pady"] = 10
        self.container11.grid()
        self.container12["padx"] = 20
        self.container12["pady"] = 10
        self.container12.grid()
        self.container13["pady"] = 15
        self.container13.grid()

        self.titulo = Label(self.container1, text="Cadastro de Proprietário :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.grid ()
        
        self.lblIdProprietario = Label(self.container2, text="ID Proprietário:", font=self.fonte, width=20)
        self.lblIdProprietario.grid(column=0, row=1)
        
        self.txtIdProprietario = ttk.Entry(self.container2)
        self.txtIdProprietario["width"] = 5
        self.txtIdProprietario["font"] = self.fonte
        self.txtIdProprietario.grid(column=1, row=1)
        
        self.btnBuscar = ttk.Button(self.container2, text="Buscar")
        self.btnBuscar["command"] = self.buscarProprietarioID
        self.btnBuscar.grid(column=2, row=1, padx=10)
        
        self.lblNomeProprietario = Label(self.container3, text="Nome:", font=self.fonte, width=20)
        self.lblNomeProprietario.grid(column=0, row=2)
        
        self.txtNomeProprietario = ttk.Entry(self.container3)
        self.txtNomeProprietario["width"] = 40
        self.txtNomeProprietario["font"] = self.fonte
        self.txtNomeProprietario.grid(column=1, row=2)

        self.lblRGProprietario = Label(self.container4, text = "RG:", font=self.fonte, width=20)
        self.lblRGProprietario.grid(column=0, row=0)

        self.txtRGProprietario = ttk.Entry(self.container4)
        self.txtRGProprietario["width"] = 40
        self.txtRGProprietario["font"] = self.fonte
        self.txtRGProprietario.grid(column=1, row=0)

        self.lblCPFProprietario = Label(self.container5, text = "CPF:", font=self.fonte, width=20)
        self.lblCPFProprietario.grid(column=0, row=0)

        self.txtCPFProprietario = ttk.Entry(self.container5)
        self.txtCPFProprietario["width"] = 40
        self.txtCPFProprietario["font"] = self.fonte
        self.txtCPFProprietario.grid(column=1, row=0)

        
        self.lblTelefoneProprietario = Label(self.container6, text="Telefone:", font=self.fonte, width=20)
        self.lblTelefoneProprietario.grid(column=0, row=3)
        
        self.txtTelefoneProprietario = ttk.Entry(self.container6)
        self.txtTelefoneProprietario["width"] = 40
        self.txtTelefoneProprietario["font"] = self.fonte
        self.txtTelefoneProprietario.grid(column=1,row=3)
        
        self.lblEmailProprietario= Label(self.container7, text="E-mail:", font=self.fonte, width=20)
        self.lblEmailProprietario.grid(column=0, row=4)
        
        self.txtEmailProprietario = ttk.Entry(self.container7)
        self.txtEmailProprietario["width"] = 40
        self.txtEmailProprietario["font"] = self.fonte
        self.txtEmailProprietario.grid(column=1, row=4)
        
        self.lblIdContrato = Label(self.container8, text="ID Contrato:", font=self.fonte, width=20)
        self.lblIdContrato.grid(column=0, row=5)
        
        self.txtIdContratoProp = ttk.Entry(self.container8)
        self.txtIdContratoProp["width"] = 40
        self.txtIdContratoProp["font"] = self.fonte
        self.txtIdContratoProp.grid(column=1, row=5)

        self.lblEnderecoProprietario = Label(self.container9, text="Endereço:", font=self.fonte, width=20)
        self.lblEnderecoProprietario.grid(column = 0, row= 7)
        
        self.txtEnderecoProprietario = ttk.Entry(self.container9)
        self.txtEnderecoProprietario["width"] = 40
        self.txtEnderecoProprietario["font"] = self.fonte
        self.txtEnderecoProprietario.grid(column =1, row=7)

        self.lblDataProprietario = Label(self.container10, text="Data de cadastro:", font=self.fonte, width=20)
        self.lblDataProprietario.grid(column = 0, row= 7)
        
        self.txtDataProprietario = ttk.Entry(self.container10)
        self.txtDataProprietario["width"] = 40
        self.txtDataProprietario["font"] = self.fonte
        self.txtDataProprietario.grid(column =1, row=7)
        self.txtDataProprietario.delete(0, END)
        self.txtDataProprietario.insert(0, dataatual)
        
        self.lblIdImoveis = Label(self.container11, text="Id Imoveis:", font=self.fonte, width=20)
        self.lblIdImoveis.grid(column=0, row=1)
        
        self.txtIdImoveis = ttk.Entry(self.container11)
        self.txtIdImoveis['width'] = 40
        self.txtIdImoveis['font'] = self.fonte
        self.txtIdImoveis.grid(column=1, row=1)

        self.bntInsert = Button(self.container12, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirProprietario
        self.bntInsert.grid (column = 0, row = 8)
        
        self.bntAlterar = Button(self.container12, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarProprietario
        self.bntAlterar.grid (column = 1, row= 8)
        
        self.bntExcluir = Button(self.container12, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirProprietario
        self.bntExcluir.grid(column = 2, row = 8)
        
        self.lblmsgProprietario = Label(self.container13, text="")
        self.lblmsgProprietario["font"] = ("Verdana", "9", "italic")
        self.lblmsgProprietario.grid()

        ###########################################
        ###   fim  frame Cadastro Proprietario  ###
        ###########################################
        

###########################################
###   Inicio frame Cadastro inquilino   ###
###########################################
      
        self.frameInquilino = LabelFrame(self.frameMeio)
        
        self.frameInquilino.columnconfigure(1, weight = 1)
        self.frameInquilino.grid_configure(columnspan=2)
        self.frameInquilino.grid(column=0, row=0, stick='NSEW')

        self.container1 = Frame(self.frameInquilino)
        self.container2 = Frame(self.frameInquilino)
        self.container3 = Frame(self.frameInquilino)
        self.container4 = Frame(self.frameInquilino)
        self.container5 = Frame(self.frameInquilino)
        self.container6 = Frame(self.frameInquilino)
        self.container7 = Frame(self.frameInquilino)
        self.container8 = Frame(self.frameInquilino)
        self.container9 = Frame(self.frameInquilino)
        self.container10 = Frame(self.frameInquilino)
        self.container11 = Frame(self.frameInquilino)
        self.container12 = Frame(self.frameInquilino)
        self.container13 = Frame(self.frameInquilino)

        self.container1["pady"] = 10
        self.container1.grid()
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.grid()
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.grid()
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.grid()
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.grid()
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.grid()
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.grid()
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.grid()
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.grid()
        self.container10["padx"] = 20
        self.container10["pady"] = 10
        self.container10.grid()
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.grid()
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.grid()
        self.container13['padx'] = 20
        self.container13['pady'] = 15
        self.container13.grid()

        self.titulo = Label(self.container1, text="Cadastro Inquilino / Cliente:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.grid()
        
        self.lblIdUsuario = Label(self.container2, text="ID Usuario:", font=self.fonte, width=20)
        self.lblIdUsuario.grid(column=0, row=1)
        
        self.txtIdUsuario = ttk.Entry(self.container2)
        self.txtIdUsuario["width"] = 5
        self.txtIdUsuario["font"] = self.fonte
        self.txtIdUsuario.grid(column=1, row=1)
        
        self.btnBuscar = ttk.Button(self.container2, text="Buscar")
        self.btnBuscar["command"] = self.buscarClienteID
        self.btnBuscar.grid(column=2,row=1, padx=10)
        
        self.lblNome = Label(self.container3, text="Nome:", font=self.fonte, width=20)
        self.lblNome.grid(column=0, row=2)
        
        self.txtNome = ttk.Entry(self.container3)
        self.txtNome["width"] = 40
        self.txtNome["font"] = self.fonte
        self.txtNome.grid(column=1, row=2)

        self.lblDataCadastro = Label(self.container4, text="Data de cadastro: ", font=self.fonte, width=20)
        self.lblDataCadastro.grid(column=0, row=3)

        self.txtDataCadastro = ttk.Entry(self.container4, width=45)
        self.txtDataCadastro.grid(column=1, row=3)
        self.txtDataCadastro.delete(0, END)
        self.txtDataCadastro.insert(0, dataatual)

        self.lblRG= Label(self.container5, text="RG:", font=self.fonte, width=20)
        self.lblRG.grid(column=0,row=4)
        
        self.txtRG = ttk.Entry(self.container5)
        self.txtRG["width"] = 40
        self.txtRG["font"] = self.fonte
        self.txtRG.grid(column=1,row=4)

        self.lblCPF = Label(self.container6, text="CPF:", font=self.fonte, width=20)
        self.lblCPF.grid(column=0,row=5)
        
        self.txtCPF = ttk.Entry(self.container6)
        self.txtCPF["width"] = 40
        self.txtCPF["font"] = self.fonte
        self.txtCPF.grid(column=1,row=5)

        self.lblEndereco = Label(self.container7, text='Endereço:', font=self.fonte, width=20)
        self.lblEndereco.grid(column=0, row=6)

        self.txtEndereco = ttk.Entry(self.container7)
        self.txtEndereco['width'] = 40
        self.txtEndereco['font'] = self.fonte
        self.txtEndereco.grid(column=1,row=6)

        
        self.lblTelefone = Label(self.container8, text="Telefone:", font=self.fonte, width=20)
        self.lblTelefone.grid(column=0,row=6)
        
        self.txtTelefone = ttk.Entry(self.container8)
        self.txtTelefone["width"] = 40
        self.txtTelefone["font"] = self.fonte
        self.txtTelefone.grid(column=1,row=6)
        
        self.lblEmail= Label(self.container9, text="E-mail:", font=self.fonte, width=20)
        self.lblEmail.grid(column=0, row=7)
        
        self.txtEmail = ttk.Entry(self.container9)
        self.txtEmail["width"] = 40
        self.txtEmail["font"] = self.fonte
        self.txtEmail.grid(column=1,row=7)
        
        self.lblIdContrato= Label(self.container10, text="ID Contrato:", font=self.fonte, width=20)
        self.lblIdContrato.grid(column=0,row=8)
        
        self.txtIdContrato = ttk.Entry(self.container10)
        self.txtIdContrato["width"] = 40
        self.txtIdContrato["font"] = self.fonte
        self.txtIdContrato.grid(column=1,row=8)
        
        self.lblTipo= Label(self.container11, text="Tipo:", font=self.fonte, width=20)
        self.lblTipo.grid(column=0,row=9)
        
        tipoCliente = ['Aluguel','Compra']

        self.txtTipo = ttk.Combobox(self.container11, values=tipoCliente)
        self.txtTipo["width"] = 30
        self.txtTipo["font"] = self.fonte
        self.txtTipo.grid(column=1,row=9)
        
        self.bntInsert = Button(self.container12, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirCliente
        self.bntInsert.grid (column=0,row=10)
        
        self.bntAlterar = Button(self.container12, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarCliente
        self.bntAlterar.grid (column=1,row=10)
        
        self.bntExcluir = Button(self.container12, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirCliente
        self.bntExcluir.grid(column=2, row=10)
        
        self.lblmsg = Label(self.container13, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.grid()

        ##############################################
        ###   Termino do frame Inquilino           ###
        ##############################################


###########################################
###        Inicio frame Lateral         ###
###########################################

        self.LatCadastroInq = ttk.Button(self.frameLateral, text='Cadastro Inquilino')
        self.LatCadastroInq['width'] = 20
        self.LatCadastroInq['padding'] = 30
        self.LatCadastroInq.bind('<1>', self.abreinquilino)
        self.LatCadastroInq.grid(column=0,row=0)

        self.LatCadastroImoveis = ttk.Button(self.frameLateral, text='Cadastro Imóveis')
        self.LatCadastroImoveis['width'] = 20
        self.LatCadastroImoveis['padding'] = 30
        self.LatCadastroImoveis.bind('<1>', self.abreImoveis)
        self.LatCadastroImoveis.grid(column=0,row=1)

        self.LatCadastroProprietario = ttk.Button(self.frameLateral, text='Cadastro Proprietário')
        self.LatCadastroProprietario['width'] = 20
        self.LatCadastroProprietario['padding'] = 30
        self.LatCadastroProprietario.bind('<1>', self.abreProprietario)
        self.LatCadastroProprietario.grid(column=0,row=2)

        self.LatRelatorios = ttk.Button(self.frameLateral, text='Relatórios')
        self.LatRelatorios['width'] = 20
        self.LatRelatorios['padding'] = 30
        self.LatRelatorios.grid(column=0,row=3)

        self.LatBoletos = ttk.Button(self.frameLateral, text='Boletos')
        self.LatBoletos['width'] = 20
        self.LatBoletos['padding'] = 30
        self.LatBoletos.grid(column=0,row=4)

        self.espacoBranco = Label(self.frameLateral, text= '')
        self.espacoBranco['width'] = 20
        self.espacoBranco['pady'] = 70
        self.espacoBranco.grid(column=0,row=5)

        self.LatSair = ttk.Button(self.frameLateral, text='Sair')
        self.LatSair['width'] = 20
        self.LatSair['padding'] = 30
        self.LatSair.bind('<1>', self.FechaSistema)
        self.LatSair.grid(column=0,row=6)

        self.set('################################################################            SOFTWARE produzido por Jefferson Kwak. Todos os direitos reservados.          ################################################################')


        ###########################################
        ###           Fim frame Lateral         ###
        ###########################################
        

#inicio do loop programa#
        
        back.lift()
        self.principal.mainloop()


###########################################
###       Inicio Janela Pesquisa        ###
###########################################

    def abrePesquisa(self):
        self.Pesquisa = Toplevel(self.frameMeio)
        self.Pesquisa.title('Pesquisar')
        self.Pesquisa.iconbitmap('icone.ico')
        self.frameNote = ttk.Notebook(self.Pesquisa)
        self.painel1 = Frame(self.frameNote)
        self.painel2 = Frame(self.frameNote)
        self.painel3 = Frame(self.frameNote)
        
        self.frameNote.add(self.painel1, text='Inquilino ou Cliente')
        self.frameNote.add(self.painel2, text='Imoveis')
        self.frameNote.add(self.painel3, text='Proprietario')


###Note1
        Label(self.painel1, text='Digite um nome: ').grid(row=0,column=0,pady=5)
        self.entpes = ttk.Entry(self.painel1,width=50)
        self.entpes.grid(row=0,column=1,pady=5)
        self.btn2 = Button(self.painel1,text='Pesquisar', width=20, command=self.buscarClienteNome)
        self.btn2.grid(row=0,column=2,pady=5)
        self.btn3 = Button(self.painel1,text='Apagar selecionado',width=20)
        self.btn3.grid(row=3,column=0,columnspan=3,pady=5)
        self.btn4 = Button(self.painel1,text='Exportar BD',width=20)
        self.btn4.grid(row=3,column=1,columnspan=3,pady=5)
        #Treeview dos resultados
        self.lista = ttk.Treeview(self.painel1,columns=('ID','NOME','RG','CPF',
                                                    'ENDEREÇO', 'TELEFONE','E-MAIL', 'OBS'),height=8)
        #tamanho de cada coluna
        self.lista.column('ID',width=50,minwidth=50,stretch=False)
        self.lista.column('NOME',width=100,minwidth=100,stretch=False)        
        self.lista.column('DATA DE CADASTRO',width=100,minwidth=100,stretch=False)
        self.lista.column('RG',width=100,minwidth=100,stretch=False)
        self.lista.column('CPF',width=100,minwidth=100,stretch=False)
        self.lista.column('ENDEREÇO',width=100,minwidth=100,stretch=False)
        self.lista.column('TELEFONE',width=100,minwidth=100,stretch=False)
        self.lista.column('E-MAIL',width=100,minwidth=100,stretch=False)
        self.lista.column('CONTRATO',width=140,minwidth=140,stretch=False)
        #exibição de cada coluna
        self.lista['show'] = 'headings'
        self.lista.heading('ID', text='ID')
        self.lista.heading('NOME', text='NOME')
        self.lista.heading('DATA DE CADASTRO', text='DATA CADASTRO')
        self.lista.heading('RG', text='RG')
        self.lista.heading('CPF', text='CPF')
        self.lista.heading('ENDEREÇO', text='ENDEREÇO')
        self.lista.heading('TELEFONE', text='TELEFONE')
        self.lista.heading('E-MAIL', text='E-MAIL')
        self.lista.heading('CONTRATO', text='OBS')
        
        self.lista.grid(row=1,column=0,columnspan=4,pady=5,padx=5)
        self.scrol2 = Scrollbar(self.painel1,command=self.lista.yview)
        self.scrol2.grid(row=1,column=5,pady=5,sticky='ns')
        self.scrol3 = Scrollbar(self.painel1,command=self.lista.xview,
                                orient='horizontal')
        self.scrol3.grid(row=2,column=0,columnspan=4,pady=5,sticky='we')
        self.lista.configure(xscrollcommand=self.scrol3.set)
        self.lista.configure(yscrollcommand=self.scrol2.set)

###Note2
        Label(self.painel2, text='Digite um nome: ').grid(row=0,column=0,pady=5)
        self.entpes = ttk.Entry(self.painel2,width=50)
        self.entpes.grid(row=0,column=1,pady=5)
        self.btn2 = Button(self.painel2,text='Pesquisar',
                           width=20)
        self.btn2.grid(row=0,column=2,pady=5)
        self.btn3 = Button(self.painel2,text='Apagar selecionado',width=20)
        self.btn3.grid(row=3,column=0,columnspan=3,pady=5)
        self.btn4 = Button(self.painel2,text='Exportar BD',width=20)
        self.btn4.grid(row=3,column=1,columnspan=3,pady=5)
        #Treeview dos resultados
        self.lista = ttk.Treeview(self.painel2,columns=('ID','NOME','RG','CPF',
                                                    'ENDEREÇO','Nº CASA',
                                                    'TELEFONE','CELULAR',
                                                    'E-MAIL', 'OBS'),height=8)
        #tamanho de cada coluna
        self.lista.column('ID',width=50,minwidth=50,stretch=False)
        self.lista.column('NOME',width=100,minwidth=100,stretch=False)
        self.lista.column('RG',width=100,minwidth=100,stretch=False)
        self.lista.column('CPF',width=100,minwidth=100,stretch=False)
        self.lista.column('ENDEREÇO',width=100,minwidth=100,stretch=False)
        self.lista.column('Nº CASA',width=100,minwidth=100,stretch=False)
        self.lista.column('TELEFONE',width=100,minwidth=100,stretch=False)
        self.lista.column('CELULAR',width=100,minwidth=100,stretch=False)
        self.lista.column('E-MAIL',width=100,minwidth=100,stretch=False)
        self.lista.column('OBS',width=140,minwidth=140,stretch=False)
        #exibição de cada coluna
        self.lista['show'] = 'headings'
        self.lista.heading('ID', text='ID')
        self.lista.heading('NOME', text='NOME')
        self.lista.heading('RG', text='RG')
        self.lista.heading('CPF', text='CPF')
        self.lista.heading('ENDEREÇO', text='ENDEREÇO')
        self.lista.heading('Nº CASA', text='Nº CASA')
        self.lista.heading('TELEFONE', text='TELEFONE')
        self.lista.heading('CELULAR', text='CELULAR')
        self.lista.heading('E-MAIL', text='E-MAIL')
        self.lista.heading('OBS', text='OBS')
        
        self.lista.grid(row=1,column=0,columnspan=4,pady=5,padx=5)
        self.scrol2 = Scrollbar(self.painel2,command=self.lista.yview)
        self.scrol2.grid(row=1,column=5,pady=5,sticky='ns')
        self.scrol3 = Scrollbar(self.painel2,command=self.lista.xview,
                                orient='horizontal')
        self.scrol3.grid(row=2,column=0,columnspan=4,pady=5,sticky='we')
        self.lista.configure(xscrollcommand=self.scrol3.set)
        self.lista.configure(yscrollcommand=self.scrol2.set)

        self.frameNote.grid(column=0, row=0)

###Note3
        Label(self.painel3, text='Digite um nome: ').grid(row=0,column=0,pady=5)
        self.entpes = ttk.Entry(self.painel3,width=50)
        self.entpes.grid(row=0,column=1,pady=5)
        self.btn2 = Button(self.painel3,text='Pesquisar',
                           width=20)
        self.btn2.grid(row=0,column=2,pady=5)
        self.btn3 = Button(self.painel3,text='Apagar selecionado',width=20)
        self.btn3.grid(row=3,column=0,columnspan=3,pady=5)
        self.btn4 = Button(self.painel3,text='Exportar BD',width=20)
        self.btn4.grid(row=3,column=1,columnspan=3,pady=5)
        #Treeview dos resultados
        self.lista = ttk.Treeview(self.painel3,columns=('ID','NOME','RG','CPF',
                                                    'ENDEREÇO','Nº CASA',
                                                    'TELEFONE','CELULAR',
                                                    'E-MAIL', 'OBS'),height=8)
        #tamanho de cada coluna
        self.lista.column('ID',width=50,minwidth=50,stretch=False)
        self.lista.column('NOME',width=100,minwidth=100,stretch=False)
        self.lista.column('RG',width=100,minwidth=100,stretch=False)
        self.lista.column('CPF',width=100,minwidth=100,stretch=False)
        self.lista.column('ENDEREÇO',width=100,minwidth=100,stretch=False)
        self.lista.column('Nº CASA',width=100,minwidth=100,stretch=False)
        self.lista.column('TELEFONE',width=100,minwidth=100,stretch=False)
        self.lista.column('CELULAR',width=100,minwidth=100,stretch=False)
        self.lista.column('E-MAIL',width=100,minwidth=100,stretch=False)
        self.lista.column('OBS',width=140,minwidth=140,stretch=False)
        #exibição de cada coluna
        self.lista['show'] = 'headings'
        self.lista.heading('ID', text='ID')
        self.lista.heading('NOME', text='NOME')
        self.lista.heading('RG', text='RG')
        self.lista.heading('CPF', text='CPF')
        self.lista.heading('ENDEREÇO', text='ENDEREÇO')
        self.lista.heading('Nº CASA', text='Nº CASA')
        self.lista.heading('TELEFONE', text='TELEFONE')
        self.lista.heading('CELULAR', text='CELULAR')
        self.lista.heading('E-MAIL', text='E-MAIL')
        self.lista.heading('OBS', text='OBS')
        
        self.lista.grid(row=1,column=0,columnspan=4,pady=5,padx=5)
        self.scrol2 = Scrollbar(self.painel3,command=self.lista.yview)
        self.scrol2.grid(row=1,column=5,pady=5,sticky='ns')
        self.scrol3 = Scrollbar(self.painel3,command=self.lista.xview,
                                orient='horizontal')
        self.scrol3.grid(row=2,column=0,columnspan=4,pady=5,sticky='we')
        self.lista.configure(xscrollcommand=self.scrol3.set)
        self.lista.configure(yscrollcommand=self.scrol2.set)

        self.frameNote.grid(column=0, row=0)
        
        

        

###Inicio dos metodos da classe####

    def abreImoveis(self, event):
       self.frameImoveis.lift()
    def abreImoveisMenu(self):
       self.frameImoveis.lift()


    def abreProprietario(self, event):
        self.frameProprietario.lift()
    def abreProprietarioMenu(self):
        self.frameProprietario.lift()


    def abreinquilino(self, event):
        self.frameInquilino.lift()
    def abreinquilinoMenu(self):
        self.frameInquilino.lift()


    def FechaSistema(self, event):
        self.principal.destroy()
    def FechaSistemaMenu(self):
        self.principal.destroy()


    def abreTeamViewer(self):
        subprocess.call(["C:/Users/Jefferson/GITHUB/Tkinter/TeamViewerQS.exe"])


    def set(self, format, *args):
        self.statusBar.config(text=format % args)
        self.statusBar.update_idletasks()

    def clear(self):
        self.statusBar.config(text="")
        self.statusBar.update_idletasks()


###Metodos Clientes###

    def inserirCliente(self):
        user = Cliente()
        
        user.Nome = self.txtNome.get().title()
        user.DataCadastro = self.txtDataCadastro.get()
        user.RG = self.txtRG.get()
        user.CPF = self.txtCPF.get()
        user.Endereco = self.txtEndereco.get()
        user.Telefone = self.txtTelefone.get()
        user.Email = self.txtEmail.get()
        user.IdContrato = self.txtIdContrato.get()
        user.Tipo = self.txtTipo.get()
        
        self.lblmsg["text"] = user.insertUser()
        
        self.txtIdUsuario.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtRG.delete(0, END)
        self.txtCPF.delete(0, END)
        self.txtEndereco.delete(0,END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtIdContrato.delete(0, END)
        self.txtTipo.delete(0, END) 
        
    def alterarCliente(self):
        user = Cliente()
        
        user.IdUsuario = self.txtIdUsuario.get()
        user.Nome = self.txtNome.get().title()
        user.DataCadastro = self.txtDataCadastro.get()
        user.RG = self.txtRG.get()
        user.CPF = self.txtCPF.get()
        user.Endereco = self.txtEndereco.get()
        user.Telefone = self.txtTelefone.get()
        user.Email = self.txtEmail.get()
        user.IdContrato = self.txtIdContrato.get()
        user.Tipo = self.txtTipo.get()
        
        self.lblmsg["text"] = user.updateUser()
        
        self.txtIdUsuario.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtRG.delete(0, END)
        self.txtCPF.delete(0, END)
        self.txtEndereco.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtIdContrato.delete(0, END)
        self.txtTipo.delete(0, END) 
          
    def excluirCliente(self):
        user = Cliente()
        
        user.IdUsuario = self.txtIdUsuario.get()
        
        self.lblmsg["text"] = user.deleteUser()
        
        self.txtIdUsuario.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtRG.delete(0, END)
        self.txtCPF.delete(0, END)
        self.txtEndereco.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtIdContrato.delete(0, END)
        self.txtTipo.delete(0, END) 
                
    def buscarClienteID(self):
        user = Cliente()
        
        IdUsuario = self.txtIdUsuario.get()
        
        self.lblmsg["text"] = user.selectUser(IdUsuario)
        
        self.txtNome.delete(0, END)
        self.txtNome.insert(INSERT, user.Nome)

        self.txtDataCadastro.delete(0, END)
        self.txtDataCadastro.insert(INSERT, user.DataCadastro)

        self.txtRG.delete(0, END)
        self.txtRG.insert(INSERT, user.RG)

        self.txtCPF.delete(0, END)
        self.txtCPF.insert(INSERT, user.CPF)

        self.txtEndereco.delete(0, END)
        self.txtEndereco.insert(INSERT, user.Endereco)
        
        self.txtTelefone.delete(0, END)
        self.txtTelefone.insert(INSERT,user.Telefone)
        
        self.txtEmail.delete(0, END)
        self.txtEmail.insert(INSERT, user.Email)
        
        self.txtIdContrato.delete(0, END)
        self.txtIdContrato.insert(INSERT, user.IdContrato)
        
        self.txtTipo.delete(0, END)
        self.txtTipo.insert(INSERT,user.Tipo)

    def buscarClienteNome(self):
        Nome = self.entpes.get()

###Metodos Imoveis####

    def inserirImovel(self):
        user = Imovel()
        
        user.DataCadastro = self.txtDataCadastro.get()
        user.IdProprietario = self.txtIdProprietarioImovel.get()
        user.AreaUtil = self.txtAreaUtil.get()
        user.AreaTotal = self.txtAreaTotal.get()
        user.VlrVenda = self.txtVlrVenda.get()
        user.VlrAluguel = self.txtVlrAluguel.get()
        user.VlrIPTU = self.txtVlrIPTU.get()
        user.VlrCondominio = self.txtVlrCondominio.get()
        user.NumRelogioAES = self.txtNumRelogioAES.get()
        user.NumRelogioSABESP = self.txtNumRelogioSABESP.get()
        user.NumSeguro = self.txtNumSeguro.get()
        user.Apolice = self.txtApolice.get()        
        user.Tipo = self.txtTipo.get()
        
        self.lblmsgimovel["text"] = user.insertImovel()
        
        self.txtDataCadastro.delete(0, END)
        self.txtIdProprietarioImovel.delete(0, END)
        self.txtAreaUtil.delete(0, END)
        self.txtAreaTotal.delete(0, END)
        self.txtVlrVenda.delete(0, END)
        self.txtVlrAluguel.delete(0, END)
        self.txtVlrIPTU.delete(0, END)
        self.txtVlrCondominio.delete(0, END) 
        self.txtNumRelogioAES.delete(0, END)
        self.txtNumRelogioSABESP.delete(0,END)
        self.txtNumSeguro.delete(0,END)
        self.txtApolice.delete(0, END)
        self.txtTipo.delete(0, END)
        
    def alterarImovel(self):
        user = Imovel()
        
        user.IdImovel = self.txtIdImovel.get()
        user.DataCadastro = self.txtDataCadastro.get()
        user.IdProprietario = self.txtIdProprietarioImovel.get()
        user.AreaUtil = self.txtAreaUtil.get()
        user.AreaTotal = self.txtAreaTotal.get()
        user.VlrVenda = self.txtVlrVenda.get()
        user.VlrAluguel = self.txtVlrAluguel.get()
        user.VlrIPTU = self.txtVlrIPTU.get()
        user.VlrCondominio = self.txtVlrCondominio.get()
        user.NumRelogioAES = self.txtNumRelogioAES.get()
        user.NumRelogioSABESP = self.txtNumRelogioSABESP.get()
        user.NumSeguro = self.txtNumSeguro.get()
        user.Apolice = self.txtApolice.get()        
        user.Tipo = self.txtTipo.get()
        
        self.lblmsgimovel["text"] = user.updateImovel()
        
        self.txtDataCadastro.delete(0, END)
        self.txtIdProprietarioImovel.delete(0, END)
        self.txtAreaUtil.delete(0, END)
        self.txtAreaTotal.delete(0, END)
        self.txtVlrVenda.delete(0, END)
        self.txtVlrAluguel.delete(0, END)
        self.txtVlrIPTU.delete(0, END)
        self.txtVlrCondominio.delete(0, END) 
        self.txtNumRelogioAES.delete(0, END)
        self.txtNumRelogioSABESP.delete(0,END)
        self.txtNumSeguro.delete(0,END)
        self.txtApolice.delete(0, END)
        self.txtTipo.delete(0, END)
          
    def excluirImovel(self):
        user = Imovel()
        
        user.IdImovel = self.txtIdImovel.get()
        
        self.lblmsgimovel["text"] = user.deleteImovel()
        
        self.txtDataCadastro.delete(0, END)
        self.txtIdProprietarioImovel.delete(0, END)
        self.txtAreaUtil.delete(0, END)
        self.txtAreaTotal.delete(0, END)
        self.txtVlrVenda.delete(0, END)
        self.txtVlrAluguel.delete(0, END)
        self.txtVlrIPTU.delete(0, END)
        self.txtVlrCondominio.delete(0, END) 
        self.txtNumRelogioAES.delete(0, END)
        self.txtNumRelogioSABESP.delete(0,END)
        self.txtNumSeguro.delete(0,END)
        self.txtApolice.delete(0, END)
        self.txtTipo.delete(0, END)

    def buscarImovel(self):
        user = Imovel()
        
        IdImovel = self.txtIdImovel.get()
        
        self.lblmsgimovel["text"] = user.selectImovel(IdImovel)
        
        self.txtDataCadastro.delete(0, END)
        self.txtDataCadastro.insert(INSERT, user.DataCadastro)

        self.txtIdProprietarioImovel.delete(0, END)
        self.txtIdProprietarioImovel.insert(INSERT, user.IdProprietario)

        self.txtAreaUtil.delete(0, END)
        self.txtAreaUtil.insert(INSERT, user.AreaUtil)

        self.txtAreaTotal.delete(0, END)
        self.txtAreaTotal.insert(INSERT, user.AreaTotal)
        
        self.txtVlrVenda.delete(0, END)
        self.txtVlrVenda.insert(INSERT,user.VlrVenda)
        
        self.txtVlrAluguel.delete(0, END)
        self.txtVlrAluguel.insert(INSERT, user.VlrAluguel)
        
        self.txtVlrIPTU.delete(0, END)
        self.txtVlrIPTU.insert(INSERT, user.VlrIPTU)

        self.txtVlrCondominio.delete(0, END)
        self.txtVlrCondominio.insert(INSERT, user.VlrCondominio)

        self.txtNumRelogioAES.delete(0, END)
        self.txtNumRelogioAES.insert(INSERT, user.NumRelogioAES)

        self.txtNumRelogioSABESP.delete(0, END)
        self.txtNumRelogioSABESP.insert(INSERT, user.NumRelogioSABESP)

        self.txtNumSeguro.delete(0, END)
        self.txtNumSeguro.insert(INSERT, user.NumSeguro)

        self.txtApolice.delete(0, END)
        self.txtApolice.insert(INSERT, user.Apolice)
        
        self.txtTipo.delete(0, END)
        self.txtTipo.insert(INSERT,user.Tipo)

###MEtodos Proprietário###

    def inserirProprietario(self):
        user = Proprietario()
        
        user.NomeProprietario = self.txtNomeProprietario.get().title()
        user.RGProprietario = self.txtRGProprietario.get()
        user.CPFProprietario = self.txtCPFProprietario.get()
        user.TelefoneProprietario = self.txtTelefoneProprietario.get()
        user.EmailProprietario = self.txtEmailProprietario.get()
        user.IdContrato = self.txtIdContratoProp.get()
        user.EnderecoProprietario = self.txtEnderecoProprietario.get()
        user.DataProprietario = self.txtDataProprietario.get()
        user.IdImoveis = self.txtIdImoveis.get()
        
        self.lblmsgProprietario["text"] = user.insertProprietario()
        
        self.txtNomeProprietario.delete(0, END)
        self.txtRGProprietario.delete(0, END)
        self.txtCPFProprietario.delete(0, END)
        self.txtTelefoneProprietario.delete(0, END)
        self.txtEmailProprietario.delete(0, END)
        self.txtIdContratoProp.delete(0, END)
        self.txtEnderecoProprietario.delete(0, END)
        self.txtDataProprietario.delete(0, END) 
        self.txtIdImoveis.delete(0, END)
        
    def alterarProprietario(self):
        user = Proprietario()
        
        user.IdProprietario = self.txtIdProprietario.get()
        user.NomeProprietario = self.txtNomeProprietario.get().title()
        user.RGProprietario = self.txtRGProprietario.get()
        user.CPFProprietario = self.txtCPFProprietario.get()
        user.TelefoneProprietario = self.txtTelefoneProprietario.get()
        user.EmailProprietario = self.txtEmailProprietario.get()
        user.IdContrato = self.txtIdContratoProp.get()
        user.EnderecoProprietario = self.txtEnderecoProprietario.get()
        user.DataProprietario = self.txtDataProprietario.get()
        user.IdImoveis = self.txtIdImoveis.get()
        
        self.lblmsgProprietario["text"] = user.updateProprietario()
        
        self.txtNomeProprietario.delete(0, END)
        self.txtRGProprietario.delete(0, END)
        self.txtCPFProprietario.delete(0, END)
        self.txtTelefoneProprietario.delete(0, END)
        self.txtEmailProprietario.delete(0, END)
        self.txtIdContratoProp.delete(0, END)
        self.txtEnderecoProprietario.delete(0, END)
        self.txtDataProprietario.delete(0, END) 
        self.txtIdImoveis.delete(0, END)
          
    def excluirProprietario(self):
        user = Proprietario()
        
        user.IdProprietario = self.txtIdProprietario.get()
        
        self.lblmsgProprietario["text"] = user.deleteProprietario()
        
        self.txtNomeProprietario.delete(0, END)
        self.txtRGProprietario.delete(0, END)
        self.txtCPFProprietario.delete(0, END)
        self.txtTelefoneProprietario.delete(0, END)
        self.txtEmailProprietario.delete(0, END)
        self.txtIdContratoProp.delete(0, END)
        self.txtEnderecoProprietario.delete(0, END)
        self.txtDataProprietario.delete(0, END) 
        self.txtIdImoveis.delete(0, END)

    def buscarProprietarioID(self):
        user = Proprietario()
        
        IdProprietario = self.txtIdProprietario.get()
        
        self.lblmsgProprietario["text"] = user.selectProprietario(IdProprietario)
        
        self.txtNomeProprietario.delete(0, END)
        self.txtNomeProprietario.insert(INSERT, user.NomeProprietario)

        self.txtRGProprietario.delete(0, END)
        self.txtRGProprietario.insert(INSERT, user.RGProprietario)

        self.txtCPFProprietario.delete(0, END)
        self.txtCPFProprietario.insert(INSERT, user.CPFProprietario)

        self.txtTelefoneProprietario.delete(0, END)
        self.txtTelefoneProprietario.insert(INSERT, user.TelefoneProprietario)

        self.txtEmailProprietario.delete(0, END)
        self.txtEmailProprietario.insert(INSERT, user.EmailProprietario)

        self.txtIdContratoProp.delete(0, END)
        self.txtIdContratoProp.insert(INSERT, user.IdContrato)

        self.txtEnderecoProprietario.delete(0, END)
        self.txtEnderecoProprietario.insert(INSERT, user.EnderecoProprietario)

        self.txtDataProprietario.delete(0, END)
        self.txtDataProprietario.insert(INSERT, user.DataProprietario)

        self.txtIdImoveis.delete(0, END)
        self.txtIdImoveis.insert(INSERT, user.IdImoveis)
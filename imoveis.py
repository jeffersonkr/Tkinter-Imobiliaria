from banco import Banco

class Imovel(object):

    def __init__(self, IdImovel=1, DataCadastro = str, IdProprietario = int, AreaUtil =str, AreaTotal = str, VlrVenda=str, VlrAluguel=str, VlrIPTU = str, VlrCondominio = str, NumRelogioAES =str, NumRelogioSABESP = str, NumSeguro = str, Apolice=str, Tipo=str):
        self.info = {}
        self.IdImovel = IdImovel
        self.DataCadastro = DataCadastro
        self.IdProprietario = IdProprietario
        self.AreaUtil = AreaUtil
        self.AreaTotal = AreaTotal
        self.VlrVenda = VlrVenda
        self.VlrAluguel = VlrAluguel
        self.VlrIPTU = VlrIPTU
        self.VlrCondominio = VlrCondominio
        self.NumRelogioAES = NumRelogioAES
        self.NumRelogioSABESP = NumRelogioSABESP
        self.NumSeguro = NumSeguro
        self.Apolice = Apolice
        self.Tipo = Tipo

    def insertImovel(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into Imoveis (DataCadastro, IdProprietario, AreaUtil, AreaTotal, VlrVenda, VlrAluguel, VlrIPTU, VlrCondominio, NumRelogioAES, NumRelogioSABESP, NumSeguro, Apolice, Tipo) values ('" + self.DataCadastro + "', '" + self.IdProprietario + "', '" + self.AreaUtil + "', '"+ self.AreaTotal + "', '" + self.VlrVenda + "' , '" + self.VlrAluguel + "' , '" + self.VlrIPTU + "', '" + self.VlrCondominio + "','" + self.NumRelogioAES + "', '" + self.NumRelogioSABESP + "','" + self.NumSeguro + "', '" + self.Apolice + "', '" + self.Tipo + "' )")
        
            banco.conexao.commit()
            c.close()

            return "Imóvel cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Imóvel"

    def deleteImovel(self):

        banco = Banco()
        try:
            c=banco.conexao.cursor()

            c.execute("delete from Imoveis where IdImovel = " + self.IdImovel + " ")

            banco.conexao.commit()
            c.close()

            return "Excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão"

    def selectImovel(self, IdImovel):
        banco = Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select * from Imoveis where IdImovel = " + IdImovel + "  ")

            for linha in c:
                self.IdImovel = linha[0]
                self.DataCadastro = linha[1]
                self.IdProprietario = linha[2]
                self.AreaUtil = linha[3]
                self.AreaTotal = linha[4]
                self.VlrVenda = linha[5]
                self.VlrAluguel = linha[6]
                self.VlrIPTU = linha[7]
                self.VlrCondominio = linha[8]
                self.NumRelogioAES = linha[9]
                self.NumRelogioSABESP = linha[10]
                self.NumSeguro = linha[11]
                self.Apolice = linha[12]
                self.Tipo = linha[13]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do Imóvel!"

    def updateImovel(self):
        banco = Banco()
        try:
            c=banco.conexao.cursor()

            c.execute("update Imoveis set DataCadastro = '"+self.DataCadastro+"', IdProprietario = '"+self.IdProprietario+"', AreaUtil = '"+self.AreaUtil+"', AreaTotal = '"+self.AreaTotal+"', VlrVenda = '"+self.VlrVenda+"', VlrAluguel = '"+self.VlrAluguel+"', VlrIPTU = '"+self.VlrIPTU+"', VlrCondominio = '"+self.VlrCondominio+"', NumRelogioAES = '"+self.NumRelogioAES+"', NumRelogioSABESP = '"+self.NumRelogioSABESP+"', NumSeguro = '"+self.NumSeguro+"', Apolice = '"+self.Apolice+"',Tipo = '"+self.Tipo+"' where IdImovel = "+self.IdImovel+" ")
            banco.conexao.commit()
            c.close()

            return "Dados atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração dos dados!"
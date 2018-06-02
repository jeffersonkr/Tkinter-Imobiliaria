from banco import Banco

class Proprietario(object):

    def __init__(self, IdProprietario=0, NomeProprietario = '',  RGProprietario = '', CPFProprietario='', TelefoneProprietario ='', EmailProprietario = '', IdContrato=0, EnderecoProprietario='', DataProprietario = '', IdImoveis =0):
        self.info = {}
        self.IdProprietario = IdProprietario
        self.NomeProprietario = NomeProprietario
        self.RGProprietario = RGProprietario
        self.CPFProprietario = CPFProprietario
        self.TelefoneProprietario = TelefoneProprietario
        self.EmailProprietario = EmailProprietario
        self.IdContrato = IdContrato
        self.EnderecoProprietario = EnderecoProprietario
        self.DataProprietario = DataProprietario
        self.IdImoveis = IdImoveis

    def insertProprietario(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into Proprietario (NomeProprietario, RGProprietario, CPFProprietario, TelefoneProprietario, EmailProprietario, IdContrato, EnderecoProprietario, DataProprietario, IdImoveis) values ('" + self.NomeProprietario + "', '" + self.RGProprietario + "', '" + self.CPFProprietario + "', '"+ self.TelefoneProprietario + "', '" + self.EmailProprietario + "' , '"+ self.IdContrato + "' , '" + self.EnderecoProprietario + "', '"+ self.DataProprietario+ "','" + self.IdImoveis + "')")
        
            banco.conexao.commit()
            c.close()

            return "Proprietário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Proprietário"

    def deleteProprietario(self):

        banco = Banco()
        try:
            c=banco.conexao.cursor()

            c.execute("delete from Proprietario where IdProprietario = " + self.IdProprietario + " ")

            banco.conexao.commit()
            c.close()

            return "Excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão"

    def selectProprietario(self, IdProprietario):
        banco = Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select * from Proprietario where IdProprietario = " + IdProprietario + "  ")

            for linha in c:
                self.IdProprietario = linha[0]
                self.NomeProprietario = linha[1]
                self.RGProprietario = linha[2]
                self.CPFProprietario = linha[3]
                self.TelefoneProprietario = linha[4]
                self.EmailProprietario = linha[5]
                self.IdContrato = linha[6]
                self.EnderecoProprietario = linha[7]
                self.DataProprietario = linha[8]
                self.IdImoveis = linha[9]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do Proprietário!"

    def updateProprietario(self):
        banco = Banco()
        try:
            c=banco.conexao.cursor()

            c.execute("update Proprietario set NomeProprietario = '"+self.NomeProprietario+"', RGProprietario = '"+self.RGProprietario+"', CPFProprietario = '"+self.CPFProprietario+"', TelefonProprietario = '"+self.TelefoneProprietario+"', EmailProprietario = '"+self.EmailProprietario+"', IdContrato = '"+self.IdContrato+"', EnderecoProprietario = '"+self.EnderecoProprietario+"', DataProprietario = '"+self.DataProprietario+"', IdImoveis = '"+self.IdImoveis+"' where IdProprietario = "+self.IdProprietario+" ")
            banco.conexao.commit()
            c.close()

            return "Dados atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração dos dados!"
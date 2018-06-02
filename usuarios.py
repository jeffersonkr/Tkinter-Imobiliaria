from banco import Banco

class Cliente(object):

    def __init__(self, IdUsuario=1, Nome=str, DataCadastro=str, RG=str, CPF=str, Endereco=str, Telefone=str, Email=str, IdContrato=0, Tipo=str):
        self.info = {}
        self.IdUsuario = IdUsuario
        self.Nome = Nome
        self.DataCadastro = DataCadastro
        self.RG = RG
        self.CPF = CPF
        self.Endereco = Endereco
        self.Telefone = Telefone
        self.Email = Email
        self.IdContrato = IdContrato
        self.Tipo = Tipo

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (Nome, DataCadastro, RG, CPF, Endereco, Telefone, Email, IdContrato, Tipo) values ('" + self.Nome + "', '" + self.DataCadastro + "', '" + self.RG + "', '" + self.CPF + "', '" + self.Endereco + "', '" + self.Telefone + "', '" + self.Email + "', '" + self.IdContrato + "' , '" + self.Tipo + "' )")
        
            banco.conexao.commit()
            c.close()

            return "Cliente cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do cliente"

    def updateUser(self):
        banco = Banco()
        try:
            c=banco.conexao.cursor()

            c.execute("update usuarios set Nome = '" + self.Nome + "', DataCadastro = '" + self.DataCadastro + "',  RG = '" + self.RG + "', CPF = '" + self.CPF + "', Endereco = '" + self.Endereco + "', Telefone = '" + self.Telefone + "', Email = '" + self.Email + "', IdContrato = '" + self.IdContrato + "', Tipo = '" + self.Tipo + "' where idusuario = " + self.IdUsuario + " ")

            banco.conexao.commit()
            c.close()

            return "Dados atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração dos dados!"

    def deleteUser(self):

        banco = Banco()
        try:
            c=banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.IdUsuario + " ")

            banco.conexao.commit()
            c.close()

            return "Excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão"

    def selectUser(self, IdUsuario):
        banco = Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select * from usuarios where IdUsuario = " + IdUsuario + "  ")
                
            for linha in c:
                self.IdUsuario = linha[0]
                self.Nome = linha[1]
                self.DataCadastro = linha[2]
                self.RG = linha[3]
                self.CPF = linha[4]
                self.Endereco = linha[5]
                self.Telefone = linha[6]
                self.Email = linha[7]
                self.IdContrato = linha[8]
                self.Tipo = linha[9]
            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário!"

    def selectUserNome(self, Nome):
        banco = Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select * from usuarios where IdUsuario = "'%' + Nome + '%' "  ")
                
            for linha in c:
                self.cliente = linha
            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário!"
        
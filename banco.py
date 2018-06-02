import sqlite3


class Banco():
   
      def __init__(self):
          self.conexao = sqlite3.connect('banco.db')
          self.createTable()
   
      def createTable(self):
          cliente = self.conexao.cursor()
   
          cliente.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                       IdUsuario integer primary key autoincrement,
                       Nome text not null,
                       DataCadastro text not null,
                       RG text not null,
                       CPF text not null,
                       Endereco text not null,
                       Telefone text not null,
                       Email text not null CHECK (Email LIKE "%@%"),
                       IdContrato text,
                       Tipo text not null CHECK (Tipo in ('Aluguel','Compra'))
                       )""")


          cliente.execute( """
                        CREATE TABLE IF NOT EXISTS Proprietario(
                            IdProprietario INTEGER primary key autoincrement,
                            NomeProprietario text not null,
                            RGProprietario text not null,
                            CPFProprietario text not null,
                            TelefoneProprietario text not null,
                            EmailProprietario text not null CHECK (Email LIKE "%@%"),
                            IdContrato text not null,
                            EnderecoProprietario text not null,
                            DataProprietario text not null,
                            IdImoveis text
                        )""")
                        
          cliente.execute(            
                        """CREATE TABLE IF NOT EXISTS Imoveis (
                        IdImovel integer primary key autoincrement,
                        DataCadastro text not null,
                        IdProprietario integer not null,
                        AreaUtil text not null,
                        AreaTotal text not null,
                        VlrVenda text not null,
                        VlrAluguel text not null,
                        VlrIPTU text not null,
                        VlrCondominio text not null,
                        NumRelogioAES text not null,
                        NumRelogioSABESP text not null,
                        NumSeguro text not null,
                        Apolice text not null,
                        Tipo text not null CHECK (Tipo in ('Venda e Aluguel','Aluguel','Venda','Reforma')),
                        FOREIGN KEY (IdProprietario) REFERENCES Proprietario(IdProprietario)
                        ) """ )


          cliente.execute("""CREATE TABLE IF NOT EXISTS Contrato (
                        IdContrato integer primary key autoincrement,
                        Tipo text not null,
                        DataContrato text not null,
                        IdUsuario integer not null,
                        IdProprietario integer not null,
                        IdImovel integer not null,
                        FOREIGN KEY (IdUsuario) REFERENCES usuarios(IdUsuario)
                        FOREIGN KEY (IdImovel) REFERENCES Imoveis(IdImovel)

                         )""")

          
                        
                        
                        
                        
          self.conexao.commit()
          cliente.close()
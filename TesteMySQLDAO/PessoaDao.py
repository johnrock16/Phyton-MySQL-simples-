from TesteMySQLConnection import ConnectionFactory


con=ConnectionFactory.ConnectionFactory()

class Pessoa():
    def CadastrarPessoa(self,nome,idade):
        try:
            sql = "INSERT INTO pessoa (TB_PESSOA_NOME, TB_PESSOA_IDADE) VALUES (%s, %s)"
            val = (nome, idade)
            con.executar(sql,val)
        except:
            print("Não foi possivel cadastrar")
        else:
            print("Cadastrado com sucesso")

    def AlterarPessoa(self,id,nome,idade):
        try:
            sql="Update pessoa set TB_PESSOA_NOME = %s , TB_PESSOA_IDADE=%s  where TB_PESSOA_ID=%s "
            val=(nome,idade,id)
            con.executar(sql,val)
        except:
            print("Não foi possivel alterar os dados")
        else:
            print("Alterado com Sucesso")

    def DeletarPessoa(self,id):
        try:
            sql="Delete from pessoa where TB_PESSOA_ID= %s "
            val=(id, )
            con.executar(sql,val)
        except:
            print("Não foi possivel deletar")
        else:
            print("Deletado com sucesso")

    def PesquisaNome(self,nome):
        try:
            sql="Select * from pessoa where TB_PESSOA_NOME like %s "
            val=(nome, )
            con.listar(sql,val)
        except:
            print("Não foi possivel pesquisar por este nome")

    def ListarPessoas(self):
        try:
            con.listartodos()
        except:
            print("Não foi possivel listar")

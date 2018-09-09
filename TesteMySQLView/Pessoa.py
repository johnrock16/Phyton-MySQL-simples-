from TesteMySQLDAO import PessoaDao

__init__="__main__"


pessoa=PessoaDao.Pessoa()
rodar=True
while rodar:
    opcao=input("O que deseja fazer? \n"
                "1- Cadastrar Pessoa \n"
                "2- Alterar Pessoa cadastrada \n"
                "3- Deletar Pessoa cadastrada \n"
                "4- Listar todas as pessoas cadastradas \n"
                "5- Pesquisar por nome pessoa cadastrada \n"
                "6- Sair do programa \n")
    if(opcao=="1"):
        nome=input("Digite um nome para cadastrar")
        idade=input("Digite uma idade para cadastrar")
        pessoa.CadastrarPessoa(nome,idade)
    elif(opcao=="2"):
        id=int(input("Digite o id da pessoa que deseja alterar"))
        nome=input("Digite o novo nome da pessoa")
        idade=input("Digite a nova idade da pessoa")
        pessoa.AlterarPessoa(id,nome,idade)
    elif(opcao=="3"):
        id=int(input("Digite o id da pessoa que deseja excluir"))
        pessoa.DeletarPessoa(id)
    elif(opcao=="4"):
        pessoa.ListarPessoas()
    elif(opcao=="5"):
        nome=input("Digite o nome da pessoa que deseja pesquisar")
        pessoa.PesquisaNome(nome)
    elif(opcao=="6"):
        print("programa encerrado")
        rodar=False
    else:
        print("Digite um numero de 1 a 6")
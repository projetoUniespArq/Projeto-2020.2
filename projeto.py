 
lcategoria = []
ltematica = []
llivro = []
livro = dict()
categoria = dict ()
tematica = dict ()


def menu ():
    print("Menu:")
    print("    1-Cadastro de categorias e temáticas")
    print("    2-Configurações de livros")
    print("    3-Editar quantidade de um titulo")
    # print("    4-Excluir livros")
    # print("    4-Busca por exemplares")
    print("    4-Importar informações de um livro por arquivo")
    print("    5-Status de livros")
    print("    6-Gerar relatorios")
    print('    7-Sair do sistema')
    opc = int(input('    Digite sua opção: '))
    return opc

    
def cadastroCategoriasTematicas ():
    print("-----Cadastro de Categorias e Temáticas------")
    opc = int(input("Deseja cadastrar uma categoria nova?\n1-SIM\n2-Cadastro de Temáticas\n3-NÃO(Volta ao menu principal): ")) 
    while (opc != 4):
        if (opc==1):
            categoria["Categoria"] = input("Digite a categoria: ").upper()
            if categoria in lcategoria:
                print("Essa categoria já esta cadastrada!")
                main()
            else:
                lcategoria.append(categoria.copy())
                print(lcategoria)
                print("Categoria cadastrada com sucesso!")
                cadastroCategoriasTematicas()
                # main()           
        elif (opc==2): 
            cOrdenado=sorted(lcategoria,key=lambda l:l["Categoria"])
            for i, j in enumerate (cOrdenado,start=1):
                print(f'\n{i}-',end = ' ')
                for k in j.values():
                    print(f'{k}', end=' ')
            numeroCategoria = int(input("\nInforme o numero da categoria: "))
            tematica["Categoria"] = lcategoria[numeroCategoria-1]["Categoria"]
            tematica["Tematica"]= input("Digite a tematica: ").upper()
            if tematica not in ltematica:
                ltematica.append(tematica.copy())
                print("Temática cadastrada com sucesso")
                main()
            else:
                print("Temática já cadastrada")               
        elif (opc==3):
                main()    
def configuracoesLivro():
    print("-----Cadastro de Livros------")
    tOrdenado=sorted(ltematica,key=lambda l:(l["Categoria"],l["Tematica"]))
    for i, j in enumerate (tOrdenado,start=1):
        print(f'\n{i}-',end = ' ')
        for k in j["Categoria"],j["Tematica"]:
            print(f'{k} ',end = '')
    newBook = int(input("\nDigite o numero correspondente a categoria e a tematica: "))
    livro = {
        "Titulo": input("Informe o titulo: "),
        "Autor": input("Informe o Autor: "),
        "Ano": int(input("Digite o ano: ")),
        "Quantidade":int(input("Informe a quantidade de livros: ")),
        "Assunto": input("Digite o Assunto: ")
    }   
    if livro not in llivro:
        llivro.append(livro.copy())
        ltematica[newBook-1]["Livro"]=(llivro)
              
        print(ltematica)
        print(llivro)

        arquivo = open('db.txt', 'a')
        arquivo.write(f'COLLECTIONS: \n {ltematica}\n')


        print('Digite 1 para remover livros: ', '\nDigite 2 para procurar livro' ,'\nDigite 3 para voltar ao menu: ')
        value = int(input('Digite um valor: '))

        if(value == 1):
            print(f'Nome do livro: {livro["Titulo"]}')

            x = input("Digite o nome do livro para ser deletado: ")
            if(x == livro["Titulo"]):
                del livro
                print('Livro deletado com sucesso')
                
            main()

        elif(value == 2):
            print('*Buscar por exemplares')

            lv = input('Digite o nome do livro: ')

            if(lv == livro["Titulo"]):
                print(livro)
            else:
                print('Esse livro não esta disponivel')

            main()

        else:
            main()
        
    else:
        print("Livro já cadastrado")

    
        

    

def main ():
    opcao=menu ()
    while True:
        case = {
            1: lambda: cadastroCategoriasTematicas(),
            2: lambda: configuracoesLivro(),
            3: lambda: print('third'),
            # 4: lambda: removeLivro(),
            # 4: lambda: buscarLivro(),
            4: lambda: print('sixth'),
            5: lambda: print('seventh'),
            6: lambda: print('octave'),
        }

        case.get(opcao, lambda: print('carregando...'))()

        if(opcao >= 7):
            print('programa encerrado')
            break

            
              
main ()
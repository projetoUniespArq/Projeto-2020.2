lcategoria = []
ltematica = []
llivro = []
livro = dict()
tematica = dict ()

def menu ():
    print("Menu:")
    print("    1-Cadastro de categorias e temáticas")
    print("    2-Configurações de livros")
    print("    3-Editar quantidade de um titulo")
    print("    4-Excluir livros")
    print("    4-Busca por exemplares")
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
            categoria = input("Categoria: ")
            if categoria not in lcategoria:
                lcategoria.append(categoria)
                print(lcategoria)
                print("Categoria cadastrada com sucesso!")
                main()
            else: 
                print("Categoria já foi cadastrada")               
        elif (opc==2):
            for i in range (len(lcategoria)):  
                print(i+1,lcategoria[i])   
            numeroCategoria = int (input("\nInforme o numero da categoria: ")) 
            tematica=input("Tematica: ")
            tematica = {
                lcategoria[numeroCategoria-1]:tematica
            }
            if tematica not in ltematica:
                ltematica.append(tematica.copy())
                print("Temática cadastrada com sucesso")
                print(ltematica)
                print(ltematica[0])
                main()
            else:
                print("Temática já cadastrada")               
        elif (opc==3):
                main()
def addLivro ():
    print("-----Cadastro de Livros------")
    for k,l in enumerate (ltematica):
        for i,j in l.items():
            print((k+1),"-",i+": "+str(j))
    newBook = int(input("\nDigite o numero correspondente a categoria e a tematica: "))
    recebendoDados= ltematica[newBook-1]
    recebendoCategoria= list(recebendoDados.keys())
    recebendoTematica=list(recebendoDados.values())
    livro = {
        "Titulo": input("Informe o titulo: "),
        "Autor": input("Informe o Autor: "),
        "Ano": int(input("Digite o ano: ")),
        "Quantidade":int(input("Informe a quantidade de livros: ")),
        "Assunto": input("Digite o Assunto: "),
        "Categoria":recebendoCategoria[0],
        "Tematica":recebendoTematica[0]  
    } 
    if livro not in llivro:
        llivro.append(livro.copy())
        print(llivro)
        main()
    else:
        print("Livro já cadastrado")

def quantidadeLivros ():
    nomeLivro= (input("Digite o nome do livro que deseja editar a quantidade: "))
    for i in range (len(llivro)):
        if llivro[i]["Titulo"] == nomeLivro:
            quantidade = int(input("Livro encontrado!\nAgora informe a quantidade: "))
            llivro[i]["Quantidade"]=quantidade
            print("Atulizada com sucesso!")
            print(llivro)
            
            main()
    else:                
        print("Livro não encontrado!")
        main()
def main ():
    opcao=menu ()
    while True:
        case = {
            1: lambda: cadastroCategoriasTematicas(),
            2: lambda: addLivro(),
            3: lambda: quantidadeLivros(),
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
lcategoria = []
ltematica = []
llivro = []
livro = dict()
tematica = dict ()


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
                cadastroCategoriasTematicas()
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
    recebendoTematica= list(recebendoDados.values())
    livro = {
        "Titulo": input("Informe o titulo: "),
        "Autor": input("Informe o Autor: "),
        "Ano": int(input("Digite o ano: ")),
        "Quantidade":int(input("Informe a quantidade de livros: ")),
        "Assunto": input("Digite o Assunto: "),
        "Categoria":recebendoCategoria[0],
        "Tematica":recebendoTematica[0], 
         
    } 
    if livro not in llivro:
        llivro.append(livro.copy())
        
        arq = open('database.txt', 'a', encoding="utf8")
        
        armazena = f'{livro["Titulo"]}, {livro["Autor"]}, {livro["Ano"]} \n'
        arq.writelines(armazena)
        
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


def excluirLivro():
    for i in range (len(llivro)):
        print('---------------------------------------')
        pesquisar = input('Procure pelo livro: ')
        print('---------------------------------------')

        if pesquisar == llivro[i]["Titulo"]:

            print(f'Titulo do livro - {llivro[i]["Titulo"]}')
            print(f'Autor do livro - {llivro[i]["Autor"]}')
            print(f'Ano do livro - {llivro[i]["Ano"]}')

            print('---------------------------------------')
            decisao = int(input('Digite 1 para deletar o livro ou 2 para voltar ao menu principal: '))
            print('---------------------------------------')

            if(decisao == 1):

                del(llivro[i])
                print('Livro deletado com sucesso! ')
                print(llivro)

        else:
            print('livro não encontrado') 

    main()

def status():
    for i in range(len(llivro)):
        print('----------------------------------')

        n = input('Digite o nome do livro: ')
        if(n == llivro[i]["Titulo"]):
            print('----------------------------------')

            print(f'Livro - {llivro[i]["Titulo"]}')
            print(f'Autor - {llivro[i]["Autor"]}')
            print(f'Ano - {llivro[i]["Ano"]}')

            print('Registre o status que esse livro se encontrar')

            stus = input(': ')

            llivro[i]["Status"] = stus

            print(llivro[i])
            print('----------------------------------')

        else:
            print('----------------------------------')

            print('livro não encotrado')

    main()

def buscarExemplares():
    for i in range(len(llivro)):

        
        print('----------------------------------')
        print('*LEMBRE-SE DE CADASTRAR UM STATUS ANTES*')
        procurar = input('Digite o nome do exemplar ou digite sair para voltar ao menu : ')

            
        if procurar == 'sair':
            main()
        

        elif(procurar == llivro[i]["Titulo"]):
                
            print('----------------------------------')

            print(f'livro - {llivro[i]["Titulo"]}')
            print(f'autor - {llivro[i]["Autor"]}')
            print(f'status - {llivro[i]["Status"]}')

            print('----------------------------------')
        else:
            print('----------------------------------')

            print('livro não encontrado')
        
    main()

def arquivo():
    arq = open('database.txt', 'r')
    with open('database.txt') as arq:

        lista = list(arq)
        print(lista)

        for li in lista:
            Type = li.strip().split(',')
            print(f'*{Type}')
           
            titulo = input('Digite o nome do livro: ')
        
            if(titulo == Type[0]):
                print(f'Nome do livro {Type[0]}')
                print(f'Nome do autor {Type[1]}')
                print(f'Ano do livro {Type[2]}')

        arq.close()
                
        main()


                
                
def main ():
    while True:
        print("Menu:")
        print("    1-Cadastro de categorias e temáticas")
        print("    2-Configurações de livros")
        print("    3-Editar quantidade de um titulo")
        print("    4-Excluir livros")
        print("    5-Busca por exemplares")
        print("    6-Cadastrar status de livro")
        print("    7-Importar informações de um livro por arquivo")
        print("    8-Gerar relatorios")
        print('    9-Sair do sistema')
        opcao = int(input('    Digite sua opção: '))
        
       
           

        case = {
            1: lambda: cadastroCategoriasTematicas(),
            2: lambda: addLivro(),
            3: lambda: quantidadeLivros(),
            4: lambda: excluirLivro(),
            5: lambda: buscarExemplares(),
            6: lambda: status(),
            7: lambda: arquivo()
        }
            
        case.get(opcao, lambda: print('...'))()
        break
       
        
     
main()
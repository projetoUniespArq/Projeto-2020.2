lcategoria = []
ltematica = []
llivro = []
llivroExcluidos = []
larqCategoria = []
larqTematica = []
larqArcevo = []
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
                print("Categoria cadastrada com sucesso!")
                cadastroCategoriasTematicas()
            else: 
                print("-----Categoria já foi cadastrada-----")               
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
                cadastroCategoriasTematicas()
            else:
                print("Temática já cadastrada") 
                cadastroCategoriasTematicas()              
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
<<<<<<< HEAD
        llivro.append(livro)
        print("Livro cadastrado com sucesso!")
=======
        llivro.append(livro.copy())
        
        arq = open('database.txt', 'a', encoding="utf8")
        
        armazena = f'{livro["Titulo"]}, {livro["Autor"]}, {livro["Ano"]} \n'
        arq.writelines(armazena)
        
        print(llivro)
        
>>>>>>> 6c8b271cee19726b407aeac42a922f0ddc9f4305
        main()
    else:
        print("Livro já foi cadastrado!")

def quantidadeLivros ():
    print("-----Quantidade de Livros------")
    nomeLivro= (input("Digite o nome do livro que deseja editar a quantidade: "))
    for i in range (len(llivro)):
        if llivro[i]["Titulo"] == nomeLivro:
            quantidade = int(input("Livro encontrado!\nAgora informe a quantidade: "))
            llivro[i]["Quantidade"]=quantidade
            print("Atulizada com sucesso!")
            main()
    else:                
        print("Livro não encontrado!")
    main()

def excluirLivro():
    print('---------------------------------------')
    forma=int (input('Digite a forma que a forma que deseja excluir\n1-Grupo de livros pelo ano\n2-Individualmente pelo titulo: '))
    print('---------------------------------------')
    if forma == 1:
        ano = int(input("Digite o ano dos livros serão excluídos. Todos os livros menores que esse ano serão excluídos: "))
        for i in range (len(llivro)):
            if llivro[i]["Ano"] <= ano:
                print(f'Titulo do livro - {llivro[i]["Titulo"]}')
                print(f'Autor do livro - {llivro[i]["Autor"]}')
                print(f'Ano do livro - {llivro[i]["Ano"]}')     
                llivroExcluidos.append(i)
                print('---------------------------------------')
        decisaoExcluir = int(input('Digite 1 para deletar o livro ou 2 para voltar ao menu principal: '))
        if decisaoExcluir == 1:
            for i in llivroExcluidos:
                del(llivro[i])
            print(llivro)
    if forma == 2:
        pesquisar = input('Procure pelo livro: ')
        for i in range (len(llivro)):
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

<<<<<<< HEAD
def gerarRelatorio ():
    print("-----Relatórios------")
    opcaoRelatorio=int(input("1-Relatorio das Categorias existentes no acervo\n2-Relatorio das tematicas no acervo\n3-Relatorios do acervo: "))
    if opcaoRelatorio == 1:
        cArquivo = open("categoria.txt","a")
        larqCategoria.append("Categorias cadastradas no arcevo:\n")
        for i in lcategoria:
            larqCategoria.append("-")
            larqCategoria.append(str(i))
            larqCategoria.append("  \n")
        larqCategoria.append("***********************************")
        larqCategoria.append(f"\nQuantidade de categorias no acervo: {len(lcategoria)}")
        larqCategoria.append("  \n")
        cArquivo.writelines(larqCategoria)
        cArquivo.close()
        print("Relatorio gerado com sucesso! ")
        main ()
    elif opcaoRelatorio == 2:
        tArquivo = open ("tematica.txt","a")
        larqTematica.append("Essas são as tematicas associadas as categorias existentes:\n")
        for i in ltematica:
            for j,l in i.items ():
                larqTematica.append(str(j))
                larqTematica.append("-")
                larqTematica.append(str(l))
                larqTematica.append("  \n")
        larqTematica.append("***********************************")
        larqTematica.append(f"\nQuantidade de tematicas no acervo: {len(ltematica)}")
        tArquivo.writelines(larqTematica)
        tArquivo.close()
        print("Relatorio gerado com sucesso! ")
        main ()
    elif opcaoRelatorio == 3:
        arcevo = open("arcevo.txt","a")
        larqArcevo.append("Relatorio do acervo:\n")
        larqArcevo.append(f"Numero de Categorias cadastradas: {len(lcategoria)}\n")
        larqArcevo.append(f"Numero de Tematicas cadastradas: {len(ltematica)}\n")
        larqArcevo.append(f"Numero de livros cadastrados: {len(llivro)}\n")
        arcevo.writelines(larqArcevo)
        arcevo.close()
        print("Relatorio gerado com sucesso! ")
        main ()
def livroExterno ():
    print("-----Livro Externo------")
    pasta = input("Digite nome do arquivo com formato que foi salvo o arquivo: ")
    arquivo = open(pasta,"r").readline().split(";")
    livro = {
        "Titulo": arquivo[0],
        "Autor": arquivo[1],
        "Ano": arquivo[2],
        "Quantidade":arquivo[3],
        "Assunto": arquivo[4],
        "Categoria":arquivo[5],
        "Tematica":arquivo[6],     
    } 
    if livro not in llivro:
        llivro.append(livro.copy())
        print("Livro cadastrado com sucesso!")
        main()
    else:
        print("Livro já cadastrado")
=======
def arquivo():
    arq = open('database.txt', 'r')
    with open('database.txt') as arq:
>>>>>>> 6c8b271cee19726b407aeac42a922f0ddc9f4305

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
        print("    2-Adicionar Livros")
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
<<<<<<< HEAD
            7: lambda: livroExterno(),
            8: lambda: gerarRelatorio()
=======
            7: lambda: arquivo()
>>>>>>> 6c8b271cee19726b407aeac42a922f0ddc9f4305
        }
            
        case.get(opcao, lambda: print('...'))()
        break
       
        
     
main()
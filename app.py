import shelve

# login de acesso

print('* Faça seu acesso *')
  
nome  = input('Digite seu nome completo: ')
chaveAcesso = input('Digite sua chave de acesso: ')  

print(f'Bem vindo {nome}, login efetuado com sucesso')
  
# banco de dados
db = shelve.open('database.db')
db['Funcionario'] = {
  'nome': nome,
  'acesso': chaveAcesso
}

# cadastro de categoriais
def CadastroCategorias():
  categoria = input('Digite uma categoria: ')
  tema = input('Digite um tema: ')

  db['RegistroCategorias'] = {
    'registrar': {
       
      'categoria': categoria,
      'tema': tema  
    }  
  }

  print(db['RegistroCategorias']['registrar'])



# home
while True:
  def Menu():
    print('* Home *\n',
          '- 1 Cadastrar categorias e temáticas\n',
          '- 2 Cadastrar novos livro\n',
          '- 3 Editar quantidade de um titulo\n',
          '- 4 Excluir livros\n',
          '- 5 Busca por exemplaresn\n',
          '- 6 Importar informações de um livro por arquivo\n',
          '- 7 Status de livros\n',
          '- 8 Gerar relatorios\n',

          '- 9 Sair'
        )
    
    value = int(input('Escolha uma das opções: '))
    cases = {
      1: lambda: CadastroCategorias(),
      2: lambda: print('second'),
      3: lambda: print('second'),
      4: lambda: print('second'),
      5: lambda: print('second'),
      6: lambda: print('second'),
      7: lambda: print('second'),
      8: lambda: print('second'),
    }
    cases.get(value, lambda: print('...'))()
  
    if(value >= 9):
        print('O programa foi finalizado')
  Menu()
  
  break





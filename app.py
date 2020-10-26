import shelve

# login de acesso
def Login():
  print('* Faça seu acesso *')
  
  nome  = input('Digite seu nome completo: ')
  chaveAcesso = input('Digite sua chave de acesso: ')  
  
  # banco de dados
  db = shelve.open('database.db')
  db['Funcionario'] = {
    'nome': nome,
    'acesso': chaveAcesso
  }

  print(f'Bem vindo {nome}, login efetuado com sucesso')
Login()

# home
while True:
  def Menu():
    print('* Home *\n',
          '- 1 Cadastrar categorias e temáticas\n',
          '- 2 Cadastrar livro\n',
          '- 3 Sair'
        )
    
    value = int(input('Escolha uma das opções: '))
    cases = {
      1: lambda: print('first'),
      2: lambda: print('second'),    
    }
    cases.get(value, lambda: print('...'))()
  
    if(value == 3):
        print('O programa foi finalizado')
  Menu()
  break



import shelve

def Login():
  print('* Faça seu acesso *')
  
  nome  = input('Digite seu nome completo: ')
  chaveAcesso = input('Digite sua chave de acesso: ')  
  
  # banco de dados
  db = shelve.open('database.db')
  db['Aluno'] = {
    'nome': nome,
    'matricula': chaveAcesso
  }

  print(f'Bem vindo {nome}, login efetuado com sucesso')
Login()
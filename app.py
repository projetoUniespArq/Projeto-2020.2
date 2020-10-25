import shelve

def Login():
  print('* Faça seu login *')
  
  nome  = input('Digite seu nome completo: ')
  matricula = input('Digite sua matricula: ')  
  
  # banco de dados
  db = shelve.open('database.db')
  db['Aluno'] = {
    'nome': nome,
    'matricula': matricula
}
  # manipulando valores
  # print(db['Aluno']['nome'])

  print(f'Bem vindo {nome}, login efetuado com sucesso')
Login()
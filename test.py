

categoria = input("digite uma categoria: ")
tema = input('digite um tema: ')

arr = [
  {
    'categorias': [categoria],
    categoria: [tema]
  }
]



print(arr)

arquivo = open('db.txt', 'a')
arquivo.write(f'{categoria}: {tema}')
arquivo.close()  
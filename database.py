i = 1
arr = []

while i <= 3:
  categoria = input('digite uma categoria: ')
  tema = input('digite um tema: ')

  arr.append({
    categoria: tema
  })

  i += 1

print(arr)

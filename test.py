x = input(': ')

arquivo = open('data.txt', 'a')
lista = list()
lista.append(x)

arquivo.writelines(lista)


arquivo = open('data.txt', 'r')
print(arquivo.readlines())




#  catalago = []

#         chave = open('database.txt', 'r').readlines(.strip().split(''))

#         with open('database.txt', 'rb') as data:
#             for(dat in data.readlines()):
#                 book = dat.strip().replace('\t', '')

#                 booksList = book.split(',')

#                 bookDict = {}
#                 for v in bookDict:
#                     if v:
#                         bookDict[chave[booksList.index(v)]] == v

#                 catalago.append(bookDict)
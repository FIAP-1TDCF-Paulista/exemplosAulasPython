arquivo = open('novo-arquivo-2.txt', 'r', encoding='utf8')
lista = arquivo.readlines()
print(lista)
arquivo.close()
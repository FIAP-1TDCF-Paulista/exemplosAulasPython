arquivo = open('novo-arquivo-2.txt', 'r', encoding='utf-8')
conteudo = arquivo.readlines()
conteudo.append('\nNova linha')
arquivo = open('novo-arquivo-2.txt', 'w', encoding='utf-8')
arquivo.writelines(conteudo)
arquivo.close()
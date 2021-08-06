import os
myfile= input("Digite o nome do arquivo a ser deletado: ")
try:
    os.remove(myfile)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))
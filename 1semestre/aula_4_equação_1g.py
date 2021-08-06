'''
Faculdade de Informática e Administração Paulista - FIAP
Defesa Cibernética
Development and Coding for Security
Prof. Ms. Fábio Henrique Cabrini
3/2021
Equação do 1º grau 
'''
print("Cálculo da Equação do 1º grau genérica")
print("b.x+c=0")
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
print("Equação do 1º grau")
print("{0}.x + ({1}) = 0".format(b,c))
x = -c/b
print("O valor de x = {0:2.3f}".format(x))
if b > 0:
    print("A reta é crescente! /")
else:
    print("A reta é decrescente! \\")
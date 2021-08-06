x = 1
while x != 0:
    x = int(input("Digite um número inteiro ou zero para sair: "))
    if x % 2 == 0:
        print("%d é par" % x)
    else:
        print("%d é impar" % x)
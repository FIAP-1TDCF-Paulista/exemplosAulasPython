def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1) #recursivo

print("Cálculo do Fatorial de N")
x = int(input("Digite o valor de n: "))
f = fatorial(x)
print("O fatorial de {0} é {1}".format(x,f))
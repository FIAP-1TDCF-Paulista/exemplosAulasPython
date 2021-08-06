n = 0
while n < 2:
    try:
        n = int(input("Digite o valor de n (n > 1): "))
        if n < 2:
            print("Digite n >= 2")
    except:
        print("O número digitado deve ser inteiro!")
lista = [0, 1]
for i in range (n-2):
    lista.append(lista[i] + lista [i+1])
print ("Sequência gerada:", lista)
print("\n\nFim do Programa")
try:
    A = int(input("Digite o valor para A: "))
    B = int(input("Digite o valor para B: "))
    Divisao = A / B
    print("A divisão",A,"/",B," = ",Divisao)
except ZeroDivisionError:
    print("Não é possível realizar a divisão por zero!")
except ValueError:
    print("Digite números inteiros!")
except:
    print("Erro desconhecido!")
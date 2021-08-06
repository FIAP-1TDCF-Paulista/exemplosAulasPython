try:
    S = input("Digite N no intervalo [100, 500] ==>> ")
    N = int(S)
except:
    print("O valor digitado {} não é um número!".format(S))
else:
    if N < 100 or N > 500:
        print("O valor digitado {} está fora do intervalo!".format(N))
    else:
        print("O valor digitado {} está dentro do intervalo!".format(N))
finally:
    print("F I M\n\n")
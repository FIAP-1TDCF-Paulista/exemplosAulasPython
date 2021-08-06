A = int(input("Digite o valor para A: "))
B = int(input("Digite o valor para B: "))
try:
  Divisao = A / B
  print("A divisão",A,"/",B," = ",Divisao)
except:
  print("Não é possível realizar divisão por zero! Você deveria saber : )")
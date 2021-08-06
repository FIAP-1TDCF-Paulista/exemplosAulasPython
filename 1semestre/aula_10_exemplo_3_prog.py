from aula_10_exemplo_3_func import pagamento, pagamentoaspira

tipofunc = int(input("Digite o tipo de professor 1 (senior) ou 2 (aspira): "))
horas_t= input("digite o número de horas: ")
valor_h= input("Digite o valor hora/aula: ")
if tipofunc == 1:
    print("O salário Senior é R$ ",pagamento(horas_t,valor_h))
else:
    print("O salário de Aspira é R$ ",pagamentoaspira(horas_t,valor_h))
# definição da função
def pagamento(horas, valor):
    salario=float(horas)*float(valor)*5.5
    return salario

# corpo do programa
horas_t= input("Digite as horas: ")
valor_h= input("Digite o valor hora: ")
#print("O salário é R$ ",pagamento(horas_t,valor_h))
print(f"O salário é R$ {pagamento(horas_t,valor_h)}")
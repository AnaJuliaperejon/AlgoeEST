base=int(input("insira o salário base"))
hora_extra=int(input("insira as horas extras trabalhadas"))
valor_hora=int(input("insira o valor da hora extra"))
valor_total=hora_extra*valor_hora
salario_total=(valor_total+base)
print(f"valor total do salário é: {salario_total}")
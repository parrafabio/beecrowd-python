funcionario = input()
salario = float(input())
vendas = float(input())

bonus = vendas * 0.15

print(f'TOTAL = R$ {bonus + salario:.2f}')
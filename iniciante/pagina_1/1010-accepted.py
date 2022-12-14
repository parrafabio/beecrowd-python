num1, quat1, valor1 = input().split()
num2, quat2, valor2 = input().split()

pay = int(quat1) * float(valor1) + int(quat2) * float(valor2)

print(f'VALOR A PAGAR: R$ {pay:.2f}')
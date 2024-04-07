nome = 'Cleber'
altura = 1.77
peso = 87
imc = peso / altura ** 2  # IMC = Peso / (altura x altura)

# f-strings = formatação

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print (linha_2)
print(linha_3)

# Cleber Couto tem 1.77 de altura,
# pesa 87 kilos e seu IMC é 
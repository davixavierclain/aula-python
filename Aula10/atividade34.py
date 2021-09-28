salário = float(input('Informe o seu salário atual R$ '))
faixa1 = 15
faixa2 = 10
if salário <= 1250:
    aumento = faixa1
else:
    aumento = faixa2
print('Atualmente seu salário é R${:.2f} e com o aumento você passa a ganhar R${:.2f}'.format(salário, salário + (salário * aumento) / 100))
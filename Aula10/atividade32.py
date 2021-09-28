import calendar
year = int(input('Digite um ano : '))
yearbi6 = calendar.isleap(year)
if yearbi6 is True:
    print(f'O ano de {year} é bisexto')
else:
    print(f'O ano de {year} não é bisexto')
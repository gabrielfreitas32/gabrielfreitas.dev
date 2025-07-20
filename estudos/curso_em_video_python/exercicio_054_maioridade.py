from datetime import date

maiores = 0
menores = 0

for c in range(1, 7):
    idade = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade_atual = ano_atual - idade

    if idade_atual >= 21:
        maiores += 1
    else:
        menores += 1

print('{} pessoas, já atingiram a maior idade'.format(maiores))
print('{} pessoas, ainda não atingiram a maior idade'.format(menores))

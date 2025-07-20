# Importa o módulo para obter o ano atual
from datetime import date

# Inicializa os contadores
maiores = 0
menores = 0

# Laço para receber 6 anos de nascimento
for c in range(1, 7):
    idade = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade_atual = ano_atual - idade

    # Verifica se já atingiu a maioridade (21 anos ou mais)
    if idade_atual >= 21:
        maiores += 1
    else:
        menores += 1

# Exibe os resultados
print(f'{maiores} pessoas já atingiram a maior idade.')
print(f'{menores} pessoas ainda não atingiram a maior idade.')

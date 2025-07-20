# Calculadora simples de IMC
# Recebe altura e peso, calcula o IMC e informa o status

alt = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))

imc = peso / (alt ** 2)

# Verifica a faixa do IMC e atribui o status
if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    status = 'COM PESO IDEAL'
elif 25 <= imc < 30:
    status = 'COM SOBREPESO'
elif 30 <= imc < 40:
    status = 'COM OBESIDADE'
else:
    status = 'COM OBESIDADE MORBIDA'

print()
print(f'Sua altura é {alt:.2f} m, seu peso é {peso:.2f} kg.')
print(f'Seu IMC é {imc:.1f}, você está {status}.')
print()

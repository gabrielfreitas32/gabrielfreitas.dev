frase = str(input('Digite uma frase: ')).upper()
frase_sem_espaço = frase.replace(' ','')
frase_invertida = frase_sem_espaço [::-1]
if frase_invertida == frase_sem_espaço:
    print('A frase {} é PALÍNDROMO!'.format(frase))
else:
    print('A frase {} não é PALÍNDROMO!'.format(frase))

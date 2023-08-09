lista2 = {'1º prêmio': 'CESTA GRANDE', '2º prêmio': 'CESTA MEDIA', '3º prêmio': 'CESTA PEQUENA'}
x = 40
for nome,numero in lista2.items():
    x -= 20
    print(nome,numero)
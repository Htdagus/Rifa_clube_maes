#quantidade de premios a ser sorteado na rifa
premios_qtd = int("3")
#premios_qtd = int(input('Qual a quantidade de prêmios?'))
#print(f"A quantidade de prêmios é {premios_qtd}" )


#quais os premios que serão sorteados
#1º prêmio = ??? ; 2º prêmio = ???



# i= int("1")
# premio_sorteado = []
# premio_lista = []
# while i <= premios_qtd:
#     premio=(input(f'Qual {i}º premio a ser sorteado?'))
#     premio_lista.append(f"{i}º prêmio: {premio}")
#     i= i + 1
# print(f'Os premios a ser sorteados são: {premio_lista}')

i= int("1")
premio_dicionario = {}
while i <= premios_qtd:
    premio= str(input(f'Qual {i}º prêmio a ser sorteado?'))
    premio_dicionario[f"{i}º prêmio:"]= premio
    i= i + 1
print(f'Os prêmios a ser sorteados são: {premio_dicionario}')

#listade premios

#1º prêmio = ??? ; 2º prêmio = ???
#['1º prêmio: CESTA GRANDE', '2º prêmio: CESTA MEDIA', '3º prêmio: CESTA PEQUENA']


from reportlab.pdfgen import canvas
#"LOCAL DO SORTEIO:",
#"VALOR: R$", 
#"DATA DO SORTEIO:", 



nome_clube = "CLUBE DE MÃES ANA NERI"
data_sorteio = "DATA DO SORTEIO: 09/09/2023"							
local_sorteio = "LOCAL: SALÃO PAROQUIAL"
rifa_valor = "VALOR: R$ 5,00"
#quantidade total de números a venda na rifa 
rifa_total_numeros = "100"
#números de rifa por folha
rifa_qtd_numeros_folha= "20"

premios_qtd = int("3")

def GeneratePDF(lista):
    try:
        nome_pdf = "TESTE RIFA"
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 700
        #saber ate onde pode ir altura dos premios
        premio_altura = x -(20 +(premios_qtd * 20))
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(100,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 30)
        pdf.drawCentredString(300,780, nome_clube)
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawCentredString(300,760, "Ação entre Amigos")
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(300,740, local_sorteio)
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(100,720, rifa_valor)
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(300,720, data_sorteio)
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawCentredString(300,700, "PREMIAÇÃO")
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawCentredString(300,premio_altura, "final da premiçao PREMIAÇÃO")
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawCentredString(300,20, "final da folha")
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
       print('Erro ao gerar {}.pdf'.format(nome_pdf))

lista = {'1º prêmio': 'CESTA GRANDE', '2º prêmio': 'CESTA MEDIA', '3º prêmio': 'CESTA PEQUENA'}

GeneratePDF(lista)


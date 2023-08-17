from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect

#"LOCAL DO SORTEIO:",
#"VALOR: R$", 
#"DATA DO SORTEIO:", 



nome_clube = str("CLUBE DE MÃES ANA NERI")
data_sorteio = str("DATA DO SORTEIO: 09/09/2023")							
local_sorteio = str("LOCAL: SALÃO PAROQUIAL")
rifa_valor = str("VALOR: R$ 5,00")
#quantidade total de números a venda na rifa 
rifa_total_numeros = "100"
#números de rifa por folha
rifa_qtd_numeros_folha= int(20)

premios_qtd = int("4")

def GeneratePDF(premio_dicionario):
    try:
        nome_pdf = "TESTE RIFA"
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
       
        pdf.setTitle(nome_pdf)
        
        pdf.setFont("Helvetica-Oblique", 30)
        pdf.drawCentredString(300,790, str(nome_clube))
        
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawCentredString(300,760, "Ação entre Amigos")
        
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(300,730, str(local_sorteio))

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(100,700, str(rifa_valor))

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(300,700, str(data_sorteio))

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawCentredString(300,670, "PREMIAÇÃO")

        pdf.setFont("Helvetica-Bold", 16)
        
        x = 660
        #saber ate onde pode ir altura dos premios
        premio_altura = x -(20 +(premios_qtd * 20))
        
        for premio_nr, premio in premio_dicionario.items():
            x -= 20
            pdf.drawString(100,x, '{} : {}'.format(premio_nr, premio))

        pdf.drawCentredString(100,(premio_altura-20) , "Nome:")
        pdf.drawCentredString(500,(premio_altura-20) , "Telefone:")
        
        
        pdf.setFont("Helvetica-Bold", 14)  
        linhas = int(rifa_qtd_numeros_folha)
        numeros_inicial = premio_altura - 30
        tracos= numeros_inicial
        lin= 1
        numero_linhas = 1
        altura_linhas= -((40 - numeros_inicial)/linhas)
        while lin <= linhas: 
            tracos = tracos - altura_linhas # é a altura entre linha
            pdf.line(10, tracos, 580, tracos)
            pdf.drawCentredString(30, tracos+3, str(numero_linhas))
            numero_linhas= lin +1
            lin = lin +1
        


        # pdf.line(10, 20, 580, 20)

        pdf.setFont("Helvetica-Bold", 10)        
        pdf.drawCentredString(300,20, "Nome da(o) Responsável: __________________________________")

        
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
       print('Erro ao gerar {}.pdf'.format(nome_pdf))

premio_dicionario = {'3º prêmio': 'CESTA PEQUENA', '1º prghgêmiod': 'CESTA GRANDE', '2º prêghmio': 'CESTA MEDIA', '3º prêlmio': 'CESTA PEQUENA'}

GeneratePDF(premio_dicionario)


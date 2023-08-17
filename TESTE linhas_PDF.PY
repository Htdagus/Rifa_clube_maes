from reportlab.pdfgen import canvas


def GeneratePDF(premio_dicionario):
    try:
        nome_pdf = "TESTE linhas"
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 700
        #saber ate onde pode ir altura dos premios
                
        for premio_nr, premio in premio_dicionario.items():
            x -= 20
            pdf.drawString(100,x, '{} : {}'.format(premio_nr, premio))
        
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 30)
        
        pdf.drawCentredString(300,780,'nome clube')
        pdf.setFont("Helvetica-Bold", 20)

        linhas = 10
        numeros_inicial = 0
        tracos= numeros_inicial
        lin= 1
        
        while lin <= linhas: 
            tracos = tracos + 20
            pdf.line(10, tracos, 580, tracos)
            lin = lin +1
        
        # pdf.line(10, 20, 580, 20)

        pdf.drawCentredString(300,20, "final da folha")
                
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))


premio_dicionario = {'1º prêmio': 'CESTA GRANDE', '2º prêmio': 'CESTA MEDIA', '3º prêmio': 'CESTA PEQUENA'}

GeneratePDF(premio_dicionario)
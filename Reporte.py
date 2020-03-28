from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def crearPDF(name, subTitulo):
    
    pdf = canvas.Canvas(name)
    pdf.drawString(5,5,name)
    pdf.setTitle(subTitulo)
    pdf.drawString(270,800,subTitulo)
    pdf.drawImage('salida.gv.png',0,480)
    
    pdf.save()

crearPDF('Automata.pdf', 'Reporte')
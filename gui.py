#!/usr/bin/python
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class Gui:
    MY_ADDRESS = 'huseyingokay_1999@hotmail.com'
    RECEIVER_ADDRESS = 'huseyin.gokay@ozu.edu.tr'
    PASSWORD = 'XRAYSKINGSTAR8520'
    MESSAGE = 'denemeedfskljdsfkljdgkldf'
    SUBJECT = 'AMETTEN GELDI'
    ATTACH = 'ornekahmet.pdf'
    OUTPUT_PDF = "interview_letter.pdf"


    def pdfReadAndWrite(self, ATTACH):
        packet = io.BytesIO()
        # create a new PDF with Reportlab
        file = open("ornek.txt", "r", encoding="utf-8")
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(0, 0, file.read())
        can.save()

        #move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open(ATTACH, "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open(self.OUTPUT_PDF, "wb")
        output.write(outputStream)
        outputStream.close()



if __name__ == '__main__':
    pdfReadAndWrite(ATTACH)

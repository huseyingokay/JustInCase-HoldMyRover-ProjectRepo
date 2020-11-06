#!/usr/bin/python
from fpdf import FPDF

class Gui:
    MY_ADDRESS = 'huseyingokay_1999@hotmail.com'
    RECEIVER_ADDRESS = 'huseyin.gokay@ozu.edu.tr'
    PASSWORD = 'XRAYSKINGSTAR8520'
    MESSAGE = 'denemeedfskljdsfkljdgkldf'
    SUBJECT = 'AMETTEN GELDI'
    ATTACH = 'ornekahmet.pdf'
    OUTPUT_PDF = "interview_letter.pdf"


    def pdfReadAndWrite(self):
        file = open("ornek.txt", "r")
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size = 15)
        # create a cell
        for x in file:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        # save the pdf with name .pdf
        pdf.output(self.OUTPUT_PDF)

#!/usr/bin/python
# -*- coding:utf-8 -*-
import fileinput
from fpdf import FPDF

class Gui:
    SENDER_ADDRESS = 'huseyingokay_1999@hotmail.com'
    RECEIVER_ADDRESS = 'huseyin.gokay@ozu.edu.tr'
    RECEIVER = "Hüseyin Bey"
    SENDER = "Ahmet Boi"
    POSITION = "SOFTWARE"
    PASSWORD = 'XRAYSKINGSTAR8520'
    MESSAGE = 'My job application letter'
    SUBJECT = 'AMETTEN GELDI'
    ATTACH = 'ornekahmet.pdf'
    OUTPUT_PDF = "interview_letter.pdf"
    DATE = "August 15, 2020"
    PHONE = "555-555-4123"

    def pdfReadAndWrite(self):
        file = open("ornek.txt", "r+")
        fileData = file.readlines()
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size = 11)
        # create a cell
        for x in fileData:
            if("(RECEIVER)" in x):
                x = x.replace("(RECEIVER)", self.RECEIVER)
            elif("(SENDER)" in x):
                x = x.replace("(SENDER)", self.SENDER)
            elif("(POSITION)" in x):
                x = x.replace("(POSITION)", self.POSITION)
            elif("(SENDER_ADDRESS)" in x):
                x = x.replace("(SENDER_ADDRESS)", self.SENDER_ADDRESS)
            elif("(RECEIVER_ADDRESS)" in x):
                x = x.replace("(RECEIVER_ADDRESS)", self.RECEIVER_ADDRESS)
            elif("(DATE)" in x):
                x = x.replace("(DATE)", self.DATE)
            elif("(PHONE)" in x):
                x = x.replace("(PHONE)", self.PHONE)

            pdf.multi_cell(185, 5, txt = x, align = 'L')
        # save the pdf with name .pdf
        pdf.output(self.OUTPUT_PDF)

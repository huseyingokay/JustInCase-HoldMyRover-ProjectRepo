#!/usr/bin/python
# --coding: utf-8--

import fileinput
from fpdf import FPDF
import time

class Gui:
    SENDER_ADDRESS = 'huseyingokay_1999@hotmail.com'
    RECEIVER_ADDRESS = 'huseyin.gokay@ozu.edu.tr'
    RECEIVER = "Hüseyin Bey"
    SENDER = "Ahmet Çağatay Savaşlı"
    POSITION = ".NET Developer"
    UNIVERSITY = "Ozyegin University"
    FACULTY = "Computer Science"
    PASSWORD = 'XRAYSKINGSTAR8520'
    MESSAGE = 'My job application letter'
    SUBJECT = 'Ahmet Çağatay Savaşlı - Job Application Form'
    ATTACH = 'ornekahmet.pdf'
    OUTPUT_PDF = "interview_letter.pdf"
    DATE = time.strftime("%x")
    PHONE = "555-555-4123"

    def pdfReadAndWrite(self):
        file = open("letter.txt", "r+")
        fileData = file.readlines()
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # set style and size of font
        # that you want in the pdf
        pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
        pdf.set_font("DejaVu", size = 11)
        # create a cell
        for x in fileData:
            if("(RECEIVER)" in x):
                x = x.replace("(RECEIVER)", self.RECEIVER)
            if("(SENDER)" in x):
                x = x.replace("(SENDER)", self.SENDER)
            if("(POSITION)" in x):
                x = x.replace("(POSITION)", self.POSITION)
            if("(SENDER_ADDRESS)" in x):
                x = x.replace("(SENDER_ADDRESS)", self.SENDER_ADDRESS)
            if("(RECEIVER_ADDRESS)" in x):
                x = x.replace("(RECEIVER_ADDRESS)", self.RECEIVER_ADDRESS)
            if("(DATE)" in x):
                x = x.replace("(DATE)", self.DATE)
            if("(UNIVERSITY)" in x):
                x = x.replace("(UNIVERSITY)", self.UNIVERSITY)
            if("(FACULTY)" in x):
                x = x.replace("(FACULTY)", self.FACULTY)
            if("(PHONE)" in x):
                x = x.replace("(PHONE)", self.PHONE)

            pdf.multi_cell(185, 5, txt = x, align = 'L')
        # save the pdf with name .pdf
        pdf.output(self.OUTPUT_PDF)

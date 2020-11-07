#!/usr/bin/python
# -*- coding:utf-8 -*-
import fileinput
from fpdf import FPDF

class Gui:
    MY_ADDRESS = 'huseyingokay_1999@hotmail.com'
    RECEIVER_ADDRESS = 'huseyin.gokay@ozu.edu.tr'
    RECEIVER = "ahmet"
    POSITION = "SOFTWARE"
    PASSWORD = 'XRAYSKINGSTAR8520'
    MESSAGE = 'denemeedfskljdsfkljdgkldf'
    SUBJECT = 'AMETTEN GELDI'
    ATTACH = 'ornekahmet.pdf'
    OUTPUT_PDF = "interview_letter.pdf"

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
            elif("(POSITION)" in x):
                x = x.replace("(POSITION)", self.POSITION)
            pdf.multi_cell(185, 5, txt = x, align = 'L')
        # save the pdf with name .pdf
        pdf.output(self.OUTPUT_PDF)

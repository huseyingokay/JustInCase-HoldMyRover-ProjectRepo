#!/usr/bin/python
# -*- coding:utf-8 -*-

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
        file = open("ornek.txt", "rt")
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size = 15)
        # create a cell
        for x in file:
            row = file.read()
            self.parameterFinder(row, file)
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        # save the pdf with name .pdf
        pdf.output(self.OUTPUT_PDF)

    def parameterFinder(self, line, file):
        if('(RECEIVER)' in line):
            row = row.replace('(RECEIVER)', self.RECEIVER)
            file.close()
            file = open("ornek.txt", "a")
            file.write(row)
        if("(POSITION)" in line):
            row = line.replace("(POSITION)", self.POSITION)
            file.close()
            file = open("ornek.txt", "a")
            file.write(row)

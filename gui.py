#!/usr/bin/python
# --coding: utf-8--

import fileinput
from fpdf import FPDF
import time
from mainGui import *

class Gui:
    def addVariables(self, mainWindow):
        print("addVariables worked")
        self.SENDER_ADDRESS = mainWindow.senderMail.text()
        self.RECEIVER_ADDRESS = mainWindow.receiverMail.text()
        self.RECEIVER = mainWindow.receiverName.text()
        self.SENDER = mainWindow.senderName.text()
        self.POSITION = mainWindow.appPosition.text()
        self.UNIVERSITY = mainWindow.senderSchool.text()
        self.FACULTY = mainWindow.senderDiv.text()
        self.PASSWORD = mainWindow.senderPass.text()
        self.MESSAGE = mainWindow.mailMessage.toPlainText()
        self.SUBJECT = mainWindow.mailSubject.text()

        #########
        self.RECEIVER_INFORMATION = mainWindow.receiverInfo.toPlainText()
        self.SENDER_SKILLS = mainWindow.senderSkills.toPlainText()
        self.SENDER_MORE = mainWindow.senderMore.toPlainText()
        #########

        self.ATTACH = 'ornekahmet.pdf'
        self.OUTPUT_PDF = "interview_letter.pdf"
        self.DATE = time.strftime("%x")
        self.PHONE = mainWindow.senderPhone.text()
        print("addVariables worked")
        self.pdfReadAndWrite()

    def pdfReadAndWrite(self):
        print("in")
        file = open("ornek.txt", "r+")
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

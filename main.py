#--coding: utf-8--
import smtplib
from gui import Gui
from pdf_attachment import Attachment
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mainGui import *


class Main():
    def __init__(self, mainWindow, filesWindow):
        self.SENDER = Gui()
        self.PDF_HANDLER = Attachment()


    def sendMail(self):
        self.s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        self.msg = MIMEMultipart()

        self.s.starttls()
        self.s.login(self.MY_ADDRESS, self.PASSWORD)

        self.msg['From'] = self.MY_ADDRESS
        self.msg['Subject'] = self.SUBJECT

        self.msg.attach(MIMEText(self.MESSAGE, "plain"))

        if (len(self.ATTACH) != 0):
            self.PDF_HANDLER.attach(self.msg, self.OUTPUT_PDF)
        self.msg['To'] = self.RECEIVER_ADDRESS

        self.s.send_message(self.msg)
        self.s.quit()

        filesWindow.close()

    def getVars(self):
        self.SENDER.addVariables(mainWindow)

        self.MY_ADDRESS = self.SENDER.SENDER_ADDRESS
        self.RECEIVER_ADDRESS = self.SENDER.RECEIVER_ADDRESS
        self.PASSWORD = self.SENDER.PASSWORD
        self.MESSAGE = self.SENDER.MESSAGE
        self.ATTACH = self.SENDER.ATTACH
        self.SUBJECT = self.SENDER.SUBJECT
        self.OUTPUT_PDF = self.SENDER.OUTPUT_PDF

        mainWindow.close()
        filesWindow.show()


app = QtWidgets.QApplication(sys.argv)
mainWindow = Ui_MAIN()
filesWindow = Ui_FILES()
mainWindow.show()

main = Main(mainWindow, filesWindow)

mainWindow.appButton.clicked.connect(lambda: main.getVars())
filesWindow.pushButton.clicked.connect(lambda: main.sendMail())

sys.exit(app.exec_())

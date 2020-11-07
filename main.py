#--coding: utf-8--
import smtplib
from gui import Gui
from pdf_attachment import Attachment
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER = Gui()
PDF_HANDLER = Attachment()
MY_ADDRESS = SENDER.SENDER_ADDRESS
RECEIVER_ADDRESS = SENDER.RECEIVER_ADDRESS
PASSWORD = SENDER.PASSWORD
MESSAGE = SENDER.MESSAGE
ATTACH = SENDER.ATTACH
SUBJECT = SENDER.SUBJECT
OUTPUT_PDF = SENDER.outputPdfNames

# create a message


def main():
    # set up the SMTP server

    # send the message via the server set up earlier.
    for y in range(len(RECEIVER_ADDRESS)):
        msg = MIMEMultipart()
        
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        # Prints out the message body for our sake
        print(MESSAGE)
        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['Subject'] = SUBJECT

        # add in the message body
        msg.attach(MIMEText(MESSAGE, "plain"))
        SENDER.pdfReadAndWrite(y)

        if (len(ATTACH) != 0):
            PDF_HANDLER.attach(msg, OUTPUT_PDF[y])
        msg['To'] = RECEIVER_ADDRESS[y]
        print(RECEIVER_ADDRESS[y])
        s.send_message(msg)

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()

import smtplib
from gui import Gui
from pdf_attachment import Attachment
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER = Gui()
PDF_HANDLER = Attachment()
MY_ADDRESS = SENDER.MY_ADDRESS
RECEIVER_ADDRESS = SENDER.RECEIVER_ADDRESS
PASSWORD = SENDER.PASSWORD
MESSAGE = SENDER.MESSAGE
ATTACH = SENDER.ATTACH
SUBJECT = SENDER.SUBJECT
OUTPUT_PDF = SENDER.OUTPUT_PDF

# create a message
msg = MIMEMultipart()

def main():
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # Prints out the message body for our sake
    print(MESSAGE)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=RECEIVER_ADDRESS
    msg['Subject']=SUBJECT

    # add in the message body
    msg.attach(MIMEText(MESSAGE, "plain"))
    SENDER.pdfReadAndWrite()

    if (len(ATTACH) != 0):
        PDF_HANDLER.attach(msg, OUTPUT_PDF)
        PDF_HANDLER.attach(msg, ATTACH)

    # send the message via the server set up earlier.
    s.send_message(msg)

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()

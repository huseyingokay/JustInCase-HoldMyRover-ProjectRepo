import smtplib
from gui import Gui
from pdf_attachment import Attachment
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sender1 = Gui()
sender2 = Attachment()
MY_ADDRESS = sender1.MY_ADDRESS
RECEIVER_ADDRESS = sender1.RECEIVER_ADDRESS
PASSWORD = sender1.PASSWORD
MESSAGE = sender1.MESSAGE
ATTACH = sender1.ATTACH
SUBJECT = sender1.SUBJECT

msg = MIMEMultipart()


def main():
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # create a message


    # Prints out the message body for our sake
    print(MESSAGE)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=RECEIVER_ADDRESS
    msg['Subject']=SUBJECT

    # add in the message body
    msg.attach(MIMEText(MESSAGE, "plain"))

    if (ATTACH != ''):
        sender2.attach(msg,ATTACH)



    # send the message via the server set up earlier.
    s.send_message(msg)

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'huseyingokay_1999@hotmail.com'
PASSWORD = 'XRAYSKINGSTAR8520'

def main():
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message ='Ahmet'

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']="cagatay.savasli@ozu.edu.tr"
    msg['Subject']="This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()

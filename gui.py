#!/usr/bin/python
import smtplib
from email.mime.base import MIMEBase
from email import encoders

class Gui:
    MY_ADDRESS = 'huseyingokay_1999@hotmail.com'
    PASSWORD = 'XRAYSKINGSTAR8520'
    MESSAGE = 'denemee'
    ATTACH =


def attach:
    with open("ornekahmet.pdf", "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")

    attach.add_header('Content-Disposition','attachment',filename=str("ornekahmet.pdf"))

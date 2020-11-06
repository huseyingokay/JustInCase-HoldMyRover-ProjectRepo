#!/usr/bin/python
import smtplib
from email.mime.application import MIMEApplication


class Attachment:
    def attach(self,msg):
        with open("ornekahmet.pdf", "rb") as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")

        attach.add_header('Content-Disposition','attachment',filename=str("ornekahmet.pdf"))
        msg.attach(attach)


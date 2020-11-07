#!/usr/bin/python
#--coding: utf-8--
from email.mime.application import MIMEApplication

class Attachment:
    def attach(self, msg, ATTACH):
        with open(ATTACH, "rb") as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")

        attach.add_header('Content-Disposition','attachment',filename=str(ATTACH))
        msg.attach(attach)

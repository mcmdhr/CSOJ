# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 16:14
# Filename     : mail.py
# Description :
#=============================================================================
from envelops import Envelop

from django.conf import settings

def send_email(from_name, to_email, to_name, subject, content):
    envelop = Envelop(from_addr=(settings.SMTP_CONFIG["email"], from_name),
                      to_addr=(to_email, to_name),
                      subject=subject,
                      html_body=content)
    envelop.send(settings.SMTP_CONFIG["smtp_server"],
                 login=settings.SMTP_CONFIG["email"],
                 password=settings.SMTP_CONFIG["password"],
                 tls=settings.SMTP_CONFIG["tls"])

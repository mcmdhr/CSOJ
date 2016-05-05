# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-26 10:59
# Filename     : tasks.py
# Description :
#=============================================================================
from celery import shared_task
from utils.mail import send_email


@shared_task
def _send_email(from_name, to_email, to_name, subject, content):
    send_email(from_name, to_email, to_name, subject, content)

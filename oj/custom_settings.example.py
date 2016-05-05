# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-05-04 13:53
# Filename     : custom_settings.example.py
# Description :
#=============================================================================
import os


WEBSITE_INFO = {"website_name": u"四川师范大学 OnlineJudge",
                "website_name_shortcut": u"cs oj",
                "website_footer": u"四川师范大学计算机科学学院",
                # url结尾没有/
                "url": u"http://your-domain-or-ip.com"}


SMTP_CONFIG = {"smtp_server": "smtp.domain.com",
               "email": "noreply@domain.com",
               "password": "your_password",
               "tls": False}

# please set your own SECRET_KEY to a long random string
# SECRET_KEY = ""

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
                "website_name_shortcut": u"四川师范大学 oj",
                "website_footer": u"四川师范大学 ACM-ICPC",
                # url结尾没有/
                "url": u"https://your-domain-or-ip.com"}


SMTP_CONFIG = {"smtp_server": "smtp.xxx.com",
               "email": "noreply@xxx.com",
               "password": os.environ.get("smtp_password", "111111"),
               "tls": False}

# please set your own SECRET_KEY to a long random string
# SECRET_KEY = ""

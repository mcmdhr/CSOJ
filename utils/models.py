# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 16:29
# Filename     : models.py
# Description :
#=============================================================================
import json
from django.db import models

from utils.xss_filter import XssHtml


class RichTextField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def get_prep_value(self, value):
        if not value:
            value = ""
        parser = XssHtml()
        parser.feed(value)
        parser.close()
        return parser.getHtml()


class JsonField(models.TextField):
    pass

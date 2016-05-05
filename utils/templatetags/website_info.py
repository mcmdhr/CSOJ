# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 15:19
# Filename     : website.py
# Description :
#=============================================================================
from django import template
from django.conf import settings
register = template.Library()


@register.simple_tag
def show_website_info(name):
    return settings.WEBSITE_INFO[name]

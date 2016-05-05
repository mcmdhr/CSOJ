# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 15:19
# Filename     : user.py
# Description :
#=============================================================================
import datetime
from account.models import User


def get_username(user_id):
    try:
        return User.objects.get(id=user_id).username
    except User.DoesNotExist:
        return ""


from django import template

register = template.Library()
register.filter("get_username", get_username)

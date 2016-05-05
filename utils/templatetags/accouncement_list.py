# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 15:18
# Filename     : accouncement_list.py
# Description :
#=============================================================================
from django import template

from announcement.models import Announcement


def public_announcement_list():
    return Announcement.objects.filter(visible=True).order_by("-create_time")

register = template.Library()
register.assignment_tag(public_announcement_list, name="public_announcement_list")

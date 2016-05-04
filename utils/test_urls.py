#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 16:29
# Filename     : test_urls.py
# Description :
#=============================================================================
# coding=utf-8
from django.conf.urls import include, url



urlpatterns = [
    url(r'^paginate_test/$', "utils.tests.pagination_test_func"),
]

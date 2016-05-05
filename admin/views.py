# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-26 17:11
# Filename     : views.py
# Description :
#=============================================================================
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from rest_framework.views import APIView


class AdminTemplateView(APIView):
    def get(self, request, template_dir, template_name):
        path = os.path.join(settings.TEMPLATES[0]["DIRS"][0], "admin", template_dir, template_name + ".html")
        try:
            return HttpResponse(open(path).read(), content_type="text/html")
        except IOError:
            return HttpResponse(u"模板不存在", content_type="text/html")

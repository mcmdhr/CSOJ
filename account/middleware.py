#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-26 10:09
# Filename     : middleware.py
# Description :
#=============================================================================
# codeing=utf-8
import time
import json
import urllib
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from utils.shortcuts import error_response, error_page
from .models import ADMIN

class SessionSecurityMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated() and request.user.admin_type >= ADMIN:
            if "last_activity" in request.session:
                # There are 24 hours with no activity
                if time.time() - request.session["last_activity"] >= 24 * 60 * 60:
                    auth.logout(request)
                    if request.is_ajax():
                        return HttpResponse(json.dumps({"code": 1, "data": u"Please login"}),
                                            content_type="application/json")
                    else:
                        return HttpResponseRedirect("/login/?__from=" + urllib.quote(request.build_absolute_uri()))
            # update last activity time
            request.session["last_activity"] = time.time()

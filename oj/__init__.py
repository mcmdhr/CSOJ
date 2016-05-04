#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-05-04 13:52
# Filename     : __init__.py
# Description :
#=============================================================================
"""
   ___         _  _                  __              _
  /___\ _ __  | |(_) _ __    ___     \ \  _   _   __| |  __ _   ___
 //  //| '_ \ | || || '_ \  / _ \     \ \| | | | / _` | / _` | / _ \
/ \_// | | | || || || | | ||  __/  /\_/ /| |_| || (_| || (_| ||  __/
\___/  |_| |_||_||_||_| |_| \___|  \___/  \__,_| \__,_| \__, | \___|
                                                        |___/
https://github.com/mcmdhr/CSOJ.git
"""
from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

#!/user/bin/env python

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 09:39
# Filename     : manage.py
# Description :
#=============================================================================

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oj.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

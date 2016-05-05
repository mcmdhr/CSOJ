#!/usr/bin/env bash

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-05-04 14:09
# Filename     : runtest.sh
# Description :
#=============================================================================
coverage run --source='.' manage.py test
test_result=$?
if [ "$test_result" -eq 0 ];then
    coverage html
    open htmlcov/index.html
fi

# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 14:56
# Filename     : tasks.py
# Description :
#=============================================================================
from __future__ import absolute_import
from celery import shared_task
from judge_dispatcher.tasks import JudgeDispatcher


@shared_task
def _judge(submission, time_limit, memory_limit, test_case_id):
    JudgeDispatcher(submission, time_limit, memory_limit, test_case_id).judge()

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 16:49
# Filename     : logger.py
# Description :
#=============================================================================
# coding=utf-8
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
                    filename='log/judge.log')

logger = logging

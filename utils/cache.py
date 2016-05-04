#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-27 16:11
# Filename     : cache.py
# Description :
#=============================================================================
# codeing=utf-8
import redis
from django.conf import settings

def get_cache_redis():
    return redis.Redis(host=settings.REDIS_CACHE["host"],
                       port=settings.REDIS_CACHE["port"],
                       db=settings.REDIS_CACHE["db"])

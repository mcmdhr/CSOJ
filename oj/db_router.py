# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-05-04 13:53
# Filename     : db_router.py
# Description :
#=============================================================================


class DBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'submission':
            return 'submission'
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'submission':
            return 'submission'
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == "submission":
            return db == app_label
        else:
            return db == "default"

# coding=utf-8

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-05-04 13:50
# Filename     : serializers.py
# Description :
#=============================================================================
import json
from rest_framework import serializers
from .models import JudgeServer


class CreateJudgesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    ip = serializers.IPAddressField()
    port = serializers.IntegerField()
    # 这个服务器最大可能运行的判题实例数量
    max_instance_number = serializers.IntegerField()
    token = serializers.CharField(max_length=30)


class EditJudgesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    ip = serializers.IPAddressField()
    port = serializers.IntegerField()
    # 这个服务器最大可能运行的判题实例数量
    max_instance_number = serializers.IntegerField()
    token = serializers.CharField(max_length=30)
    status = serializers.BooleanField()


class JudgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeServer

#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-04-26 10:19
# Filename     : models.py
# Description :
#=============================================================================
# codeing = utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from jsonfield import JSONField

class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

REGULAR_USER = 0
ADMIN = 1
SUPER_ADMIN = 2

class User(AbstractBaseUser):
    # username
    username = models.CharField(max_length=30, unique=True)
    # realname
    real_name = models.CharField(max_length=30, blank=True, null=True)
    # email
    email = models.EmailField(max_length=254, blank=True, null=True)
    # user's register time
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # 0=not admin 1=admin 2=super
    admin_type = models.InergerField(default=0)
    # 1=ac 2=testing
    problem_status = JSONField(default={})
    # token of reset password
    reset_password_token = models.CharField(max_length=40, blank=True, null=True)
    # create time of token
    reset_password_token_create_time = models.DateTimeField(blank=True, null=True)
    # SSO auth token
    auth_token = models.CharField(max_length=40, blank=True, null=True)
    # open auth?
    two_factor_auth = models.BooleanField(default=False)
    tfa_token = models.CharField(max_length=40, blank=True, null=True)
    # open api key
    openapi_appkey = models.CharField(max_length=35, blank=True, null=True)
    # forbidden user
    is_forbidden = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"

def _random_avatar():
    import random
    return "/static/img/avatar/avatar-" + str(random.randint(1, 20)) + ".png"

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.CharField(max_length=50, default=_random_avatar)
    blog = models.URLField(blank=True, null=True)
    mood = models.CharField(max_length=200, blank=True, null=True)
    hduoj_username = models.CharField(max_length=30, blank=True, null=True)
    bestcoder_username = models.CharField(max_length=30, blank=True, null=True)
    codeforces_username = models.CharField(max_length=30, blank=True, null=True)
    rank = models.IntegerField(default=65535)
    accepted_number = models.IntegerField(default=0)
    submissions_number = models.IntegerField(default=0)
    problems_status = JSONField(default={})
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    student_id = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "user_profile"

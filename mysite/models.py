# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AChannelSet(models.Model):
    channel = models.CharField(unique=True, max_length=50)
    parent_id = models.IntegerField()
    weight = models.IntegerField()
    status = models.IntegerField()
    operator = models.CharField(max_length=50, blank=True, null=True)
    utime = models.DateTimeField()
    ctime = models.DateTimeField()
    remark = models.CharField(max_length=200)
    channel_type = models.CharField(max_length=10)
    is_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_channel_set'


class AMenu(models.Model):
    type = models.CharField(max_length=20)
    action = models.CharField(unique=True, max_length=20)
    status = models.IntegerField()
    name = models.CharField(max_length=50)
    parent_id = models.IntegerField()
    icon = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'a_menu'


class AUserExtra(models.Model):
    permission_str = models.TextField()
    role = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'a_user_extra'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OBanner(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    os_type = models.IntegerField(blank=True, null=True)
    pic_url = models.CharField(max_length=200, blank=True, null=True)
    click_url = models.CharField(max_length=500, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    channel = models.TextField(blank=True, null=True)
    channel_type = models.IntegerField()
    open_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'o_banner'


class OUserBasic(models.Model):
    uid = models.AutoField(primary_key=True)
    ctime = models.DateTimeField()
    channel = models.CharField(max_length=16)
    os_type = models.CharField(max_length=8)
    app_version = models.CharField(max_length=16)
    package_name = models.CharField(max_length=30)
    reg_ip = models.CharField(max_length=15)
    invite_uid = models.IntegerField()
    reg_source = models.CharField(max_length=2)
    reg_qid = models.CharField(max_length=64)
    bind_mobile = models.BigIntegerField()
    status = models.IntegerField()
    utime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'o_user_basic'


class OUserExtra(models.Model):
    uid = models.IntegerField(primary_key=True)
    reg_source = models.CharField(max_length=2)
    reg_qid = models.CharField(max_length=64)
    token = models.CharField(max_length=256)
    ticket = models.CharField(max_length=256)
    nickname = models.CharField(max_length=512)
    gender = models.CharField(max_length=1)
    figure_url = models.CharField(max_length=256)
    figure_url_other = models.CharField(max_length=1000, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_user_extra'


class OUserMsg00(models.Model):
    uid = models.IntegerField()
    info_title = models.CharField(max_length=50)
    info_subtitle = models.CharField(max_length=64)
    content = models.TextField()
    share_msg = models.CharField(max_length=255)
    info_time = models.DateTimeField()
    info_type = models.IntegerField()
    info_notify = models.IntegerField()
    status = models.IntegerField()
    end_time = models.DateTimeField()
    click_url = models.CharField(max_length=300, blank=True, null=True)
    button_text = models.CharField(max_length=40, blank=True, null=True)
    url_images = models.CharField(max_length=500)
    share_url = models.CharField(max_length=500)
    category = models.CharField(max_length=20)
    icon = models.CharField(max_length=500)
    pid = models.IntegerField()
    package_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'o_user_msg_00'


class OVerifyLog(models.Model):
    pnum = models.BigIntegerField()
    device_id = models.CharField(max_length=50)
    status = models.IntegerField()
    code = models.CharField(max_length=6)
    package_name = models.CharField(max_length=100, blank=True, null=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    os_type = models.CharField(max_length=20, blank=True, null=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'o_verify_log'


class OVersion(models.Model):
    version = models.CharField(max_length=15)
    os_type = models.CharField(max_length=10)
    ctime = models.DateTimeField()
    what_news = models.TextField()
    update_is_recommend = models.IntegerField()
    update_is_force = models.IntegerField()
    app_id = models.IntegerField()
    dl_url = models.CharField(max_length=255)
    channel = models.CharField(max_length=36)
    status = models.IntegerField()
    rate = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'o_version'
        unique_together = (('version', 'os_type', 'app_id', 'channel'),)


class TDeviceUid(models.Model):
    device_id = models.CharField(max_length=50, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_device_uid'

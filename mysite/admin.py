# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AChannelSetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'channel',
        'parent_id',
        'weight',
        'status',
        'operator',
        'utime',
        'ctime',
        'remark',
        'channel_type',
        'is_public',
    )
    list_filter = ('utime', 'ctime')


class AMenuAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'type',
        'action',
        'status',
        'name',
        'parent_id',
        'icon',
    )
    search_fields = ('name',)


class AUserExtraAdmin(admin.ModelAdmin):

    list_display = ('id', 'permission_str', 'role', 'user')
    list_filter = ('user',)


class AuthGroupAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class AuthGroupPermissionsAdmin(admin.ModelAdmin):

    list_display = ('id', 'group', 'permission')
    list_filter = ('group', 'permission')


class AuthPermissionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'content_type', 'codename')
    list_filter = ('content_type',)
    search_fields = ('name',)


class AuthUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_filter = ('last_login', 'date_joined')


class AuthUserGroupsAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'group')
    list_filter = ('user', 'group')


class AuthUserUserPermissionsAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'permission')
    list_filter = ('user', 'permission')


class DjangoAdminLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message',
        'content_type',
        'user',
    )
    list_filter = ('action_time', 'content_type', 'user')


class DjangoContentTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'app_label', 'model')


class DjangoMigrationsAdmin(admin.ModelAdmin):

    list_display = ('id', 'app', 'name', 'applied')
    list_filter = ('applied',)
    search_fields = ('name',)


class DjangoSessionAdmin(admin.ModelAdmin):

    list_display = ('session_key', 'session_data', 'expire_date')
    list_filter = ('expire_date',)


class OBannerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'os_type',
        'pic_url',
        'click_url',
        'ctime',
        'utime',
        'start_time',
        'end_time',
        'seq',
        'status',
        'channel',
        'channel_type',
        'open_type',
    )
    list_filter = ('ctime', 'utime', 'start_time', 'end_time')
    search_fields = ('name',)


class OUserBasicAdmin(admin.ModelAdmin):

    list_display = (
        'uid',
        'ctime',
        'channel',
        'os_type',
        'app_version',
        'package_name',
        'reg_ip',
        'invite_uid',
        'reg_source',
        'reg_qid',
        'bind_mobile',
        'status',
        'utime',
    )
    list_filter = ('ctime', 'utime')


class OUserExtraAdmin(admin.ModelAdmin):

    list_display = (
        'uid',
        'reg_source',
        'reg_qid',
        'token',
        'ticket',
        'nickname',
        'gender',
        'figure_url',
        'figure_url_other',
        'province',
        'city',
        'country',
        'year',
        'point',
    )


class OUserMsg00Admin(admin.ModelAdmin):

    list_display = (
        'id',
        'uid',
        'info_title',
        'info_subtitle',
        'content',
        'share_msg',
        'info_time',
        'info_type',
        'info_notify',
        'status',
        'end_time',
        'click_url',
        'button_text',
        'url_images',
        'share_url',
        'category',
        'icon',
        'pid',
        'package_name',
    )
    list_filter = ('info_time', 'end_time')


class OVerifyLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'pnum',
        'device_id',
        'status',
        'code',
        'package_name',
        'app_version',
        'os_type',
        'ctime',
    )
    list_filter = ('ctime',)


class OVersionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'version',
        'os_type',
        'ctime',
        'what_news',
        'update_is_recommend',
        'update_is_force',
        'app_id',
        'dl_url',
        'channel',
        'status',
        'rate',
    )
    list_filter = ('ctime',)


class TDeviceUidAdmin(admin.ModelAdmin):

    list_display = ('id', 'device_id', 'uid', 'ctime', 'utime')
    list_filter = ('ctime', 'utime')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AChannelSet, AChannelSetAdmin)
_register(models.AMenu, AMenuAdmin)
_register(models.AUserExtra, AUserExtraAdmin)
_register(models.AuthGroup, AuthGroupAdmin)
_register(models.AuthGroupPermissions, AuthGroupPermissionsAdmin)
_register(models.AuthPermission, AuthPermissionAdmin)
_register(models.AuthUser, AuthUserAdmin)
_register(models.AuthUserGroups, AuthUserGroupsAdmin)
_register(models.AuthUserUserPermissions, AuthUserUserPermissionsAdmin)
_register(models.DjangoAdminLog, DjangoAdminLogAdmin)
_register(models.DjangoContentType, DjangoContentTypeAdmin)
_register(models.DjangoMigrations, DjangoMigrationsAdmin)
_register(models.DjangoSession, DjangoSessionAdmin)
_register(models.OBanner, OBannerAdmin)
_register(models.OUserBasic, OUserBasicAdmin)
_register(models.OUserExtra, OUserExtraAdmin)
_register(models.OUserMsg00, OUserMsg00Admin)
_register(models.OVerifyLog, OVerifyLogAdmin)
_register(models.OVersion, OVersionAdmin)
_register(models.TDeviceUid, TDeviceUidAdmin)
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AChannelSetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'channel',
        'parent_id',
        'weight',
        'status',
        'operator',
        'utime',
        'ctime',
        'remark',
        'channel_type',
        'is_public',
    )
    list_filter = ('utime', 'ctime')


class AMenuAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'type',
        'action',
        'status',
        'name',
        'parent_id',
        'icon',
    )
    search_fields = ('name',)


class AUserExtraAdmin(admin.ModelAdmin):

    list_display = ('id', 'permission_str', 'role', 'user')
    list_filter = ('user',)


class AuthGroupAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class AuthGroupPermissionsAdmin(admin.ModelAdmin):

    list_display = ('id', 'group', 'permission')
    list_filter = ('group', 'permission')


class AuthPermissionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'content_type', 'codename')
    list_filter = ('content_type',)
    search_fields = ('name',)


class AuthUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_filter = ('last_login', 'date_joined')


class AuthUserGroupsAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'group')
    list_filter = ('user', 'group')


class AuthUserUserPermissionsAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'permission')
    list_filter = ('user', 'permission')


class DjangoAdminLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message',
        'content_type',
        'user',
    )
    list_filter = ('action_time', 'content_type', 'user')


class DjangoContentTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'app_label', 'model')


class DjangoMigrationsAdmin(admin.ModelAdmin):

    list_display = ('id', 'app', 'name', 'applied')
    list_filter = ('applied',)
    search_fields = ('name',)


class DjangoSessionAdmin(admin.ModelAdmin):

    list_display = ('session_key', 'session_data', 'expire_date')
    list_filter = ('expire_date',)


class OBannerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'os_type',
        'pic_url',
        'click_url',
        'ctime',
        'utime',
        'start_time',
        'end_time',
        'seq',
        'status',
        'channel',
        'channel_type',
        'open_type',
    )
    list_filter = ('ctime', 'utime', 'start_time', 'end_time')
    search_fields = ('name',)


class OUserBasicAdmin(admin.ModelAdmin):

    list_display = (
        'uid',
        'ctime',
        'channel',
        'os_type',
        'app_version',
        'package_name',
        'reg_ip',
        'invite_uid',
        'reg_source',
        'reg_qid',
        'bind_mobile',
        'status',
        'utime',
    )
    list_filter = ('ctime', 'utime')


class OUserExtraAdmin(admin.ModelAdmin):

    list_display = (
        'uid',
        'reg_source',
        'reg_qid',
        'token',
        'ticket',
        'nickname',
        'gender',
        'figure_url',
        'figure_url_other',
        'province',
        'city',
        'country',
        'year',
        'point',
    )


class OUserMsg00Admin(admin.ModelAdmin):

    list_display = (
        'id',
        'uid',
        'info_title',
        'info_subtitle',
        'content',
        'share_msg',
        'info_time',
        'info_type',
        'info_notify',
        'status',
        'end_time',
        'click_url',
        'button_text',
        'url_images',
        'share_url',
        'category',
        'icon',
        'pid',
        'package_name',
    )
    list_filter = ('info_time', 'end_time')


class OVerifyLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'pnum',
        'device_id',
        'status',
        'code',
        'package_name',
        'app_version',
        'os_type',
        'ctime',
    )
    list_filter = ('ctime',)


class OVersionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'version',
        'os_type',
        'ctime',
        'what_news',
        'update_is_recommend',
        'update_is_force',
        'app_id',
        'dl_url',
        'channel',
        'status',
        'rate',
    )
    list_filter = ('ctime',)


class TDeviceUidAdmin(admin.ModelAdmin):

    list_display = ('id', 'device_id', 'uid', 'ctime', 'utime')
    list_filter = ('ctime', 'utime')


def _register(model, admin_class):
    admin.site.register(model, admin_class)

try:
    _register(models.AChannelSet, AChannelSetAdmin)
    _register(models.AMenu, AMenuAdmin)
    _register(models.AUserExtra, AUserExtraAdmin)
    _register(models.AuthGroup, AuthGroupAdmin)
    _register(models.AuthGroupPermissions, AuthGroupPermissionsAdmin)
    _register(models.AuthPermission, AuthPermissionAdmin)
    _register(models.AuthUser, AuthUserAdmin)
    _register(models.AuthUserGroups, AuthUserGroupsAdmin)
    _register(models.AuthUserUserPermissions, AuthUserUserPermissionsAdmin)
    _register(models.DjangoAdminLog, DjangoAdminLogAdmin)
    _register(models.DjangoContentType, DjangoContentTypeAdmin)
    _register(models.DjangoMigrations, DjangoMigrationsAdmin)
    _register(models.DjangoSession, DjangoSessionAdmin)
    _register(models.OBanner, OBannerAdmin)
    _register(models.OUserBasic, OUserBasicAdmin)
    _register(models.OUserExtra, OUserExtraAdmin)
    _register(models.OUserMsg00, OUserMsg00Admin)
    _register(models.OVerifyLog, OVerifyLogAdmin)
    _register(models.OVersion, OVersionAdmin)
    _register(models.TDeviceUid, TDeviceUidAdmin)

except Exception as e:
    pass

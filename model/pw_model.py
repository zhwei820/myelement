from peewee import *

database = MySQLDatabase('pinax_mysite', **{'user': 'root', 'password': 'zw'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AChannelSet(BaseModel):
    admin = CharField()
    channel = CharField(unique=True)
    channel_type = IntegerField()
    ctime = DateTimeField()
    is_public = IntegerField()
    parent = IntegerField(db_column='parent_id')
    remark = CharField()
    status = IntegerField()
    utime = DateTimeField()
    weight = IntegerField()

    class Meta:
        db_table = 'a_channel_set'

class AMenu(BaseModel):
    action = CharField(unique=True)
    icon = CharField()
    name = CharField()
    parent = IntegerField(db_column='parent_id')
    status = IntegerField(index=True)
    type = CharField()

    class Meta:
        db_table = 'a_menu'

class AMenuUser(BaseModel):
    group = IntegerField(db_column='group_id', null=True)
    m = IntegerField(db_column='m_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'a_menu_user'
        indexes = (
            (('m', 'user'), True),
        )

class AMessageSend(BaseModel):
    admin = CharField()
    button_text = CharField(null=True)
    category = CharField()
    click_url = CharField(null=True)
    content = TextField()
    ctime = DateTimeField()
    end_time = DateTimeField()
    icon = CharField()
    info_notify = IntegerField()
    info_subtitle = CharField()
    info_title = CharField()
    message_type = IntegerField()
    message_url = CharField()
    os_type = IntegerField()
    package_name = CharField(index=True)
    rate = CharField()
    share_msg = CharField()
    share_url = CharField()
    start_time = DateTimeField()
    status = IntegerField()
    uid_batch = TextField()
    url_images = CharField()

    class Meta:
        db_table = 'a_message_send'

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        db_table = 'auth_user'

class AUserExtra(BaseModel):
    permission_str = TextField()
    role = IntegerField()
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id', unique=True)

    class Meta:
        db_table = 'a_user_extra'

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        db_table = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(db_column='content_type_id', rel_model=DjangoContentType, to_field='id')
    name = CharField()

    class Meta:
        db_table = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(db_column='group_id', rel_model=AuthGroup, to_field='id')
    permission = ForeignKeyField(db_column='permission_id', rel_model=AuthPermission, to_field='id')

    class Meta:
        db_table = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthUserGroups(BaseModel):
    group = ForeignKeyField(db_column='group_id', rel_model=AuthGroup, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'auth_user_groups'
        indexes = (
            (('user', 'group'), True),
        )

class AuthUserUserPermissions(BaseModel):
    permission = ForeignKeyField(db_column='permission_id', rel_model=AuthPermission, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'auth_user_user_permissions'
        indexes = (
            (('user', 'permission'), True),
        )

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(db_column='content_type_id', null=True, rel_model=DjangoContentType, to_field='id')
    object = TextField(db_column='object_id', null=True)
    object_repr = CharField()
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'django_admin_log'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        db_table = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        db_table = 'django_session'

class OBanner(BaseModel):
    channel = TextField(null=True)
    channel_type = IntegerField()
    click_url = CharField(null=True)
    ctime = DateTimeField(null=True)
    description = CharField(null=True)
    end_time = DateTimeField(null=True)
    name = CharField(null=True)
    open_type = CharField()
    os_type = IntegerField(null=True)
    pic_url = CharField(null=True)
    seq = IntegerField(null=True)
    start_time = DateTimeField(null=True)
    status = IntegerField(null=True)
    utime = DateTimeField(null=True)

    class Meta:
        db_table = 'o_banner'

class OUserBasic(BaseModel):
    app_version = CharField()
    bind_mobile = BigIntegerField(index=True)
    channel = CharField(index=True)
    ctime = DateTimeField(index=True)
    device = CharField(db_column='device_id', index=True, null=True)
    invite_uid = IntegerField(index=True)
    os_type = CharField(index=True)
    package_name = CharField()
    reg_ip = CharField()
    reg_qid = CharField(index=True)
    reg_source = CharField(index=True)
    salt = CharField(null=True)
    status = IntegerField(index=True)
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_basic'

class OUserExtra(BaseModel):
    city = CharField(null=True)
    country = CharField(null=True)
    figure_url = CharField()
    figure_url_other = CharField(null=True)
    gender = CharField()
    nickname = CharField()
    point = IntegerField(null=True)
    province = CharField(null=True)
    reg_qid = CharField()
    reg_source = CharField()
    ticket = CharField()
    token = CharField()
    uid = PrimaryKeyField()
    year = IntegerField(null=True)

    class Meta:
        db_table = 'o_user_extra'

class OUserMsg00(BaseModel):
    button_text = CharField(null=True)
    category = CharField()
    click_url = CharField(null=True)
    content = TextField()
    end_time = DateTimeField()
    icon = CharField()
    info_notify = IntegerField()
    info_subtitle = CharField()
    info_time = DateTimeField()
    info_title = CharField()
    info_type = IntegerField()
    package_name = CharField()
    pid = IntegerField(index=True)
    share_msg = CharField()
    share_url = CharField()
    status = IntegerField()
    uid = IntegerField()
    url_images = CharField()

    class Meta:
        db_table = 'o_user_msg_00'
        indexes = (
            (('uid', 'status'), False),
        )

class OUserScore0(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_0'

class OUserScore1(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_1'

class OUserScore2(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_2'

class OUserScore3(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_3'

class OUserScore4(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_4'

class OUserScore5(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_5'

class OUserScore6(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_6'

class OUserScore7(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_7'

class OUserScore8(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_8'

class OUserScore9(BaseModel):
    ctime = DateTimeField(index=True)
    score = IntegerField()
    score_active = IntegerField()
    score_cancel_consumption = IntegerField()
    score_cancel_withdraw = IntegerField()
    score_charge_alipay = IntegerField()
    score_charge_hbb = IntegerField()
    score_charge_weixin = IntegerField()
    score_consumption = IntegerField()
    score_field_1 = IntegerField()
    score_field_2 = IntegerField()
    score_field_3 = IntegerField()
    score_field_4 = IntegerField()
    score_field_5 = IntegerField()
    score_invite = IntegerField()
    score_predeposit = IntegerField()
    score_register = IntegerField()
    score_task = IntegerField()
    score_withdraw = IntegerField()
    uid = PrimaryKeyField()
    utime = DateTimeField()

    class Meta:
        db_table = 'o_user_score_9'

class OVerifyLog(BaseModel):
    app_version = CharField(null=True)
    code = CharField()
    ctime = DateTimeField(index=True)
    device = CharField(db_column='device_id')
    os_type = CharField(null=True)
    package_name = CharField(null=True)
    pnum = BigIntegerField(index=True)
    status = IntegerField()

    class Meta:
        db_table = 'o_verify_log'

class OVersion(BaseModel):
    app = IntegerField(db_column='app_id')
    channel = CharField()
    ctime = DateTimeField()
    dl_url = CharField()
    os_type = CharField()
    rate = TextField()
    status = IntegerField()
    update_is_force = IntegerField()
    update_is_recommend = IntegerField()
    version = CharField()
    what_news = TextField()

    class Meta:
        db_table = 'o_version'
        indexes = (
            (('version', 'os_type', 'app', 'channel'), True),
        )

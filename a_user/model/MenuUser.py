# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class MenuUser(Model):
    table_prefix = 'a_'
    table_name = 'menu_user'
    m_id = Field()
    user_id = Field()

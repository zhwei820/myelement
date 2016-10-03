# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class UserGroup(Model):
    table_name = 'auth_group'
    id = Field()
    name = Field()

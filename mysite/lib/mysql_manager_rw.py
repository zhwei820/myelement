# -*- coding: UTF-8 -*-
"""
mysql连接管理类
只能在django里面用

主要目标：
带读写分离，带多读库支持

次要目标：
带任何条件下数据库异步

@author: zh
"""
import MySQLdb
import warnings
import traceback
import MySQLdb.cursors
from django.conf import settings as _options

class mmysql_rw:
    default_charset = "utf8"

    def __init__(self, db_name=""):
        self.default_db_name = db_name
        self.auto_commit = False

        self.db = None
        self.cur = None

    def get_conn(self, auto_commit=True):
        if self.db is None:
            db_name = self.default_db_name
            self.auto_commit = auto_commit
            # 主库 读写
            if not db_name:
                self.db = MySQLdb.Connect(host=_options.DATABASES['default']['HOST'], user=_options.DATABASES['default']['USER'],
                                          passwd=_options.DATABASES['default']['PASSWORD'], port=int(_options.DATABASES['default']['PORT']),
                                          db=_options.DATABASES['default']['NAME'], charset=self.default_charset,
                                          cursorclass=MySQLdb.cursors.DictCursor)

                self.db.autocommit(self.auto_commit)
                self.cur = self.db.cursor()
            if db_name:
                self.db = MySQLdb.Connect(host=_options.DATABASES[db_name]['HOST'], user=_options.DATABASES[db_name]['USER'],
                                          passwd=_options.DATABASES[db_name]['PASSWORD'], port=int(_options.DATABASES[db_name]['PORT']),
                                          db=_options.DATABASES[db_name]['NAME'], charset=self.default_charset,
                                          cursorclass=MySQLdb.cursors.DictCursor)
                self.db.autocommit(self.auto_commit)
                self.cur = self.db.cursor()
        elif auto_commit != self.auto_commit:
            self.auto_commit = auto_commit
            self.db.autocommit(auto_commit)

    @staticmethod
    def F(sql):
        # 格式化字符串，避免sql攻击
        return MySQLdb.escape_string(sql)


    def SQ(self, sql, args=None):
        return self._query(sql, args)

    # 普通方式请求数据库
    def Q(self, sql, args=None):
        return self._query(sql, args)

    # 事物需要TQ支持 而不是Q
    def TQ(self, sql, args=None):
        try:
            self.get_conn(False)
            rs = self.cur.execute(sql, args)
            return rs
        except MySQLdb.Error as e:
            error("_query error: %s %s", sql, args, exc_info=True)
            raise e

    def _query(self, sql, args=None):
        try:
            self.get_conn()
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter('always')
#-#                info('execute %s %s', sql, args)
                rs = self.cur.execute(sql, args)
                if w:
                    # info('sql warning: %s %s %s', sql, args, w[-1].message)
                    pass
            return rs
        except MySQLdb.Error as e:
            e.args = (e.args, sql, args)
            raise e
#-#            error("_query error: %s, %s", sql, e, exc_info=True)

    def fetch_one(self):
        return self.cur.fetchone()

    def fetch_all(self):
        return self.cur.fetchall()

    def executemany(self, sql, args):
        u'''批量执行多sql语句
        '''
        rslt = None
        try:
            self.get_conn(False)
            rslt = self.cur.executemany(sql, args)
            self.db.commit()
        except StandardError as e:
            info('got StandardError and rollback when do sql:%s, (total:%d)args[:5]=%s, e:\n%s', sql, len(args), args[:5], e)
            self.db.rollback()
            rslt = 0  # TODO necessary ?
            raise e
        except Exception as e:
            info('got Exception and rollback when do sql:%s, (total:%d)args[:5]=%s, e:\n%s', sql, len(args), args[:5], e)
            self.db.rollback()
            rslt = 0  # TODO necessary ?
            raise e
#-#        finally:
#-#            self.cur.close()

        return rslt

    def close(self):
        try:
            self.cur.close()
        except:
            pass
        try:
            self.db.close()
        except:
            pass
        finally:
            self.db = None

    def __del__(self):
        try:
            if self.db is not None:
                self.close()
        except:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 添加对with语句的支持
        try:
            if self.cur:
                self.cur.close()
        except:
            pass

        try:
            if self.db:
                self.close()
        except:
            pass

        if exc_type:
            sio = StringIO()
            traceback.print_exception(exc_type, exc_val, exc_tb, None, sio)
            s = sio.getvalue()
            sio.close()
            if s[-1:] == "\n":
                s = s[:-1]
            error('%s', s, exc_info=True)
        return True  # suppress exception
#-#        return False

    def insert_id(self):
        return self.cur.lastrowid

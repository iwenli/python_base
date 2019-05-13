# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-13 10:29:53
@LastEditors: iwenli
@LastEditTime: 2019-05-13 16:59:17
@Description: ...
'''
__author__ = 'iwenli'
from pymssql import connect
from db.customConst import DbConst


class TxMssql:
    '''Connection to a mssql'''

    # def __init__(self,user='',password='',database='',charset=None,port=1433)
    def __init__(self, **kwargs):
        try:
            server = kwargs["host"]
            database = kwargs["database"]
            user = kwargs["user"]
            pwd = kwargs["password"]
            self.__conn = connect(host=server,
                                  user=user,
                                  password=pwd,
                                  database=database)
            self.__cursor = None
            print('连接到数据库:', kwargs["database"])
        except Exception as err:
            print('mssql连接错误：' + err.msg)

    # def findBySql(self, sql, params={}, limit=0, join='AND'):
    def findBySql(self, **kwargs):
        '''
        自定义sql语句查找
        limit = 是否需要返回多少行
        params = dict(field=value)
        join = 'AND | OR'
        '''
        cursor = self.__getCursor()
        # sql = self.__joinWhere(kwargs["sql"], kwargs["params"], kwargs["join"])
        if kwargs.get("join", 0) == 0: kwargs["join"] = "AND"
        sql = self.__joinWhere(**kwargs)
        cursor.execute(sql, tuple(kwargs["params"].values()))
        rows = cursor.fetchmany(
            size=kwargs["limit"]) if kwargs["limit"] > 0 else cursor.fetchall(
            )
        # result = [dict(zip(cursor.column_names, row))
        #           for row in rows] if rows else None
        # return len(result)
        return rows

    # def countBySql(self,sql,params = {},join = 'AND'):
    def countBySql(self, **kwargs):
        '''自定义sql 统计影响行数'''
        if kwargs.get("join", 0) == 0: kwargs["join"] = "AND"
        cursor = self.__getCursor()
        # sql = self.__joinWhere(kwargs["sql"], kwargs["params"], kwargs["join"])
        sql = self.__joinWhere(**kwargs)
        cursor.execute(sql, tuple(kwargs["params"].values()))
        result = cursor.fetchall()  # fetchone是一条记录， fetchall 所有记录
        return len(result) if result else 0

    # def insert(self,table,data):
    def insert(self, **kwargs):
        '''新增一条记录
          table: 表名
          data: dict 插入的数据
        '''
        fields = ','.join(k for k in kwargs["data"].keys())
        values = ','.join(("%s", ) * len(kwargs["data"]))
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (kwargs["table"], fields,
                                                   values)
        cursor = self.__getCursor()
        cursor.execute(sql, tuple(kwargs["data"].values()))
        insert_id = cursor.lastrowid
        self.__conn.commit()
        return insert_id

    # def updateByAttr(self,table,data,params={},join='AND'):
    def updateByAttr(self, **kwargs):
        #     '''更新数据'''
        if kwargs.get("params", 0) == 0:
            kwargs["params"] = {}
        if kwargs.get("join", 0) == 0:
            kwargs["join"] = "AND"
        fields = ','.join(k + '=%s' for k in kwargs["data"].keys())
        values = list(kwargs["data"].values())

        values.extend(list(kwargs["params"].values()))
        sql = "UPDATE %s SET %s " % (kwargs["table"], fields)
        kwargs["sql"] = sql
        sql = self.__joinWhere(**kwargs)
        cursor = self.__getCursor()
        cursor.execute(sql, tuple(values))
        self.__conn.commit()
        return cursor.rowcount

    # def updateByPk(self,table,data,id,pk='id'):
    def updateByPk(self, **kwargs):
        '''根据主键更新，默认是id为主键'''
        return self.updateByAttr(**kwargs)

    # def deleteByAttr(self,table,params={},join='AND'):
    def deleteByAttr(self, **kwargs):
        '''删除数据'''
        if kwargs.get("params", 0) == 0:
            kwargs["params"] = {}
        if kwargs.get("join", 0) == 0:
            kwargs["join"] = "AND"
        # fields = ','.join('`'+k+'`=%s' for k in kwargs["params"].keys())
        sql = "DELETE FROM %s " % kwargs["table"]
        kwargs["sql"] = sql
        # sql = self.__joinWhere(sql, kwargs["params"], kwargs["join"])
        sql = self.__joinWhere(**kwargs)
        cursor = self.__getCursor()
        cursor.execute(sql, tuple(kwargs["params"].values()))
        self.__conn.commit()
        return cursor.rowcount

    # def deleteByPk(self,table,id,pk='id'):
    def deleteByPk(self, **kwargs):
        '''根据主键删除，默认是id为主键'''
        return self.deleteByAttr(**kwargs)

    # def findByAttr(self,table,criteria = {}):
    def findByAttr(self, **kwargs):
        '''根據條件查找一條記錄'''
        return self.__query(**kwargs)

    # def findByPk(self,table,id,pk='id'):
    def findByPk(self, **kwargs):
        return self.findByAttr(**kwargs)

    # def findAllByAttr(self,table,criteria={}, whole=true):
    def findAllByAttr(self, **kwargs):
        '''根據條件查找記錄'''
        return self.__query(**kwargs)

    # def count(self,table,params={},join='AND'):
    def count(self, **kwargs):
        '''根据条件统计行数'''
        if kwargs.get("join", 0) == 0: kwargs["join"] = "AND"
        # sql = 'SELECT COUNT(*) FROM `%s`' % kwargs["table"]
        sql = 'SELECT COUNT(*) FROM %s' % kwargs["table"]
        # sql = self.__joinWhere(sql, kwargs["params"], kwargs["join"])
        kwargs["sql"] = sql
        sql = self.__joinWhere(**kwargs)
        cursor = self.__getCursor(False)
        cursor.execute(sql, tuple(kwargs["params"].values()))
        result = cursor.fetchone()
        return result[0] if result else 0

    # def exist(self,table,params={},join='AND'):
    def exist(self, **kwargs):
        '''判断是否存在'''
        return self.count(**kwargs) > 0

    def close(self):
        '''关闭游标和数据库连接'''
        if self.__cursor is not None:
            self.__cursor.close()
        self._conn.close()

    def __getCursor(self, as_dict=True):
        '''获取游标'''
        if self.__cursor is None:
            self.__cursor = self.__conn.cursor(as_dict)
        return self.__cursor

    # def __joinWhere(self,sql,params,join):
    def __joinWhere(self, **kwargs):
        '''转换params为where连接语句'''
        if kwargs["params"]:
            keys, _keys = self.__tParams(**kwargs)
            joinKey = "AND" if kwargs["join"].strip().upper(
            ) == ' AND ' else " OR "
            where = joinKey.join(k + '=' + str(_k)
                                 for k, _k in zip(keys, _keys))
            kwargs["sql"] += ' WHERE ' + where
        return kwargs["sql"]

    # def __tParams(self,params):
    def __tParams(self, **kwargs):
        keys = [k for k in kwargs["params"].keys()]
        _keys = [kwargs["params"][k] for k in kwargs["params"].keys()]
        return keys, _keys

    # def __query(self,table,criteria,whole=False):
    def __query(self, **kwargs):
        if kwargs.get("whole", False) == False or kwargs["whole"] is not True:
            kwargs["whole"] = False
            # kwargs["criteria"]['limit'] = 1
        # sql = self.__contact_sql(kwargs["table"], kwargs["criteria"])
        sql = self.__contact_sql(**kwargs)
        cursor = self.__getCursor()
        cursor.execute(sql)
        rows = cursor.fetchall() if kwargs["whole"] else cursor.fetchone()
        # result = [dict(zip(cursor.column_names, row))
        #           for row in rows] if kwargs["whole"] else dict(
        #               zip(cursor.column_names, rows)) if rows else None
        return rows

    # def __contact_sql(self,table,criteria):
    def __contact_sql(self, **kwargs):
        sql = 'SELECT '
        if kwargs["criteria"] and type(kwargs["criteria"]) is dict:
            # select fields
            if 'select' in kwargs["criteria"]:
                fields = kwargs["criteria"]['select'].split(',')
                sql += ','.join('`' + field + '`' for field in fields)
            else:
                sql += ' * '
            # table
            sql += ' FROM %s' % kwargs["table"]
            # where
            if 'where' in kwargs["criteria"]:
                sql += ' WHERE ' + kwargs["criteria"]['where']
            # group by
            if 'group' in kwargs["criteria"]:
                sql += ' GROUP BY ' + kwargs["criteria"]['group']
            # having
            if 'having' in kwargs["criteria"]:
                sql += ' HAVING ' + kwargs["criteria"]['having']
            # order by
            if 'order' in kwargs["criteria"]:
                sql += ' ORDER BY ' + kwargs["criteria"]['order']
            # limit
            if 'limit' in kwargs["criteria"]:
                sql += ' LIMIT ' + str(kwargs["criteria"]['limit'])
            # offset
            if 'offset' in kwargs["criteria"]:
                sql += ' OFFSET ' + str(kwargs["criteria"]['offset'])
        else:
            sql += ' * FROM `%s`' % kwargs["table"]
        return sql

    def findKeySql(self, key, **kwargs):
        sqlOperate = {
            DbConst.COUNT: lambda: self.count(**kwargs),
            DbConst.COUNT_BY_SQL: lambda: self.countBySql(**kwargs),
            DbConst.DELETE_BY_ATTR: lambda: self.deleteByAttr(**kwargs),
            DbConst.EXIST: lambda: self.exist(**kwargs),
            DbConst.FIND_ALL_BY_ATTR: lambda: self.findAllByAttr(**kwargs),
            DbConst.INSERT: lambda: self.insert(**kwargs),
            DbConst.FIND_BY_ATTR: lambda: self.findByAttr(**kwargs),
            DbConst.UPDATE_BY_ATTR: lambda: self.updateByAttr(**kwargs),
            DbConst.FIND_BY_SQL: lambda: self.findBySql(**kwargs)
        }
        return sqlOperate[key]()

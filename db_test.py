# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-13 16:50:26
@LastEditors: iwenli
@LastEditTime: 2019-05-13 17:04:38
@Description: 测试mssql数据脚本
'''
__author__ = 'iwenli'

from db.txMssql import TxMssql
import os
from db.customConst import DbConst

db_connect_str = os.getenv("PY_BD_MSSQL_PW")
if db_connect_str is None:
    db_connect_str = ""

if __name__ == "__main__":
    db_connect_params = db_connect_str.split(';')
    txMssql = TxMssql(host=db_connect_params[0],
                      user=db_connect_params[2],
                      password=db_connect_params[3],
                      database=db_connect_params[1])
    # # 根据字段统计count, join>>AND,OR,可以不传，默认为AND
    # count = txMssql.findKeySql(DbConst.COUNT,
    #                            table="ad_seed",
    #                            params={"if_monitor": "1"})
    # print(count)
    # # 自定义sql语句统计count
    # print(
    #     txMssql.findKeySql(DbConst.COUNT_BY_SQL,
    #                        sql="select * from ad_seed",
    #                        params={"if_monitor": "1"},
    #                        join="AND"))
    # # 插入数据
    # print(
    #     txMssql.findKeySql(DbConst.INSERT,
    #                        table="persons",
    #                        data={
    #                            "id": 11,
    #                            "name": "李四",
    #                            "salesrep": "lisi"
    #                        }))
    # # 根据字段删除,不传params参数，就是删除全部
    # print(
    #     txMssql.findKeySql(DbConst.DELETE_BY_ATTR,
    #                        table="persons",
    #                        params={"id": 11}))
    # # 查找是否存在该记录,不传params参数，就是查找全部.join同上
    print(
        txMssql.findKeySql(DbConst.EXIST,
                           table="persons",
                           params={"id": 10},
                           join='AND'))
    # 根据字段查找多条记录，whole不传就查一条记录，criteria里面可以传where,group by,having,order by,limt,offset
    print(
        txMssql.findKeySql(DbConst.FIND_ALL_BY_ATTR,
                           table="ad_seed",
                           criteria={"where": "nex_name='28'"},
                           whole=True))
    # 根据字段查一条记录，和上面的查多条记录参数基本一样，少了个whole参数
    print(
        txMssql.findKeySql(DbConst.FIND_BY_ATTR,
                           table="ad_seed",
                           criteria={"where": "nex_name LIKE '%8%'"},
                           whole=True))
    # 根据字段更新数据库中的记录，join可以传AND,OR,不传默认取AND
    print(
        txMssql.findKeySql(DbConst.UPDATE_BY_ATTR,
                           table="persons",
                           data={"name": "张三 new"},
                           params={"id": '10'},
                           join='AND'))
    # 根据自定义sql语句查询记录，limit:0表示所有记录，join：AND|OR.不传取AND
    print(
        txMssql.findKeySql(DbConst.FIND_BY_SQL,
                           sql="select * from persons",
                           params={
                               "name": "'張三'",
                               "id": 3
                           },
                           join='OR',
                           limit=0))
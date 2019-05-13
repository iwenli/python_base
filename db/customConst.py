# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-13 14:13:06
@LastEditors: iwenli
@LastEditTime: 2019-05-13 14:14:16
@Description: ...
'''
__author__ = 'iwenli'


class DbConst(object):
    FIND_BY_SQL = "findBySql"  # 根据sql查找
    COUNT_BY_SQL = "countBySql"  # 自定义sql 统计影响行数
    INSERT = "insert"  # 插入
    UPDATE_BY_ATTR = "updateByAttr"  # 更新数据
    DELETE_BY_ATTR = "deleteByAttr"  # 删除数据
    FIND_BY_ATTR = "findByAttr"  # 根据条件查询一条记录
    FIND_ALL_BY_ATTR = "findAllByAttr"  # 根据条件查询多条记录
    COUNT = "count"  # 统计行
    EXIST = "exist"  # 是否存在该记录

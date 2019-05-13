# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-13 10:29:53
@LastEditors: iwenli
@LastEditTime: 2019-05-13 16:32:55
@Description: ...
'''

__author__ = 'iwenli'
from pymssql import connect
import os

keys = ['a', 'b', 'c', 'd']
_keys = [1, 2, 3, 4, 5, 6]
zip_key = zip(keys, _keys)
print(list(zip_key))
join_key = 'AND '
where = ' AND '.join(
    k + '=' + str(_k)
    for k, _k in zip_key) if join_key == 'AND' else ' OR '.join(
        k + '=' + str(_k) for k, _k in zip_key)
print(where)

__key = "AND" if join_key.upper() == 'AND' else "OR"
print(__key)

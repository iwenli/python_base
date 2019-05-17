# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-17 14:52:52
@LastEditors: iwenli
@LastEditTime: 2019-05-17 16:40:54
@Description: 高级特效
'''

# from collections import Iterable
import collections

__author__ = 'iwenli'


def slice():
    l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(l[:3])  # 前三个
    print(l[1:3])  # 第一到第三个
    print(l[-1:])  # 倒数第一个
    print(l[::2])  # 每两个取一个  1，3，5
    print(l[:])  # 复制

    print('zhangsan' [-3:])


def iter():
    print(isinstance('abc', collections.Iterable))  # str是否可迭代
    print(isinstance([1, 2, 3, 5], collections.Iterable))  # list是否可迭代
    print(isinstance((1, 2, 3, 5), collections.Iterable))  # tuple是否可迭代
    print(isinstance(12354, collections.Iterable))  # 整数是否可迭代
    print(isinstance({'a': 1, 'b': 2}, collections.Iterable))  # dict是否可迭代
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key, d[key])
    for val in d.values():
        print(val)
    for key, val in d.items():
        print(key, val)


def listcompr():
    r1 = range(1, 11)
    l0 = list(r1)
    print(l0)
    l1 = []
    for x in r1:
        l1.append(x * x)
    print(l1)
    print(l0 == l1)
    l3 = [x * x for x in r1]
    print(l3)
    l4 = [x * x for x in r1 if x % 2 == 0]
    print('生成器', l4)
    l5 = [m + n for m in 'xyz' for n in '123']
    print(l5)


def generator():
    r1 = range(1, 11)
    l1 = [x * x for x in r1]
    print('列表生成式', l1)
    g1 = (x * x for x in r1)
    print(g1)
    for n in g1:
        print(n)

    for l in triangles():
        print(l)


def triangles(lens=10):
    '''杨辉三角'''
    n = 0
    A = [0, 1, 0]
    while n < lens:
        L = [A[x] + A[x + 1] for x in range(n + 1)]
        A = [0] + L + [0]
        n += 1
        yield L


if __name__ == '__main__':
    # 切片
    # slice()

    # 迭代
    # iter()

    # 列表生成式
    # listcompr()

    # 生成器
    # generator()

    # 迭代器
    # 凡是可作用于for循环的对象都是Iterable类型；
    # 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
    # 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-17 14:10:39
@LastEditors: iwenli
@LastEditTime: 2019-05-17 14:39:25
@Description: 函数
'''
__author__ = 'iwenli'


def call_fun():
    print(abs(-1000))
    print(max(1, 299, -1, 23, 0))
    print(min(-0.0001, 1, 299, -1, 23, 0))

    print(int(12.11))
    print(hex(12391923))


def fun_param():
    # 默认参数
    p = power(10, 10)
    print(p)

    # 可变参数
    print(calc(1, 3, 5))
    l = [1, 3, 5]
    t = (1, 3, 5)
    print(calc(*l))
    print(calc(*t))

    # 关键词参数
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, **extra)


def power(x, n=2):
    result = 1
    while n > 0:
        n -= 1
        result *= x
    return result


def calc(*numbers):
    sum = 0
    for num in numbers:
        sum += power(num)
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


def move(n, a, b, c):
    '''
    汉诺塔
    '''
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


if __name__ == '__main__':
    # 调用函数
    # call_fun()

    # 函数参数
    # fun_param()

    # 递归函数
    move(3, 'A', 'B', 'C')

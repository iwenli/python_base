# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-17 13:23:19
@LastEditors: iwenli
@LastEditTime: 2019-05-17 14:09:48
@Description: ...
'''
__author__ = 'iwenli'


def data_type():
    # 整数
    print(1)
    print(-8080)
    print(0xff00)
    print(0xa5b4c3d2)

    # 浮点数
    print(1.23)
    print(-0.21)
    print(1.23e9)  # 1.23x109就是1.23e9

    # 字符串
    print('I\'m ok.')
    print('I\'m learning\nPython.')
    print('''line1
    line2
    line3''')

    # 布尔值
    print(True)
    print(1 != 2)
    print(True and False)
    print(True or False)
    print(not False)

    # 空值
    print(None)


def str_unicode():
    print(ord('A'))
    print(ord('中'))
    print(chr(66))
    print(chr(20188))
    print('\u4e2d\u6587')

    # 编码
    b1 = b'abc'
    b2 = 'abc'.encode('utf-8')
    print(b1 == b2)

    # 格式化
    print('Hello, %s' % 'world')
    print('Hi, %s, you have $%d.' % ('Michael', 1000000))
    print('growth rate: %d %%' % 7)
    print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


def list_tuple():
    classmates = ['Michael', 'Bob', 'Tracy']
    print(len(classmates))
    print(classmates[2])
    print(classmates[-1])
    classmates.append('Zhangsan')
    print(classmates.pop(0))
    print(classmates)

    # 元组
    print(())
    print((1))
    print((1, ))
    print((0, [1, 2, 3]))


def conditional():
    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
        print('00前')
    else:
        print('00后')
    # 等价于 三元运算符
    print('00前') if (birth < 2000) else print('00后')


def loop():
    names = ['龙哥', '2019', 'learn python']
    for name in names:
        print(name)
    print(''.join(names))

    l1 = list(range(12))
    sum = 0
    print(l1)
    for item in l1:
        sum += item
    print('+'.join(list(map(str, l1))), '=', sum)


def dict_set():
    names = ['zs', 'ls', 'ww']
    scores = [11, 98, 90]
    l1 = list(zip(names, scores))
    d1 = dict(zip(names, scores))
    print(l1)
    print(d1)
    for item in l1:
        print(item)
    # set 会自动过滤重复元素
    s1 = set([1, 1, 2, 2, 3, 3])
    print(s1)
    s1.add('a')
    print(s1)
    s1.add(3)
    print(s1)
    s1.remove(1)
    print(s1)


if __name__ == "__main__":
    # 数据类型
    # data_type()

    # 字符编码
    # str_unicode()

    # list和tuple
    # list_tuple()

    # 条件判断
    # conditional()

    # 循环
    # loop()

    # dict和set
    dict_set()

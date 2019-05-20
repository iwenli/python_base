# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-17 16:45:45
@LastEditors: iwenli
@LastEditTime: 2019-05-20 10:44:05
@Description: 函数式编程
'''
import functools

__author__ = 'iwenli'


def f(x):
    return x * x


def high_func():
    # map 依次将每个元素迭代到function
    print('\nmap test:')
    s = range(1, 10)
    r = map(f, list(s))
    print(list(r))

    # reduce 把结果继续和序列的下一个元素做迭代
    print('\nreduce test:')
    l1 = [x for x in range(1, 10) if x % 2 == 0]
    print(l1)
    r1 = functools.reduce(lambda a, b: a + b, l1)
    print(r1)

    # filter 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
    print('\nfilter test:')
    l2 = list(range(1, 10))
    r2 = filter(lambda m: m % 2 == 0, l2)
    print(list(r2))

    # sorted
    print('\nsorted test:')
    l3 = [36, 1, -1, -45, -4, 0, 99]
    r3 = sorted(l3)
    print(r3)
    r31 = sorted(l3, key=abs, reverse=True)
    print(r31)


def return_func():
    def lazy_sum(*args):
        def sum():
            ax = 0
            for n in args:
                ax = ax + n
            return ax

        return sum

    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)
    print(f())

    # 闭包 解决参数污染
    def count():
        fs = []
        for i in range(1, 4):

            def f():
                return i * i

            fs.append(f)
        return fs

    f1, f2, f3 = count()
    print(f1(), f2(), f3())

    def _count():
        def f(j):
            def g():
                return j * j

            return g

        fs = []
        for i in range(1, 4):
            fs.append(f(i))
        return fs

    _f1, _f2, _f3 = _count()
    print(_f1(), _f2(), _f3())


def anonymous_func():
    l1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(l1)


def decorator_func():
    def now():
        print('2019年5月20日10:23:37')

    f = now
    f()
    print(f.__name__)

    # 普通装饰器
    def log(func):
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)

        return wrapper

    @log
    def log_now():
        print('2019年5月20日10:23:37')

    log_now()

    # 带参数装饰
    def log1(text):
        def decorator(func):
            @functools.wraps(func)  # 防止函数now1.__name__ == wrapper   本应该为now1
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator

    @log1('execute')
    def now1():
        print('2019年5月20日10:31:49')

    now1()
    print(now1.__name__)


def partial_func():
    print(int('15'))
    print(int('17', base=8))
    print(int('f', base=16))

    def int2(x, base=2):
        return int(x, base)

    print(int2('00001111'))

    int16 = functools.partial(int, base=16)
    print(int16('f'))


if __name__ == '__main__':
    # 高阶函数
    # high_func()

    # 返回函数
    # return_func()

    # 匿名函数
    # anonymous_func()

    # 装饰器
    # decorator_func()

    # 偏函数
    partial_func()
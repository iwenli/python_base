# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-20 16:07:31
@LastEditors: iwenli
@LastEditTime: 2019-05-20 16:20:05
@Description: ...
'''
from turtle import *
from random import *
from math import *

__author__ = 'iwenli'


def test():
    # 设置笔刷宽度:
    width(4)

    # 前进:
    forward(200)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)


def draw_star(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


def tree1():
    # 设置色彩模式是RGB:
    colormode(255)

    lt(90)

    lv = 14
    l = 120
    s = 45

    width(lv)

    # 初始化RGB颜色:
    r = 0
    g = 0
    b = 0
    pencolor(r, g, b)

    penup()
    bk(l)
    pendown()
    fd(l)
    speed("fastest")
    draw_tree(l, 4)


def draw_tree(l, level):
    global r, g, b

    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)


def zh_tree(n, l):
    pd()  # 下笔
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
    forward(l)  # 画树枝

    if n > 0:
        b = random() * 15 + 10  # 右分支偏转角度
        c = random() * 15 + 10  # 左分支偏转角度
        d = l * (random() * 0.25 + 0.7)  # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        zh_tree(n - 1, d)
        # 左转一定角度，画左分支
        left(b + c)
        zh_tree(n - 1, d)

        # 转回来
        right(c)
    else:
        # 画叶子
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n * 0.8, n * 0.8)
        circle(3)
        left(90)

        # 添加0.3倍的飘落叶子
        if (random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random() * 40
            setheading(an)
            dis = int(800 * random() * 0.5 + 400 * random() * 0.3 +
                      200 * random() * 0.2)
            forward(dis)
            setheading(t)

            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
            circle(2)
            left(90)
            pu()

            #返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)

    pu()
    backward(l)  # 退回


def zh_tree1():
    bgcolor(0.5, 0.5, 0.5)  # 背景色
    ht()  # 隐藏turtle
    speed(0)  # 速度，1-10渐进，0最快
    # tracer(0, 0)
    pu()  # 抬笔
    backward(100)
    left(90)  # 左转90度
    pu()  # 抬笔
    backward(300)  # 后退300
    zh_tree(12, 100)  # 递归7层


if __name__ == '__main__':
    # test()
    # for x in range(0, 250, 50):
    #     draw_star(x, 0)

    # tree1()
    zh_tree1()
    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()

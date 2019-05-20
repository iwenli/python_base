# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-20 15:41:27
@LastEditors: iwenli
@LastEditTime: 2019-05-20 16:03:32
@Description: 分布式进程
'''

import random, queue
from multiprocessing.managers import BaseManager

__author__ = 'iwenli'

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 替代原来的匿名函数
def return_task_queue():
    global task_queue
    return task_queue


# 替代原来的匿名函数
def return_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口50000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 50000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('添加任务 %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('开始读取结果...')
    for i in range(10):
        r = result.get(timeout=10)
        print('结果: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master 退出.')

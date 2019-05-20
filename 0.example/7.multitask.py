# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-20 14:20:47
@LastEditors: iwenli
@LastEditTime: 2019-05-20 15:41:45
@Description: 进程 和 线程
'''
import os, time, random, queue
import multiprocessing
import threading
# from multiprocessing import Process

__author__ = 'iwenli'


def multiprocess():
    # Unix/Linux/Mac:
    # pid = os.fork()
    # if pid == 0:
    #     print('我是子进程 (%s) ，我的父线程是 %s.' %
    #           (os.getpid(), os.getppid()))
    # else:
    #     print('进程 (%s) 创建了新的进程 (%s).' % (os.getpid(), pid))

    # windows
    print('父进程: %s.' % os.getpid())
    p = multiprocessing.Process(target=run_proc, args=('test', ))
    print('子进程将启动.')
    p.start()
    p.join()
    print('子进程结束.')


def run_proc(name):
    print('运行子进程 %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('运行任务 %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务 %s 执行耗时 %0.2f 秒.' % (name, (end - start)))


def _pool():
    print('父进程： %s.' % os.getpid())
    p = multiprocessing.Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('等待所有子进程完成...')
    p.close()
    p.join()
    print('所有子进程都已完成.')


def do_queue():
    # 父进程创建Queue，并传给各个子进程：
    q = multiprocessing.Queue()
    pw = multiprocessing.Process(target=write, args=(q, ))
    pr = multiprocessing.Process(target=read, args=(q, ))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    print('执行完成')


# 写数据进程执行的代码:
def write(q):
    print('生产者进程: %s' % os.getpid())
    for value in range(1, 100):
        print('数据 %s 添加到队列...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('消费者线程: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('数据 %s 出队.' % value)


def loop_threading():
    print('线程 %s 开始运行.' % threading.current_thread().name)
    i = 0
    while i < 5:
        print('线程 %s : %s' % (threading.current_thread().name, i))
        time.sleep(1)
        i += 1
    print('线程 %s 执行完成.' % threading.current_thread().name)


def multi_threading():
    print('线程 %s 开始运行...' % threading.current_thread().name)
    t = threading.Thread(target=loop_threading, name='LoopThread')
    t.start()
    t.join()
    print('线程 %s 结束.' % threading.current_thread().name)


# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
thread_local = threading.local()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def change_it_local():
    # 获取当前线程关联的num:
    num = thread_local.num
    print('处理, %s (in %s)' % (num, threading.current_thread().name))
    change_it(num)


def run_thread(n):
    thread_local.num = n  # 绑定ThreadLocal的num
    for i in range(10000):
        lock.acquire()  # 取锁
        try:
            # change_it(n)
            change_it_local()
        finally:
            lock.release()  # 执行完成释放锁


def multi_thread_lock():
    t1 = threading.Thread(target=run_thread, args=(5, ), name='A')
    t2 = threading.Thread(target=run_thread, args=(8, ), name='B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


def multi_cpu_loop():
    x = 0
    while True:
        x = x ^ 1


def multi_cpu():
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=multi_cpu_loop)
    t.start()
 

if __name__ == '__main__':
    # 多进程
    # multiprocess()

    # 进程池
    # _pool()

    # 子进程
    # import subprocess
    # r = subprocess.call(['nslookup', 'www.txooo.com'])

    # 进程通信
    # do_queue()

    # 多线程
    # multi_threading()

    # 线程锁
    # multi_thread_lock()

    # 多核cpu
    # multi_cpu() 

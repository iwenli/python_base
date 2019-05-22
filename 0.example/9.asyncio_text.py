# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-16 13:19:38
@LastEditors: iwenli
@LastEditTime: 2019-05-21 10:38:48
@Description: ...
'''
import asyncio
from aiohttp import web

__author__ = 'iwenli'


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print('return')
            return
        print('[消费者] 消费数据 %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者] 生产数据 %s...' % n)
        r = c.send(n)
        print('[生产者] 消费者返回: %s' % r)
    c.close()


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


async def wgetasync(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


if __name__ == "__main__":
    # 协程
    # produce(consumer())

    # # asyncio
    # loop = asyncio.get_event_loop()
    # tasks = [
    #     # wget(host)
    #     wgetasync(host)
    #     for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
    # ]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()

    # aiohttp
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
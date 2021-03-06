# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-21 15:10:22
@LastEditors: iwenli
@LastEditTime: 2019-05-22 17:32:42
@Description: 日志
'''
__author__ = 'iwenli'

import os
import time
import logging
import inspect
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter

dir = os.path.dirname(__file__)
dir = os.path.join(dir, '_log')
if not os.path.isdir(dir):
    os.mkdir(dir)
dir_time = time.strftime('%Y-%m-%d', time.localtime())

handlers = {
    logging.NOTSET: os.path.join(dir, 'notset_%s.log' % dir_time),
    logging.DEBUG: os.path.join(dir, 'debug_%s.log' % dir_time),
    logging.INFO: os.path.join(dir, 'info_%s.log' % dir_time),
    logging.WARNING: os.path.join(dir, 'warning_%s.log' % dir_time),
    logging.ERROR: os.path.join(dir, 'error_%s.log' % dir_time),
    logging.CRITICAL: os.path.join(dir, 'critical_%s.log' % dir_time),
}


def createHandlers():

    logLevels = handlers.keys()

    for level in logLevels:
        path = os.path.abspath(handlers[level])
        handlers[level] = RotatingFileHandler(path,
                                              maxBytes=10000,
                                              backupCount=2,
                                              encoding='utf-8')


# 加载模块时创建全局变量

createHandlers()


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class TxLog(object):
    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}
        logLevels = handlers.keys()

        for level in logLevels:
            logger = logging.getLogger(str(level))

            formatter = ColoredFormatter(
                # "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
            )
            stream = logging.StreamHandler()
            stream.setFormatter(formatter)
            logger.addHandler(stream)
            # 如果不指定level，获得的handler似乎是同一个handler?

            logger.addHandler(handlers[level])

            logger.setLevel(level)

            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack(
        )[2]
        '''日志格式：[时间] [类型] [记录代码] 信息'''

        return "[%s] [%s] [%s - %s - %s] %s" % (
            self.printfNow(), level, filename, lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)

        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)

        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)

        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)

        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)

        self.__loggers[logging.CRITICAL].critical(message)


# if __name__ == "__main__":
# log = TxLog()
# log.debug("A quirky message only developers care about")
# log.info("Curious users might want to know this")
# log.warning("Something is wrong and any user should be informed")
# log.error("Serious stuff, this is red for a reason")
# log.critical("OH NO everything is on fire")

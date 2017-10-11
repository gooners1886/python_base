#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/18 12:13
# @Author  : Andy
# @Site    : 
# @File    : main3.py
# @Software: PyCharm Community Edition


import logging
import sys
import os
import subprocess


# 可以捕捉 assert 和 数组溢出。 解决print重定向问题。
class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

stdout_old = sys.stdout
stderr_old = sys.stderr

g_str_log_file = "out.log"
fp = open(g_str_log_file, 'w')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    stream=fp
)

stdout_logger = logging.getLogger('STDOUT')
s1 = StreamToLogger(stdout_logger, logging.INFO)
sys.stdout = s1

stderr_logger = logging.getLogger('STDERR')
s2 = StreamToLogger(stderr_logger, logging.ERROR)
sys.stderr = s2

str_call_cmd = "python ./child1.py"


print ("call child 1 begin ...")

# child = subprocess.Popen(str_call_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# child = subprocess.Popen(str_call_cmd, shell=True, stdout=f, stderr=f)
# child = subprocess.Popen(str_call_cmd, shell=True)
a = subprocess.call(str_call_cmd, shell=True, stdout=fp, stderr=fp)

# print ("ret val = {}".format(a))
print ("call child 1 end.")

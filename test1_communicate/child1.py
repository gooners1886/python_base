#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/18 12:14
# @Author  : Andy
# @Site    :
# @File    : fun3.py
# @Software: PyCharm Community Edition

import subprocess
import sys
if __name__ == '__main__':

    print ("in child 1")
    str_call_cmd = "python child_child2.py"
    p_child = subprocess.Popen(str_call_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    (stdoutput, erroutput) = p_child.communicate()
    str_stdoutput = bytes.decode(stdoutput)
    for s in str_stdoutput.split('\r\n'):
        if s != '\r\n':
            print("===================")
            print(s)
            print("===================")

    str_stdoutput = bytes.decode(erroutput)
    for s in str_stdoutput.split('\r\n'):
        if s != '\r\n':
            print("===================")
            print(s)
            print("===================")

    p_child.wait()
    print ("in child call child_child 2 end")
    # assert 0, "human error in fun 3."

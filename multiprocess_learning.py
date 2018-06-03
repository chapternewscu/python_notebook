# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 13:20
# @Author  : jacobjzhang
# @Email   : jacobjzhang@tencent.com
# @File    : multiprocess_learning.py
# @Software: PyCharm

'''
learning_from :
    http://www.cnblogs.com/lianzhilei/p/7009826.html
知识点 :
    1. 多进程运行原理
    2. 多进程之间通信， multiprocess提供了queue和pipe等机制
    3. 多进程之间共享内存， Manager()是一个不错的选择
    4. 同时运行的进程数小于等于cpu_count(Pool特性，其他语言或实现方式可能不同)
'''

from multiprocessing import Pool
from multiprocessing import Queue
from multiprocessing import cpu_count
from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing import Value
from multiprocessing import Array
import os
import time
import random


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end-start))

def Bar(arg):
    print  '-->exec done:', arg, os.getpid()

def write(q):
    print ' Process to write：%s ' % (os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        print 'Put %s to queue ... ' % value
        q.put(value)
        time.sleep(random.random())

def read(q):
    print 'Process to read: %s ' % os.getpid()
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

def f(n, a):
    n.value = 3.1415
    for i in range(len(a)):
        a[i] = -a[i]

def manage_f(d, l):
    d[1] = '1'
    time.sleep(random.random())
    d['2'] = 2
    d[0.25] = None
    l.reverse()

def manage_f2(d,l):
    d['2'] = 20
    time.sleep(random.random())
    l[2] = 100

if __name__ == "__main__":
    print "Parent processs %s. " % os.getpid()
    p = Pool(cpu_count())

    for i in range(9):
        p.apply_async(long_time_task, args=(i,))

    print 'Waiting for all subprocesses done..'
    p.close()
    p.join()
    print 'All subprocesses done.'

    print '---' * 20

    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

    print '---' * 20
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print num.value
    print arr[:]

    print '--' * 20

    manager = Manager()
    d = manager.dict()
    ll = manager.list(range(10))

    p = Process(target=manage_f, args=(d, ll))
    p2 = Process(target=manage_f2, args=(d, ll))
    p.start()
    p2.start()
    p.join()

    print d
    print ll

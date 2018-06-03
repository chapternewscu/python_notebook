# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 11:20
# @Author  : jacobjzhang
# @Email   : jacobjzhang@tencent.com
# @File    : sort_learning.py
# @Software: PyCharm

'''
learnin_from :
    http://www.cnblogs.com/lianzhilei/p/6932894.html
知识点 :
    python 内置了两种排序函数，obj.sort 和sorted
    obj.sort 是原地排序
    sorted是返回排序后的新结果。

    排序有三个参数，分别是：
    key:比较排序obj的什么属性
    cmp:比较函数
    reverse:排序结果是否翻转。
    一般只用指定key
'''


# 用长度进行排序，从大到小进行排序
li = ['x11', 'abc323', 'e26', '112ddd', 'fstgd2']
li.sort(key=len, reverse=True)
new_li = sorted(li, key=lambda x: len(x), reverse=True)
print li
print new_li

# 元素的最后一个字符进行排序
li.sort(key=lambda x: x[-1])
new_li = sorted(li, key=lambda x: x[-1])
print li
print new_li

# 列表中元素为元祖进行排序
li = zip(range(10), range(10)[::-1])
print (li, type(li))
li = list(li)
li.append((0, 8))

li.sort(key=lambda x: x[-1])
new_li = sorted(li, key=lambda x: x[-1])
print li
print new_li

li.sort()
print li

# 按照value大到小输出dict中的key_value值
dic = {'z': 1,
       'y': 4,
       'x': 2,
       'g': 3,
       'sg': 3}

tmp_sort_dic = sorted(dic.iteritems(), key=lambda x: x[1])
print tmp_sort_dic

# 排序后转化为字典, 有时候业务需求，按照value从头到尾进行索引
from collections import OrderedDict
dic = OrderedDict(tmp_sort_dic)
print dic
print dic['z']


# 小写在大写前面，字母在数字前面， 奇数在偶数前面
s = "Sorting1234"


def sort_str(x):
    # print x, type(x)
    if x.isdigit():
        if int(x) % 2 == 0:
            return (4, x)
        else:
            return (3, x)
    elif x.islower():
        return (1, x)
    elif x.isupper():
        return (2, x)


li = sorted(s, key=lambda x: sort_str(x))
print li






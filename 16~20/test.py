#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
def takeFirst(elem):
    return elem[0]

# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeFirst)

print(random)

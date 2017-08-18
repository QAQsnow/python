# -*- coding: utf-8 -*-

#迭代器iterator

#判断是否是迭代器 使用isinstance()


from collections import Iterator

isinstance(x,Iterator)

#list dict str都是生成器iterable

#可以通过iter()函数变成迭代器iterator

iter([])

isinstance(iter([]),Iterator)

isinstance(iter({}),Iterator)
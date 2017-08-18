# -*- coding: utf-8 -*-

#列表生成式

#让原列表每一个数都乘以某一数 得出新列表

[x*x for x in range(1,11)]

#让列表每一个数都乘以某一个数 然后满足一定条件 得出新列表

[x*x for x in range(1,11)if x%2==0]

#可以使用两层循环

[m+n for m in 'abc' for n in 'xyz']

#运用列表生成式 列出当前目录下的所有文件和目录名

import os

[d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C' }

for k,v in d.items():

	print(k,v)
	
	
#用内置函数isinstance 判断一个变量是不是字符串

x='abc'
y=123

isinstance(x,str)
isinstance(y,str)

#把list大写字母全部变成小写的

L = ['Hello', 'World', 'IBM', 'Apple']

[s.lower() for s in l]
#py中只要是可迭代的对象，无论有无下标，都可以迭代
d={'name':'snow','age':26,'like':'art'}
for key in d:
	print(key);
	
#遍历dict里面的值  遍历出来的值不一定按顺序来排列

for value in d.values():
	print(key)
	
#遍历dict里面的索引和值

for k,v in d.items():
	print(k,v)
	
#判断是否可以迭代 通过collections模块的Itrable类型判断

from collections import Iterable

isinstance('abc',Itrable)

isinstance(d,Iterable)

isinstance(123,Iterable)

#对dict类型的实现下标循环 用内置函数enumerate()

l=[65847,124,2154]

for i,v in enumerate(l):
	print(i,v)
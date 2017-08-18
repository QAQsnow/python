# -*- coding: utf-8 -*-


l=[1,2,3,4,5,6,7,8,9]

#把函数x平方作用在l上可以用map()函数

def f(x):
	return x*x;

map(f,l)

#函数reduce是把一个序列求和

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	
print(list(map(char2num,'13579')));


#利用输入['adam', 'LISA', 'barT'] 输出 ['Adam', 'Lisa', 'Bart']

arr=['adam', 'LISA', 'barT']

def toFirstUpper(list):
	var a=list.lower()[0].upper()
	
for value in map(toFirstUpper,arr):
	print(value)

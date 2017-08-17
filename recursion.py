# -*- coding: utf-8 -*-

#递归函数

	recursion(n):
		if n==1:
			return 1
		else 
			return n*recursion(n-1)
#函数调用是通过栈数据结构实现的，进入一个函数调用，就会增加一层栈帧，达到一定数量就会发生栈溢出，
#可以通过尾递归来优化，循环是一种特殊的尾递归
#尾递归是指返回函数本身自身，并不包含任何表达式
	fact(n):
		return fact_iter(n,1)
	#尾递归函数	
	fact_iter(n,num):
		if n==1:
			return num
		else
			return fact_iter(n-1,n*num)
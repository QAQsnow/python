# -*- coding: utf-8 -*-

#打印裴波拉契数列

def lib(max):
	n,a,b=0,0,1
	while n<max:
		#print(a);
		print(b)
		a,b=b,a+b
		n=n+1
		#print(b);
	return 'done'
print(lib(6));	

for x in lib(6):
	print(x);
	

g = lib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
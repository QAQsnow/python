# -*- coding: utf-8 -*-

#函数参数
 #必要参数
 fn(a,b):
	print(a,b);
 #默认参数
 fn(a,b,c=56):
	print(a,b,c)
 #可变参数*agru(参数不确定) 会在函数内部自动生成一个tuple
 fn(a,b,c=56,*argu):
	print(a,b,c,agru)
 #关键字参数 在函数内会自动组装为一个dict
 fn(a,b,c=56,*agru,**kw):
	print(a,b,c,agru,kw)
 #命名关键字参数，参数前面要跟一个*，如果命名关键字参数签名含有可变参数 就不需要*
 fn(a,b,*,city,job):
	print(a,b,city,job)
 fn(a,b,*agru,city,job):
	print(a,b,argu,city,job)
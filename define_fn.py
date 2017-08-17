def abs_num(x):
	if x>0:
		return x
	else: 
		return -x
		
print(abs_num(-5))


def calc(*number):
	sum=0
	for num in number:
		sum=sum+num
	return sum
print(calc(*[1,2,3,4,5]));
print(calc(1,2,3,4,5))
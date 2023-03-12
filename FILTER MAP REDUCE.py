#Program to perform MAP()
def square(x):
	return x*x

original_lst1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
print( " The INITIAL List is : ",original_lst1)
print( " The SQUARED List is :", list(map(square,original_lst1)))

#Program to perform FILTER()
def positive(x):
	if x>=0:
		return x

original_lst2 = [ -34, 90, -23, 56, -4, 26, -6 ]
print( " The INITIAL List is : ",original_lst2)
print( " The POSITIVE List is :", list(filter(positive,original_lst2)))

#Program to perform REDUCE()
import functools
def largest_element(x,y):
	if x>y:
		return x
	else:
		return y
		
original_lst3 = original_lst1 + original_lst2
print( " The INITIAL List is : ",original_lst3)
print( " The LARGEST element in List is :",functools.reduce(largest_element,original_lst3))
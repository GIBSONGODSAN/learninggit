#Program to execute EXPONENTIAL of two numbers Recursively
def exponential(x,y):
	if y==0:
		return 1
	else:
		return x*exponential(x,y-1)
		
#Input the numbers from user and print Exponential
n, m = list ( map ( int, input( " Enter two numbers to find EXPONENTIAL :").split()))
print( " Exponential Result is =", exponential(n,m))
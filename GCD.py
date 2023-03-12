#Program to find GCD of two numbers
def GCD(x,y):
	rem = x % y
	if ( rem == 0):
		return y
	else:
		return GCD( y, rem )

#Input the numbers from user and print GCD
n, m = list ( map ( int, input( " Enter two numbers to find GCD :").split()))
print( " The GCD of ",n,"and", m,"is =", GCD(n,m))
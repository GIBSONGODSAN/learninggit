# Program to calculate FACTORIAL using Recursion function
def factorial(n):
	if ( n == 1 or n == 0):
		return 1
	else:
		return n*factorial( n-1 )
		
#Input the number from the user
num = int ( input ( " Enter the Number :" ) )
print( "The Factorial of ",num, "is :",factorial(num))
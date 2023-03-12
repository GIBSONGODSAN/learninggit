#Program to find Square Root using NEWTON METHOD 
def newtonSqrt(n):
 approx = 0.5 * n
 better = 0.5 * (approx + n/approx)
 while better != approx:
 	approx = better
 	better = 0.5 * (approx + n/approx)
 return approx

#Main program
num = int (input ("Enter :"))
print('The square root is' ,newtonSqrt(num)) 
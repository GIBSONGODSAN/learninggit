#Program to execute TOWER OF HANOI
#Function code to recursive method of HANOI
def hanoi(n,a,b,c):
	if n>0:
		hanoi(n-1,a,c,b)
		if a:
			c.append(a.pop())
		hanoi(n-1,b,a,c)
		
#Intializing the elements
a=[1,2,3,4]
b=[ ]
c=[ ]
print("Before :",a,b,c)
hanoi(len(a),a,b,c)   #calling the function
print("After :",a,b,c)

"""
OUTPUT

[ ]  [ ]  [ 1, 2, 3, 4 ]
funished
"""
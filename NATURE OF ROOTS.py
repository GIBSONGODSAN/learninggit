#Program to find the NATURE OF ROOTS of Quadratic equation

a, b, c = list ( map ( int, input(" Enter the Values of a, b, c :").split( ) ) )

D = ( b*b ) - ( 4*a*c )
deno = 2*a

#Condition for nature of roots
if ( D > 0):
	print( " REAL ROOTS ")
	root1 = ( -b + ( D**0.5))/deno
	root2 = ( -b  - ( D**0.5))/deno
	print( " Root1 =",root1, "\n Root2 =", root2)
elif (D==0):
	print( " EQUAL ROOTS ")
	root1 = ( -b / deno)
	print( " Root1 and Root2 =", root1)
else:
	print( " IMAGINARY ROOTS ")
	
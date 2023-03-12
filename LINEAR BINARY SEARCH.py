#Program to SEARCH Element in a list

#Common code to input array elements from user
n = int ( input ( " Enter the number of elements in the array :" ) )
i = 0
lst= [ ]
for i in range( n ):
	num = int ( input ( " Enter the element :" ) )
	lst.append( num )
print( " The Initial ARRAY is :", lst)
	
#LINEAR SEARCH
val = int ( input ( " Enter the Element to be searched :" ) )
print( " By LINEAR SEARCH " )
i = 0
found = 0
while ( i<n ):
	if ( val == lst[ i ] ):
		print ( " Number found at position :", i)
		found = 1
		break
	i = i + 1
if ( found == 0 ) :
	print( " Number is not found " )
	
#BINARY SEARCH
val = int ( input ( " Enter the Element to be searched :" ) )
print( " By BINARY SEARCH " )
found = 0
beg = 0
end = n - 1
while ( beg <= end ):
	mid = int ((beg+end )/2 )
	if ( lst[mid] == val ):
		print ( " Number found at position :", mid)
		found = 1
		break
	elif ( lst[ mid ]>val ):
		end = mid-1
	elif ( lst[ mid ]<val ):
		beg = mid+1
if ( found == 0):
	print( " Number is not found")
	
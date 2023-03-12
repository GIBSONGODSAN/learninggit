#Program to CICULATE elements in a list

lst_n = [ ]  #Empty list
n = int ( input ( " Enter the Total number of elements in the list : ") )

#To append the element in the list
for i in range(1,n+1):
	element = int ( input ( "Enter the element :") )
	lst_n.append(element)
	
#To circulate
for i in range(0,n):
	print( lst_n[ i: ] + lst_n[ :i ])
	
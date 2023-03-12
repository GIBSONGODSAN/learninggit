#Program for SELECTION SORT
def selection_Sort( A ):
	for i in range(len(A)-1):
		pos = i
		for j in range( i+1, len(A)):
			if ( A[ pos ] > A[ j ] ):
				pos = j
		A [ i ], A [ pos ] = A[ pos ], A[ i ]
	
# Program for Bubble sort in Python
def bubble_Sort(B):
    for i in range(len(B)):
    	for j in range(0, len(B) - i - 1):
    		if B[ j] > B[ j + 1]:
    			B[ j ], B[ j+1] = B[ j+1 ], B[ j ]

# Program for Insertion sort in Python
def insertion_Sort(D):
        for i in range(1, len(D)):
        	key = D[ i ]
        	j = i - 1
        	while j >= 0 and key < D[j]:
        	   D[j + 1] = D[j]
        	   j = j - 1
        	D[j + 1] = key
        	
#Program for Quick sort in Python
def partition( C, low, high):
    pivot = C[high]
    i = low -1
    for j in range(low, high):
	     if C[j] <= pivot:
	     	i = i + 1
	     	C[i], C[j] = C[j], C[i]
    C[i + 1], C[high] =  C[high], C[i + 1]
    return i + 1
def quick_Sort(C, low, high):
	if low < high:
		pi = partition( C, low, high)
		quick_Sort( C, low, pi - 1)
		quick_Sort( C, pi + 1, high)
		
#Program for MergeSort in Python
def merge_Sort(E):
        if len(E) > 1:
            r = len(E)//2
            L = E[:r]
            M = E[r:]
            merge_Sort(L)
            merge_Sort(M)
            i = j = k = 0
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                	E[k] = L[i]
                	i += 1
                else:
                	E[k] = M[j]
                	j += 1
                k += 1
            while i < len(L):
            	E[k] = L[i]
            	i += 1
            	k += 1
            while j < len(M):
            	E[k] = M[j]
            	j += 1
            	k += 1

A = [ 8, 6, 8, 2, 3, 9, 4, 1, 7, 5 ]
B = [ 7, 3, 0, 5, 7, 7, 5, 6, 1, 4 ]
C = [ 9, 0, 9, 4, 3, 9, 5, 5, 7, 0 ]
D = [ 9, 8, 4, 0, 2, 7, 4, 3, 0, 5 ]
E = [ 9, 3, 4, 2, 1, 3, 3, 6, 7, 8 ]
selection_Sort(A)
bubble_Sort(B)
insertion_Sort(C)
quick_Sort(D, 0, len(D)-1)
merge_Sort(E)
print ( " The list after SELECTION SORT is :\n", A )
print ( " The list after BUBBLE SORT is :\n", B )
print ( " The list after INSERTION SORT is :\n", C )
print ( " The list after QUICK SORT is :\n", D )
print ( " The list after MERGE SORT is :\n", E )
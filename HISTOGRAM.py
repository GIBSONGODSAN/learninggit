#Program to display HISTOGRAM AND INVERT HISTOGRAM

#Function for HISTOGRAM
def histogram(s):
	d = dict()
	for c in s:
		if c in d:
			d[c] = d[c] + 1
		else:
			d[c] = 1
	return(d)
		
#Function for INVERSE HISTOGRAM
def invert_histogram(d):
     inverse = dict()
     for key in d:
     	val = d[key]
     	if val not in inverse:
     		inverse[val] = [key]
     	else:
     		inverse[val].append(key)
     return inverse


#Main program

str = input("Enter a string:")
print("Histogram\n",histogram(str))

print("Inverted histogram \n",invert_histogram(histogram(str)))
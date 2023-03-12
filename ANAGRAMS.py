#Program to select ANAGRAMS
def anagram(lst):
	count = 0
	j=1
	for i in lst:
		if sorted(i) == sorted(lst[j]):
			print(lst[j])
			count+=1
			lst.remove(lst[j])
			j+=1
	return count

#Main program
n = int(input("Enter the number of items :"))
lst = [ ]
for i in range(0,n):
	ele = input("Enter the element :")
	lst.append(ele)
print("No. of anagrams = ",anagram(lst))


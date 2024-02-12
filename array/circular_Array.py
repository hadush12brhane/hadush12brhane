# Python3 program to demonstrate use of 
# circular array using extra memory space

def prints(a, n, ind):
	# Create an auxiliary array of twice size.
	b = [None]*2*n
	i = 0
	# Copy a[] to b[] two times
	while i < n:
		b[i] = b[n + i] = a[i]
		i = i + 1
	i = ind

	# print from ind-th index to (n+i)th index.
	while i < n + ind :
		print(b[i], end = " ");
		i = i + 1

# Driver Code
a = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(a);
prints(a, n, 4);

#This code is contributed by rishabh_jain

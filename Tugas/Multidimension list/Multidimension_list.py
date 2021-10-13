# Accessing a multidimensional list:
# Approach 1:

# Python program to demonstrate printing 
# of complete multidimensional list 
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
print(a) 

# Approach 2: Accessing with the help of loop.

# Python program to demonstrate printing 
# of complete multidimensional list row 
# by row. 
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
for record in a: 
	print(record) 

# Approach 3: Accessing using square brackets.

# Python program to demonstrate that we 
# can access multidimensional list using 
# square brackets 
a = [ [2, 4, 6, 8 ], 
	[ 1, 3, 5, 7 ], 
	[ 8, 6, 4, 2 ], 
	[ 7, 5, 3, 1 ] ] 
		
for i in range(len(a)) : 
	for j in range(len(a[i])) : 
		print(a[i][j], end=" ") 
	print()	 

# Creating a multidimensional list with all zeros:

# Python program to create a m x n matrix 
# with all 0s 
m = 4
n = 5

a = [[0 for x in range(n)] for x in range(m)] 
print(a) 

# Methods on Multidimensional lists

# Adding a sublist 
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a.append([5, 10, 15, 20, 25]) 
print(a) 

# Extending a sublist 
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a[0].extend([12, 14, 16, 18]) 
print(a) 

# Reversing a sublist 
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a[2].reverse() 
print(a) 
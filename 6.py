"""
https://www.deep-ml.com/problems/6
Write a Python function that calculates the eigenvalues of a 2x2 matrix. 
The function should return a list containing the eigenvalues, sort values from highest to lowest.
Example:
Input:
matrix = [[2, 1], [1, 2]]
Output:
[3.0, 1.0]
Reasoning:
The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which for a 2x2 matrix is 
λ^2 −trace(A)λ+det(A)=0, where λ are the eigenvalues.
"""

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	def det(a):
    	return (a[0][0]*a[1][1]) - (a[0][1]*a[1][0]) 
	def trace(a):
		return a[0][0]+a[1][1]

	a = 1
	b = -trace(matrix)
	c = det(matrix)

	square_root = (b**2 - (4*a*c))**0.5

	pos = (-b + square_root)/(2*a)
	neg = (-b - square_root)/(2*a)

	return sorted([pos, neg], reverse=True)

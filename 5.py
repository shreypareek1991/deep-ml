"""
https://www.deep-ml.com/problems/5
Write a Python function that multiplies a matrix by a scalar and returns the result.
Example:
Input:
matrix = [[1, 2], [3, 4]], scalar = 2
Output:
[[2, 4], [6, 8]]
Reasoning:
Each element of the matrix is multiplied by the scalar.
"""

## shrey 

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	return [[element * scalar for element in row] for row in matrix]

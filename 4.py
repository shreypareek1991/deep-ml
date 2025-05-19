"""
Calculate Mean by Row or Column

Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
Example:
Input:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'
Output:
[4.0, 5.0, 6.0]
Reasoning:
Calculating the mean of each column results in [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3].
"""

## shrey

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "column":
        matrix = list(zip(*matrix))
    
  return [sum(row)/len(row) for row in matrix]

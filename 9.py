"""
https://www.deep-ml.com/problems/9
multiply two matrices together (return -1 if shapes of matrix dont aline), i.e. 
C
=
A
⋅
B
C=A⋅B
Example:
Input:
A = [[1,2],[2,4]], B = [[2,1],[3,4]]
Output:
[[ 8,  9],[16, 18]]
Reasoning:
1*2 + 2*3 = 8; 2*2 + 3*4 = 16; 1*1 + 2*4 = 9; 2*1 + 4*4 = 18
Example 2: input: A = [[1,2], [2,4]], B = [[2,1], [3,4], [4,5]] output: -1 reasoning: the length of the rows of A does not equal the column length of B
"""

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    rows_a = len(a)
    cols_a = len(a[0])

    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        return -1
      
    product = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_a): # or rows_b
            for k in range(cols_b):
                product[i][k] += a[i][j] * b[j][k]

	return product

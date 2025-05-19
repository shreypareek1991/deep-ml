"""
Task: Compute the Column Space of a Matrix
In this task, you are required to implement a function matrix_image(A) that calculates the column space of a given matrix A. 
The column space, also known as the image or span, consists of all linear combinations of the columns of A. 
To find this, you'll use concepts from linear algebra, focusing on identifying independent columns that span the matrix's image. 
Your task: Implement the function matrix_image(A) to return the basis vectors that span the column space of A. 
These vectors should be extracted from the original matrix and correspond to the independent columns.

Input:
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix_image(matrix))

Output:
# [[1, 2],
#  [4, 5],
#  [7, 8]]

"""

import numpy as np

def matrix_image(A):
    matrix = A.copy()
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem != 0:
                matrix[i,:] = row/elem
                for k, _ in enumerate(matrix):
                    if i != k:
                        matrix[k,:] -= matrix[k,j] * matrix[i,:]         
                break

    non_zero_matrix = np.array([r for r in matrix if not np.all(r==0)])
    pivot_cols = [np.nonzero(non_zero_row)[0][0] for non_zero_row in non_zero_matrix]
		
    return (A[:,pivot_cols])


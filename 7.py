"""
https://www.deep-ml.com/problems/7
Write a Python function that transforms a given matrix A using the operation T−1AS
where T and S are invertible matrices. 
The function should first validate if the matrices T and S are invertible, and then perform the transformation. In cases where there is no solution return -1
Example:
Input:
A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]
Output:
[[0.5,1.5],[1.5,3.5]]
Reasoning:
The matrices T and S are used to transform matrix A by computing 
T−1AS
"""

import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

    T = np.array(T)
    A = np.array(A)
    S = np.array(S)

    is_square = (T.shape[0]==T.shape[1]) and (S.shape[0]==S.shape[1]) 
    if not is_square:
        return -1

    is_invertible = (np.linalg.det(T)!=0) and  (np.linalg.det(S)!=0)
    if not is_invertible:
        return -1

    T_inv = np.linalg.inv(T)
    AS = np.dot(A,S)


    transformed_matrix = np.dot(T_inv, AS)

	return transformed_matrix.tolist()

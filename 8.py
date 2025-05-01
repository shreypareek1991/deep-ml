"""
https://www.deep-ml.com/problems/8
Write a Python function that calculates the inverse of a 2x2 matrix. Return 'None' if the matrix is not invertible.
Example:
Input:
matrix = [[4, 7], [2, 6]]
Output:
[[0.6, -0.7], [-0.2, 0.4]]
Reasoning:
The inverse of a 2x2 matrix [a, b], [c, d] is given by (1/(ad-bc)) * [d, -b], [-c, a], provided ad-bc is not zero.
"""

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:

    def is_square(a):
        return (len(a) == len(a[0]))

    def det(a):
        if not is_square(matrix):
            return 0
        return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

    def adj(a):
        return [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]]

    def inv(a):
        adjoint = adj(a)
        determinant = det(a)
        
        for i in range(len(adjoint)):
            for j in range(len(adjoint[0])):
                adjoint[i][j] /= determinant

        return adjoint
        
    if not det(matrix):
        return None

	return inv(matrix)

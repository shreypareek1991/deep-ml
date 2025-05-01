"""
https://www.deep-ml.com/problems/10
Write a Python function to calculate the covariance matrix for a given set of vectors. 
The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix as a list of lists. 
Additionally, provide test cases to verify the correctness of your implementation.
Example:
Input:
[[1, 2, 3], [4, 5, 6]]
Output:
[[1.0, 1.0], [1.0, 1.0]]
Reasoning:
The covariance between the two features is calculated based on their deviations from the mean. 
For the given vectors, both covariances are 1.0, resulting in a symmetric covariance matrix.
"""

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    def get_row_means(a):
        means = []
        for row in a:
            means.append(sum(row)/len(row))
        return means
        
    def covar(row1, row1_mean, row2, row2_mean):
        _sum = 0
        for i in range(len(row1)):
            _sum += (row1[i]-row1_mean)*((row2[i]-row2_mean))
        return _sum/(len(row1)-1)

    row_means = get_row_means(vectors)

    cov_matrix = [["" for _ in range(len(vectors))] for _ in range(len(vectors))]

    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if i != j and cov_matrix[j][i] != "":
                cov_matrix[i][j] = cov_matrix[j][i]
            else:
                cov_matrix[i][j] = covar(vectors[i], row_means[i], 
                                    vectors[j], row_means[j])

    return cov_matrix

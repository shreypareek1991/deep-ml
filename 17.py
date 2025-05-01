"""
https://www.deep-ml.com/problems/17

Your task is to write a Python function that implements the k-Means clustering algorithm. This function should take specific inputs and produce a list of final centroids. 
k-Means clustering is a method used to partition n points into k clusters. The goal is to group similar points together and represent each group by its center (called the centroid).
Function Inputs:
points: A list of points, where each point is a tuple of coordinates (e.g., (x, y) for 2D points)
k: An integer representing the number of clusters to form
initial_centroids: A list of initial centroid points, each a tuple of coordinates
max_iterations: An integer representing the maximum number of iterations to perform
Function Output:
A list of the final centroids of the clusters, where each centroid is rounded to the nearest fourth decimal.
Example:
Input:
points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2, initial_centroids = [(1, 1), (10, 1)], max_iterations = 10
Output:
[(1, 2), (10, 2)]
Reasoning:
Given the initial centroids and a maximum of 10 iterations, the points are clustered around these points, and the centroids are updated to the mean of the assigned points, resulting in the final centroids which approximate the means of the two clusters. The exact number of iterations needed may vary, but the process will stop after 10 iterations at most.

"""

import numpy as np
def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
	# Your code here

    def dist(p1, p2):
        sq_dist = 0
        for i in range(len(p1)):
            sq_dist += (p1[i]-p2[i])**2
    
        return np.sqrt(sq_dist)
    
    centroids = initial_centroids
    
    for _ in range(max_iterations):
        clusters = {cluster_id:[] for cluster_id in range(k)}
        for point_num, p1 in enumerate(points):
            min_dist = np.inf
            closest_centroid = None
            for centroid_number, p2 in enumerate(centroids):
                distance2centroid = dist(p1, p2)
                if distance2centroid < min_dist:
                    min_dist = distance2centroid
                    closest_centroid = centroid_number
            clusters[closest_centroid].append(p1)
        
        centroids = [np.mean(np.array(cluster_points), axis=0) for _, cluster_points in clusters.items()]


	return centroids

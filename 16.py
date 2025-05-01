"""
https://www.deep-ml.com/problems/16

Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. 
The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. 
It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.
Example:
Input:
data = np.array([[1, 2], [3, 4], [5, 6]])
Output:
([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
Reasoning:
Standardization rescales the feature to have a mean of 0 and a standard deviation of 1. 
Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature value maps to 0 and the maximum to 1.

"""


import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	
    def standar_scaler(data):
        col_mean = np.mean(data, axis=0)
        col_std = np.std(data, axis=0)
    
        scaled_data = (data-col_mean) / col_std
    
        return np.round(scaled_data, 4)
    
    def min_max_scaler(data):
        col_min = np.min(data, axis=0)
        col_max = np.max(data, axis=0)
    
        scaled_data = (data-col_min) / (col_max - col_min)
    
        return np.round(scaled_data, 4)

	return standar_scaler(data), min_max_scaler(data)

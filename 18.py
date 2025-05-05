"""
https://www.deep-ml.com/problems/18
Implement a function to generate train and test splits for K-Fold Cross-Validation. 
Your task is to divide the dataset into k folds and return a list of train-test indices for each fold.
Example:
Input:
k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9]), np.array([0,1,2,3,4,5,6,7,8,9]), k=5, shuffle=False)
Output:
[([2, 3, 4, 5, 6, 7, 8, 9], [0, 1]), 
([0, 1, 4, 5, 6, 7, 8, 9], [2, 3]), 
([0, 1, 2, 3, 6, 7, 8, 9], [4, 5]), 
([0, 1, 2, 3, 4, 5, 8, 9], [6, 7]), 
([0, 1, 2, 3, 4, 5, 6, 7], [8, 9])]
Reasoning:
The function splits the dataset into 5 folds without shuffling and returns train-test splits for each iteration.
"""
import numpy as np
import random

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    # Your code here
    indices = [i for i in range(len(X))]
    if shuffle:
        np.random.seed(random_seed)
        np.random.shuffle(indices)

    fold_size = len(X)//k

    fold_num = 0
    splits = {i:[] for i in range(k)}
    for start_index in range(0, len(X), fold_size):
        splits[fold_num] = indices[start_index:start_index+fold_size]
        fold_num += 1

    folds = []
    for i in range(k):
        training = []
        for fold_num, split in splits.items():
            if fold_num == i:
                testing = split
            else:
                training+= split
        folds.append((training, testing))

    return folds

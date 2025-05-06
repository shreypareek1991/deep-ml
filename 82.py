"""
https://www.deep-ml.com/problems/82
Write a Python function to calculate the contrast of a grayscale image using the difference between the maximum and minimum pixel values.
Example:
Input:
img = np.array([[0, 50], [200, 255]])
Output:
255
Reasoning:
The function calculates contrast by finding the difference between the maximum (255) and minimum (0) pixel values in the image, resulting in a contrast of 255.
"""

import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	# Your code here
	return np.max(img) - np.min(img)

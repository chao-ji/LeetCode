"""74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # Quick observation:
    # Because 
    #   1. Integers in each row are sorted from left to right.
    #   2. The first integer of each row is greater than the last integer of the previous row.
    #
    # We can treat the matrix as a 1-D sorted array, and use regular binary search
    if not matrix:
      return False
    
    l, h = 0, len(matrix) * len(matrix[0]) - 1
    
    while l <= h:
      m = (l + h) // 2
      i, j = m // len(matrix[0]), m % len(matrix[0])
      
      if matrix[i][j] == target:
        return True
      elif matrix[i][j] < target:
        l = m + 1
      else:
        h = m - 1
      
    return False

"""73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""
# Solution 1
# Use constant space
class Solution(object):
  def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    height = len(matrix)
    width = len(matrix[0])
    zero_first_col = False
    zero_first_row = False
    
    # The main idea is use the first row and col as auxiliary memory
    # to mark the indices of rows and cols that should be zerod, rather
    # than allocating additional memory
    
    # In the meantime, we also need to boolean variables `zero_first_col`
    # and `zero_first_row` to mark if we need to zero the first col
    # and first row themselves
    
    #     
    #
    #     .!!!!!!!!!
    #     ?*********
    #     ?*********
    #     ?*********
    #     ?*********
    #
    # if any `?` or `.` == 0, set `zero_first_col` = True
    # if any `!` or `.` == 0, set `zero_first_row` = True
    #
    # Note if `.` == 0, then both `zero_first_col` and `zero_first_row`
    # should be set to True
    
    for i in range(height):
      if matrix[i][0] == 0:
        zero_first_col = True
        break
        
    for j in range(width):
      if matrix[0][j] == 0:
        zero_first_row = True
        break
    
    # mark corresponding `?` and `!` if the current `*` or `?` or `!` == 0
    for i in range(height):
      for j in range(width):
        # use the first row and col to record which row or col to set to zero 
        if matrix[i][j] == 0:
          matrix[0][j] = 0
          matrix[i][0] = 0
          
    # Use the marker stored in `?` to zero certain rows      
    for i in range(1, height):
      if matrix[i][0] == 0:
        for j in range(1, width):
          # set this row to zero
          matrix[i][j] = 0
          
    # Use the marker stored in `!` to zero certain cols            
    for j in range(1, width):
      if matrix[0][j] == 0:
        for i in range(1, height):
          # set this col to zero
          matrix[i][j] = 0

    # Finally, we set the first row/col to zero according to 
    # `zero_first_row` & `zero_first_col`
    if zero_first_row:
      for j in range(width):
        matrix[0][j] = 0
        
    if zero_first_col:
      for i in range(height):
        matrix[i][0] = 0

# Solution 2
# Use additional memory, space: O(height + width)
class Solution(object):
  def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    height = len(matrix)
    width = len(matrix[0])

    # keep track of the row and col indices of zero-valued elements    
    row_indices = set()
    col_indices = set()
    
    for i in range(height):
      for j in range(width):
        if matrix[i][j] == 0:
          row_indices.add(i)
          col_indices.add(j)
          
    # set the rows to zero
    for i in row_indices:
      for j in range(width):
        matrix[i][j] = 0
    # set the cols to zero    
    for j in col_indices:
      for i in range(height):
        matrix[i][j] = 0
        

"""54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
      return []
    # We traverse the matrix in spiral order, like peeling it off layer by layer 
    #
    #         * * * * * 
    #         * * * * * 
    #         * * * * * 
    #         * * * * *
    # 
    # Each layer as a dimension `height` and `width`, and a starting coordinate
    # When we are done with one layer, we decrement `height` -=1 and `width` -= 1
    # and increment the starting coordinate. 
    
    # E.g. layer 0, height = 4, width = 5, coordinates = (0, 0)
    #
    #         0 * * * * 
    #         *       * 
    #         *       * 
    #         * * * * *
    
    # Layer 1, height = 2, width = 3, coordinates = (1, 1)
    #
    #           1 * *
    #           * * *
    
    # When we traverse a layer, we do it along 4 edges:
    #
    #         1 1 1 1 1
    #         4       2
    #         4       2
    #         3 3 3 3 2
    height = len(matrix)
    width = len(matrix[0])    
    spiral = []
    x, y = 0, 0 # starting coordinate
    
    while height > 0 and width > 0:
      # the 1's
      for j in range(y, y + width):
        spiral.append(matrix[x][j])
      # the 2's
      for i in range(x + 1, x + height):
        spiral.append(matrix[i][y + width - 1])
        
      # Only when `height` > 1, we do the 3's, otherwise we're repeating the 1's
      if height > 1:
        for j in range(y + width - 2, y - 1, -1):
          spiral.append(matrix[x + height - 1][j])
      # Only when `width` > 1, we do the 4's, otherwise we're repeating the 2's    
      if width > 1:
        for i in range(x + height - 2, x, -1):
          spiral.append(matrix[i][y])
          
      x += 1
      y += 1
      height -= 2
      width -= 2
      
    return spiral   

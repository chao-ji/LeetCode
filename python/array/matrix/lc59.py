"""59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
  def generateMatrix(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    matrix = [[0 for j in range(n)] for i in range(n)]
    x, y, counter = 0, 0, 1
    height, width = n, n
    
    # We traverse the matrix in spiral order, like peeling it off layer by layer 
    #
    #         * * * * 
    #         * * * * 
    #         * * * * 
    #         * * * *
    # 
    # Each layer as a dimension `height` and `width`, and a starting coordinate
    # When we are done with one layer, we decrement `height` -=1 and `width` -= 1
    # and increment the starting coordinate. 
    
    # E.g. layer 0, height = 4, width = 5, coordinates = (0, 0)
    #
    #         0 * * * 
    #         *     * 
    #         *     * 
    #         * * * *
    
    # Layer 1, height = 2, width = 3, coordinates = (1, 1)
    #
    #           1 * 
    #           * * 
    
    # When we traverse a layer, we do it along 4 edges:
    #
    #         1 1 1 1
    #         4     2
    #         4     2
    #         3 3 3 2    
    while height > 0 and width > 0:
      for j in range(y, y + width):
        matrix[x][j] = counter
        counter += 1
      for i in range(x + 1, x + height):
        matrix[i][y + width - 1] = counter
        counter += 1
      if height > 1:
        for j in range(y + width - 2, y - 1, -1):
          matrix[x + height - 1][j] = counter
          counter += 1
      if width > 1:
        for i in range(x + height - 2, x, -1):
          matrix[i][y] = counter
          counter += 1
      x += 1
      y += 1
      height -= 2
      width -= 2
    return matrix   

"""221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
# Solution, DP
# time: O(mn), space: O(mn)
class Solution(object):
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
      return 0
    
    height, width = len(matrix), len(matrix[0])
    max_edge = 0
    
    # The idea: straightforward to use DP
    
    # We traverse the matrix in row major order, and whenever we
    # see a `1`, which is by itself a minimal square, we ask whether we can 
    # expand it diagonally (i.e. go up and go left)
    
    # Define `dp[i][j]` = size of the edge of largest square whose bottom right
    # corner is `matrix[i][j]`.
    
    # Base case:
    # First row and col:
    #
    # The squares whose bottom right corners lie in the first row and col
    # can be at most 1
    

    
    # For internal elements in matrix (i.e. not in first row or col)
    # if `matrix[i][j]` == 1, then `dp[i][j]` is bounded by `dp[i - 1][j - 1]` + 1
    
    #     1   1   1   .
    #
    #     1   1   1   .
    #
    #     1   1   1   .
    #   
    #     .   .   .   1
    
    # In addition, to have `dp[i][j]` = `dp[i - 1][j - 1]` + 1, we must also have
    # those elements above and to the left of `matrix[i][j]` be 1's as well,
    #
    # i.e. those `.` as above
    
    # which means `dp[i - 1][j]` and `dp[i][j - 1]` must be as large as 
    # `dp[i - 1][j - 1]`
    
    # So, `dp[i][j]` is bounded by the minimum of 
    # `dp[i - 1][j - 1]`, `dp[i - 1][j]`, `dp[i][j - 1]`
  
    dp = [[0 for j in range(width)] for i in range(height)]
    # base case: first col
    for i in range(height):
      if matrix[i][0] == '1':
        dp[i][0] = 1
        max_edge = max(max_edge, dp[i][0])
    # base case: first row
    for j in range(width):
      if matrix[0][j] == '1':
        dp[0][j] = 1
        max_edge = max(max_edge, dp[0][j])
        
    for i in range(1, height):
      for j in range(1, width):
        if matrix[i][j] == '1':
          dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
          max_edge = max(max_edge, dp[i][j])
    
    return max_edge * max_edge

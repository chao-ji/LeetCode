"""63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


"""


#Solution 1, DP, use 2D auxiliary memory
# time: O(mn), space: O(mn)
class Solution(object):
  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    # The idea: straightforward to use DP
    
    # allocate auxiliary 2-D array `dp`
    
    # `dp[i][j]`: the number of ways to get to grid[i][j] from top left corner.
    # 0 <= i <= m - 1, 0 <= j <= n - 1
    
    
    
    # Base cases:
    #
    # First row and col:
    # There is only one path to get to each element in the first row or col
    # It's reachable only if 
    #   1. It's not blocked by an obstacle.
    #   2. And its previous element is reachable
    
    #           0     1     2     3     4     5   j
    #
    #     0     ?     ?     ?     ?     ?     ?
    #
    #     1     ? 
    #
    #     2     ?     
    #
    #     3     ?     
    #
    #     i
    #
    # `?` = 0 or 1
    
    
    
    # Internal elements:
    #
    # An internal element (i >= 1 and j >= 1) is reachable only if its top
    # element `dp[i - 1][j]` and left elemtn `dp[i][j - 1]` is reachable,
    # given that itself is not blocked by obstacle
    #
    #                         i - 1, j
    #
    #              i, j - 1   i, j
    
    
    # `dp` is initialized to all 0's 
    dp = [[0 for j in range(n)] for i in range(m)]
    # Base cases: first row and col
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(1, m):
      # make sure it's not blocked by obstacle
      if obstacleGrid[i][0] == 0:
        dp[i][0] = dp[i - 1][0]
        
    for j in range(1, n):
      # make sure it's not blocked by obstacle
      if obstacleGrid[0][j] == 0:
        dp[0][j] = dp[0][j - 1]
      
      
    for i in range(1, m):
      for j in range(1, n):
        # make sure it's not blocked by obstacle
        if obstacleGrid[i][j] == 0:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
    return dp[m - 1][n - 1]    


#Solution 2, DP use 1D auxiliary memory
# time: O(mn), space: O(n), `n`: num of cols
class Solution(object):
  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
      
    # The idea: straightforward to use DP
    
    # Instead of allocating a 2-D auxiliary matrix as our
    # dynamic programming memory
    
    # We allocate 2 1-D arrays: `dp_prev` and `dp_curr`
    
    #                     0     1     2     3     4     5     6     j
    #
    # i       dp_prev:    ?     .     .     .     .     .     .
    #
    # i + 1   dp_curr:    ?     .     .     .     .     .     .

    # The algorithm is exactly the same as the one where we allocated a 
    # 2-D array
    #
    # The only DIFFERENCE is that `dp_curr` becomes `dp_prev` as we move
    # to the next row
    
    # allocating 2 1-D arrays
    dp_prev = [0 for j in range(n)]
    dp_curr = [0 for j in range(n)]
    
    # Base case: top left corner
    dp_prev[0] = 1 if obstacleGrid[0][0] == 0 else 0
    # Base case: first row
    for j in range(1, n):
      # make sure it's not blocked by obstacle
      if obstacleGrid[0][j] == 0:
        dp_prev[j] = dp_prev[j - 1]
    
    for i in range(1, m):
      # Base case: first element in each row
      #   reachable only if
      #   1. not blocked by obstacle
      #   2. the element above (i.e. `dp_prev[0]`) in reachable

      dp_curr[0] = 1 if obstacleGrid[i][0] == 0 and dp_prev[0] else 0
      
      for j in range(1, n):
        # make sure it's not blocked by obstacle
        if obstacleGrid[i][j] == 0:
          dp_curr[j] = dp_prev[j] + dp_curr[j - 1]
        else:
          dp_curr[j] = 0
          
      # `dp_curr` becomes `dp_prev`, as we move to next row    
      dp_prev = dp_curr
      
    return dp_prev[-1]   
    
     

"""64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""
# Solution, DP
# time: O(nm), space: O(nm) (can be brought down to O(m))
class Solution(object):
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    
    # The idea: straightforward to use DP
    
    # `min_sum[i][j]` stores the sum of the min-sum path ending at `grid[i][j]`
    #
    #         0   1   2   3   4   5
    #
    #     0   *   *   *   *   *   *
    #
    #     1   *   .   .   .   .   .
    #
    #     2   *   .   .   .   .   .
    #
    #     3   *   .   .   .   .   .
    #
    #     4   *   .   .   .   .   .
    
    # First row & col are just cumulative sums -- there is only one path 
    #
    # For other grid cells, you can only come from UP or LEFT
    #
    # So choose the sum of the min-sum of `min_sum[i - 1][j]` and `min_sum[i][j - 1]`
    
    min_sum = [[0 for j in range(n)] for i in range(m)]
    min_sum[0][0] = grid[0][0]
    
    for j in range(1, n):
      min_sum[0][j] = min_sum[0][j - 1] + grid[0][j]
      
    for i in range(1, m):
      min_sum[i][0] = min_sum[i - 1][0] + grid[i][0]
      
    for i in range(1, m):
      for j in range(1, n):
        min_sum[i][j] = min(
          min_sum[i - 1][j],  # UP 
          min_sum[i][j - 1]   # LEFT
        ) + grid[i][j]
        
    return min_sum[m - 1][n - 1]    
        

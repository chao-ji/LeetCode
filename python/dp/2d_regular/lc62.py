"""62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28


"""

# Solution 1, DP
# time: O(nm), space: O(nm) 
class Solution(object):
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # The idea: straightforward to use DP

    # dp[i][j] = number of ways to get to grid[i][j]
    # `i` = 0, 1, ..., n - 1
    # `j` = 0, 1, ..., m - 1

    #   dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    #           0     1     2     3     4     5   j
    #
    #     0     1     1     1     1     1     1
    #
    #     1     1     2     3     4     5     6
    #
    #     2     1     3     6     10    15    21
    #
    #     3     1     4     10    20    35    36
    #
    #     i

    counts = [[1 for j in range(n)] for i in range(m)]
    for i in range(1, m):
      for j in range(1, n):
        counts[i][j] = counts[i - 1][j] + counts[i][j - 1]
        
    return counts[m - 1][n - 1] 


# Solution 2, DP
# time: O(nm), space: O(n)
class Solution(object):
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # We could save space by keeping only the counts of the previous row

    # previous row:   [1,   *,    *,    *,    *,    *]
    # current row:    [1, 1+*, 1+2*, 1+3*, 1+4*, 1+5*]

    #           0     1     2     3     4     5   j
    #
    #     0     1     1     1     1     1     1
    #
    #     1     1     2     3     4     5     6
    #
    #     2     1     3     6     10    15    21
    #
    #     3     1     4     10    20    35    36
    #
    #     i

    # Essentially, we keep computing the cumulative sum of the cumsum array
    row = [1 for _ in range(n)]
    for i in range(1, m):
      for j in range(1, n):
        row[j] += row[j - 1]  # `row[j]` is the number ABOVE, 
                              # `row[j - 1]` is the number on the left.
    return row[n - 1] 

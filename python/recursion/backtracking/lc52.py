"""52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution(object):
  def totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """
    # `count` is a list holding a single integer, which is the count of valid n-queens board
    # It can be updated internally in the called function.

    count = [0]
    self.solve([], count, n)
    return count[0]
    # Intuition: staightforward to use Backtracking

    # We start with a partial solution (i.e. partially filled n-queens board), and want 
    # to extend until is complete:

    # Grow solution: 
    #
    #      [1]   ====>  [1, 3]  ==>  [1, 3, 0, 2],  complete n-queens board !

    # Note: n-queens board is represented by the col index of each queen in each row:
    # For example:
    #
    #   .Q..
    #   ...Q
    #   Q...
    #   ..Q.
    #
    # is represented as 1, 3, 0, 2

    # When growing the partial solution, we make choices out of a fixed number (i.e. `k`) of
    # options. Some choices would eventually lead us to the final complete solution, while
    # others may take us to dead ends

    # If the goal is to find ALL valid solutions, 
    # then whenever we have a complete solution, or we hit a dead end -- 
    # it means we can no longer grow the current solution.

    # we backtrack -- we return to the calling function, and proceed with the next option.    

  def solve(self, indices, count, n):
    if len(indices) < n:
      for i in range(n):
        if self.isValid(indices + [i]):
          indices.append(i)
          self.solve(indices, count, n)
          indices.pop()
      return
    count[0] += 1 
      
  def isValid(self, indices):
    x1, y1 = len(indices) - 1, indices[len(indices) - 1]
    for i in range(len(indices) - 1):
      x2, y2 = i, indices[i]
      if y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return False
    return True    

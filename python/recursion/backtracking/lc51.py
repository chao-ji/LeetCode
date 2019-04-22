"""51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
class Solution(object):
  def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    solutions = []
    self.solve([], solutions, n)
    return solutions
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
    
  def indicesToBoard(self, indices, n):
    board = [['.' for j in range(n)] for i in range(n)]
    for i in range(len(indices)):
      board[i][indices[i]] = 'Q'
      board[i] = ''.join(board[i])
    return board

  def solve(self, indices, solutions, n):
    if len(indices) < n:
      for i in range(n):
        if self.isValid(indices + [i]):
          indices.append(i)
          self.solve(indices, solutions, n)
          indices.pop()
      # BACKTRACK: 
      # Invalid solution    
      return
    solutions.append(self.indicesToBoard(indices, n))       
    # BACKTRACK (implicit):
    # Final complete solution
        
  def isValid(self, indices):
    x1, y1 = len(indices) - 1, indices[len(indices) - 1]
    for i in range(len(indices) - 1):
      x2, y2 = i, indices[i]
      if y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return False
    return True
  

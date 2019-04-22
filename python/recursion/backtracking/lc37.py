"""37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""
class Solution(object):
  def solveSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    solutions = []
    self.solve(board, solutions, 1)
    for i in range(len(board)):
      board[i] = solutions[0][i]
    
    # Intuition: staightforward to use Backtracking
    
    # We start with a partial solution (i.e. sudoku puzzle board), and want to extend 
    # until is complete:
    
    # Grow solution: 
    #
    #         board   ====>    board with one LESS empty cell  ==>  board completed !
    
    # When growing the partial solution, we make choices out of a fixed number (i.e. `k`) of
    # options. Some choices would eventually lead us to the final complete solution, while
    # others may take us to dead ends
    
    # If the goal is to find ALL valid solutions, 
    # then whenever we have a complete solution, or we hit a dead end -- 
    # it means we can no longer grow the current solution.
    
    # we backtrack -- we return to the calling function, and proceed with the next option.  
    
  def solve(self, board, solutions, num_sols):
    if len(solutions) < num_sols:
      for i in range(9):
        for j in range(9):
          if board[i][j] == ".":
            for k in "123456789":
              if self.isValid(i, j, board, k):
                board[i][j] = k
                self.solve(board, solutions, num_sols)
                board[i][j] = "."
            # BACKTRACK: 
            # Invalid solution
            return     
    
      solutions.append([list(row) for row in board])
      # BACKTRACK (implicit):
      # Final complete solution
      
  def isValid(self, x, y, board, val):
    for i in range(9):
      if i != x and board[i][y] == val:
        return False
    for j in range(9):
      if j != y and board[x][j] == val:
        return False
    for i in range(x // 3 * 3, x // 3 * 3 + 3):
      for j in range(y // 3 * 3, y // 3 * 3 + 3):
        if (i != x or j != y) and board[i][j] == val:
          return False
    return True    
  

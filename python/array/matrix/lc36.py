"""36. Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.


"""
class Solution(object):
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # The three rules can be checked using a hash table (or set)
    #
    # Iterate over the 9 cells for each condition 
    # i.e. row-wise, col-wise, subgrid-wise
    
    # If an existing element is found, report False.
    
    # visited = set()
    
    # for element in candidates:
    #   if element is not in visited:
    #     visited.add(element)
    #   else:
    #     return False
    
    # rows
    for i in range(9):
      s = set()
      for j in range(9):
        if board[i][j] != '.': 
          if board[i][j] not in s:
            s.add(board[i][j])
          else:
            return False
        
    #cols
    for j in range(9):
      s = set()
      for i in range(9):
        if board[i][j] != '.':
          if board[i][j] not in s:
            s.add(board[i][j])
          else:
            return False
        
    # subgrids
    for i in range(3):      # `i`: row index of subgrid
      for j in range(3):    # `j`: col index of subgrid
        s = set()
        # `k` global row index, starting at index 3 * `i`
        for k in range(i * 3, i * 3 + 3):   
          # `l` global col index, starting at index 3 * `j`
          for l in range(j * 3, j * 3 + 3): 
            if board[k][l] != '.':
              if board[k][l] not in s:
                s.add(board[k][l])
              else:
                return False
    
    return True

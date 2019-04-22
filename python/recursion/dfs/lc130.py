"""130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
# Solution 1, Recursive
class Solution(object):
  def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    if not board:
      return 
    
    # The idea:
    
    # When we see a 'O', we don't know if the connected component has an "exit",
    # i.e. there is a path that leads to an 'O' on the boarder.
    
    # We can think differently:
    
    # We scan the four BORDERS of the rectangle, and mark the 'O's in the 
    # connected component to a third markder 'I'. Then all the 'O's that
    # have not been changed must be those for whcich there is NO path to the
    # 'O' on the borders.
    
    # e.g.
    
    #         X X X X
    #         X O O X
    #         X X O X
    #         X O X X
    
    #         X X X X
    #         X O O X       the three 'O's are those that should be flipped
    #         X X O X
    #         X I X X
    
    # We finally flipp those 'O's to 'X', and restore the 'I's back to 'O' that
    # should NOT been flipped.
    
    #         X X X X
    #         X X X X
    #         X X X X
    #         X O X X

    # mark 'O' connected to boarders    
    for i in range(len(board)):
      self.fill(i, 0, board)
      self.fill(i, len(board[0]) - 1, board)
      
    for j in range(1, len(board[0]) - 1):
      self.fill(0, j, board)
      self.fill(len(board) - 1, j, board)
      
    # flipp the internal 'O's, and restore 'I's back to 'O's 
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == "O":
          board[i][j] = "X"
        elif board[i][j] == 'I':
          board[i][j] = "O"
      
  def fill(self, i, j, board):    
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
      board[i][j] = "I"
    
      self.fill(i - 1, j, board)
      self.fill(i + 1, j, board)
      self.fill(i, j - 1, board)
      self.fill(i, j + 1, board)
    
# Solution 2, Iterative
class Solution(object):
  def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    if not board:
      return 
    
    # The idea:
    
    # When we see a 'O', we don't know if the connected component has an "exit",
    # i.e. there is a path that leads to an 'O' on the boarder.
    
    # We can think differently:
    
    # We scan the four BORDERS of the rectangle, and mark the 'O's in the 
    # connected component to a third markder 'I'. Then all the 'O's that
    # have not been changed must be those for whcich there is NO path to the
    # 'O' on the borders.
    
    # e.g.
    
    #         X X X X
    #         X O O X
    #         X X O X
    #         X O X X
    
    #         X X X X
    #         X O O X       the three 'O's are those that should be flipped
    #         X X O X
    #         X I X X
    
    # We finally flipp those 'O's to 'X', and restore the 'I's back to 'O' that
    # should NOT been flipped.
    
    #         X X X X
    #         X X X X
    #         X X X X
    #         X O X X
    
    # mark 'O' connected to boarders
    for i in range(len(board)):
      self.fill(i, 0, board)
      self.fill(i, len(board[0]) - 1, board)
      
    for j in range(1, len(board[0]) - 1):
      self.fill(0, j, board)
      self.fill(len(board) - 1, j, board)
    
    # flipp the internal 'O's, and restore 'I's back to 'O's 
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == "O":
          board[i][j] = "X"
        elif board[i][j] == 'I':
          board[i][j] = "O"
      
  def fill(self, i, j, board):    
    queue = [(i, j)]
    while queue:
      i, j = queue.pop(0)
      if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
        board[i][j] = 'I'
        queue.append((i + 1, j))
        queue.append((i - 1, j))
        queue.append((i, j + 1))
        queue.append((i, j - 1))

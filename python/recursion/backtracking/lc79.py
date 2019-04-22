"""79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution(object):
  def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    # The idea: use backtracking
    
    # We try to match the word starting from each location in the board.
    
    # We start with a growing prefix of the word, represented by the index `index`, i.e.,  
    # the prefix `word[:index]` has been matched starting from the current location in the
    # board. Initially, there is nothing matched.
    
    # We make choice of growing the current prefix in four different directions:
    # NORTH, SOUTH, WEST, EAST
    # as long as the choice is VALID, i.e. 0 <= x < height, 0 <= y < width, and 
    # board[x][y] == word[index] 
    
    # Some choices would eventually lead us to the fully matched word, while
    # others may take us to dead ends, i.e. we hit a mismatched character.
    
    # Whenever we have a complete solution, or we hit a dead end -- 
    # it means we can no longer grow the current solution.

    # we backtrack -- we return to the calling function, and proceed with the next option.  
    
    found = [False]
    for i in range(len(board)):
      for j in range(len(board[0])):
        self.search(board, i, j, 0, word, found)
        if found[0]:
          return True
        
  def search(self, board, x, y, index, word, found):
    if found[0] is False:
      # when the solution is not yet complete
      if index < len(word):
        # and when the current choice is valid
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[index]:
          board[x][y] = '.'
          self.search(board, x - 1, y, index + 1, word, found)
          self.search(board, x + 1, y, index + 1, word, found)
          self.search(board, x, y - 1, index + 1, word, found)
          self.search(board, x, y + 1, index + 1, word, found)
          board[x][y] = word[index]
        # BACKTRACK  
        return
      
      found[0] = True

"""200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
# Solution 1, DFS

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
      return 0
   
    # See LC130 Surrounded Regions
 
    # The idea:
    
    # After we encounter a 1, we increment the `count` and we fill each connected
    # component of 1's with 0's. So we won't count the same connected component
    # repeatedly.
    
    count = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == "1":
          count += 1
          self.mark(i, j, grid)
          
    return count      
        
  def mark(self, i, j, grid):
    # If there is still 1's in the same connected component, we fill it with 0,
    # and keep exploring the four neighbors
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
      grid[i][j] = '0'
      self.mark(i - 1, j, grid)
      self.mark(i + 1, j, grid)
      self.mark(i, j - 1, grid)
      self.mark(i, j + 1, grid)
  
    
# Solution2, BFS
class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
      return 0
    
    # The idea:
    
    # After we encounter a 1, we increment the `count` and we fill each connected
    # component of 1's with 0's. So we won't count the same connected component
    # repeatedly.
    
    count = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == "1":
          count += 1
          self.mark(i, j, grid)
          
    return count      
        
  def mark(self, i, j, grid):
    # If there is still 1's in the same connected component, we fill it with 0,
    # and keep exploring the four neighbors
    queue = [(i, j)]
    
    while queue:
      i, j = queue.pop(0)
      if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
        grid[i][j] = '0'
        queue.append((i + 1, j))
        queue.append((i - 1, j))
        queue.append((i, j + 1))
        queue.append((i, j - 1))
  
    
        

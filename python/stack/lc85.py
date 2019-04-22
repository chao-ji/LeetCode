"""85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""
# Use Largest Rectangle in Histogram 84 as a subroutine
# Stack, O(n)
class Solution(object):
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
      return 0
    
    heights = [1 if matrix[0][j] == '1' else 0 for j in range(len(matrix[0]))]

    area = self.maxArea(heights)
    for i in range(1, len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == '1':
          heights[j] += 1
        else:
          heights[j] = 0
      area = max(area, self.maxArea(heights))
    return area
    
  # LC 84: Largest Rectangle in Histogram
  def maxArea(self, heights):
    area = 0
    stack = []
    heights = heights + [0] 

    i = 0
    while i < len(heights):
      if not stack or heights[stack[-1]] < heights[i]:
        stack.append(i)
        i += 1
      else:
        j = stack.pop()
        area = max(area, (i - 1 - (stack[-1] if stack else -1)) * heights[j])
    
    return area    

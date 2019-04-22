"""11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
# Solution 1
# Brute force, O(n^2)
class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    for i in range(len(height)):
      for j in range(i + 1, len(height)):
        max_area = max(max_area, min(height[i], height[j]) * (j - i))
        
    return max_area 

# Solution 2
# Two pointers, O(n)
class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    low, high = 0, len(height) - 1
    
    # Quick observation: the amount of water trapped between two lines `i` and `j`
    # is bounded by the shorter of `i` and `j`
    
    #
    #                |
    #                |
    #   |            |
    #   |            |
    #   |            |
    #   |            |       
    #   i            j
    # 
    # whenever `height[i]` < `height[j]`
    # moving `j` leftward would result in a strictly lower width `j` - `i`, and a height
    # NO LARGER than `height[i]`
    
    # The search space is 0 <= i < j <= len(height) - 1
    # which can be visualized as 
    # 
    #     0 1 2 3 4 5 j
    #   0   * * * * O
    #   1     * * * *
    #   2       * * *
    #   3         * *
    #   4           *
    #   i
    # assuming `len(height)` == 6
    
    # At each iteration we either increment `i`
    #
    #     0 1 2 3 4 5 j
    #   0   x x x x x
    #   1     * * * O
    #   2       * * *
    #   3         * *
    #   4           *
    #   i
    #
    # In this case, we have `height[0]` < `height[5]`, so we claim that
    #   area(0, 5) > area(0, 4) 
    #              > area(0, 3)
    #              ...
    #              > area(0, 1)
    #
    
    # or decrement `j` 
    #
    #     0 1 2 3 4 5 j
    #   0   * * * * O
    #   1     * * * x
    #   2       * * x
    #   3         * x
    #   4           x
    #   i
    #
    # In this case, we have `height[0]` >= `height[5]`, so we claim that
    #   area(0, 5) >= area(1, 5)
    #                 area(2, 5)
    #              ...
    #                 area(4, 5)
    #
    # Either way, we have completed the search for all `i'`s < `i`, or
    # all `j'`s > `j`,
    
    # Eventually, when `i` == `j`, e.g. i = 2, j = 3
    #     0 1 2 3 4 5 j
    #   0   x x x x x
    #   1     x x x x
    #   2       O x x
    #   3         x x
    #   4           x
    #   i
    # We have searched the entire space of `i` < `j` pairs
    
    while low < high:
      max_area = max(max_area, min(height[high], height[low]) * (high - low))
      if height[low] < height[high]:
        low += 1
      else:
        high -=1
        
    return max_area    

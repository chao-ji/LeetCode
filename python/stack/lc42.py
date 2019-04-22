"""42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

1: bar
0: water

               1
       1 . . . 1 1 . 1
 _ 1 . 1 1 . 1 1 1 1 1 1
  
 0 1 2 3 4 5 6 7 8 9 1011    
 
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
# Solution 1, 
# Stack, time: O(n), space: O(n)
class Solution(object):
  def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    # The water could be trapped in a number of local "ponds", where each pond has
    # a left slope (non increasing bars) and right slope (non decreassing bars).
    #
    # We maintain a stack holding bar indices of the left slope, where bar heights
    # are non-increasing, and as soon as we find the first bar with height > the
    # height of the bar at the top of the stack, there must be water trapped between
    # these current bar and the bar below the top
    #
    #      1
    #      1 1  
    #      1 1 1 1
    #      1 1 1 1 0 0 1
    #      ^ ^   ^ t   i
    # t: top
    # i: current bar
    # ^: bar indices on stack
    # water trapped between the most recent ^ and i
    
    # Note: if current bar `i` has the same height as the top of stack, we pop
    # the top and push the new index `i`, since we want to keep the most recent
    # bar.
    if not height:
      return 0
    
    # find the leftmost positive height as the initial left bar 
    left = 0
    while left < len(height):
      if height[left] > 0:
        break
      left += 1   
    
    stack = [left]
    area = 0
    
    #
    #               o
    #       o       o
    #       ooo     o  
    #       ooo     o
    #       oooo....o
    #       012345678
    #          tj   i
    # stack = [0, 2, 3, 4]
    # i = 8
    # 
    # the amount of water trapped will be
    # (i - t - 1) * (min(height[t], height[i]) - height[j]) == 4 * 1
    i = left + 1
    while i < len(height):
      if not stack or height[stack[-1]] > height[i]:
        stack.append(i)
        i += 1
      else:
        j = stack.pop()
        if stack and height[j] < height[i]:
          area += (i - stack[-1] - 1) * (min(height[stack[-1]], height[i]) - height[j])
        
    return area        
           
# Solution 2
# DP, time: O(n), space: O(n)
class Solution(object):
  def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
      return 0
    
    # Water can't be trapped at the first (0) and last bar (`len(height)` - 1).
    # For internal bars (i.e. [1, len(height) - 2]), if we know the max-height
    # bar from the left, and max-height bar from the right,
    # we can compute the water trapped as 
    #
    # `min(max_height_left, max_height_right)` - `height[i]`
    
    # Use DP to keep track of the max-height bars from left and from right.
    # They will be reused when computing water trapped across internal bars.
    area = 0
    max_sofar_left = [0 for _ in range(len(height))]    
    max_sofar_right = [0 for _ in range(len(height))]
    
    max_sofar_left[0] = height[0]
    for i in range(1, len(height)):
      max_sofar_left[i] = max(max_sofar_left[i - 1], height[i])
      
    max_sofar_right[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
      max_sofar_right[i] = max(max_sofar_right[i + 1], height[i])
      
    for i in range(1, len(height) - 1):
      side = min(max_sofar_left[i - 1], max_sofar_right[i + 1])
      if side > height[i]:
        area += (side - height[i])
        
    return area     

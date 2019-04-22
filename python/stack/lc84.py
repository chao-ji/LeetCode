"""84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


      6 
    5 o
    o o
    o o   3
2   o o 2 o
o 1 o o o o
o o o o o o


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.


      6 
    5 o
    i i
    i i   3
2   i i 2 o
o 1 i i o o
o o i i o o


Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
# Solution 1
# Brute force, O(n^2)
class Solution(object):
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    #    ..
    #   ... .
    #   .....
    #   .....
    #   i   j
    #  min_height = 2

    # For each bar `i` and bar `j` >= `i`, find the bar in between `i` and `j`
    # with minimum height `min_height`
    # The area is computed as (`j` - `i` + 1) * `min_height`
    max_area = 0
    # `i`: left boundary
    for i in range(len(heights)):
      min_height = heights[i]
    
      # `j`: right boundary
      # `min_height`: keeps track of minimum height between `i` and `j`
      # as we move the right boundary  
      for j in range(i, len(heights)):
        min_height = min(min_height, heights[j])
        max_area = max(max_area, min_height * (j - i + 1))
    return max_area   

# Solution 2
# Brute force, O(n^2)
class Solution(object):
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    area = 0
    # For each bar `i`, move pointer `j` (initialized to `i`) backward and then forward,
    # until the first bar with height < `height[i]`, i.e. `low` and `high`.
    #
    # area = `height[i]` * (high - low - 1)
    for i in range(len(heights)):
      for j in range(i, -2, -1):
        if j >= 0 and heights[j] < heights[i]:
          break
      low = j
      
      for j in range(i, len(heights) + 1):
        if j < len(heights) and heights[j] < heights[i]:
          break
      high = j
      
      area = max(area, (high - low - 1) * heights[i])
    return area  

# Solution 3
# Stack, O(n)
class Solution(object):
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # For each `heights[i]` in `heights`, if we could find the area `max_area(i)` of the 
    # largest rectangle with `heights[i]` as the smallest bar, then we are done -- the 
    # result will be the maximum over all `max_area(i)`
    #
    # The naive approach would be scanning in both directions from the index `i`, until you
    # find the first bar whose height < `heights[i]`, we call them the left and right border.
    #
    # the indices of the bars making the largest rectangle would be `left + 1`, `left + 2`, ...
    # `right - 2`, `right - 1`, inclusive at both ends.
    # the `max_area(i)` is simply `(right - left - 1)` * `heights[i]`
    #
    # This would take O(n^2)
    #
    # Given input
    #
    #                           6
    #                         5 . 
    #                         . . 
    #                         . .   3
    #                     2   . . 2 .
    #                     . 1 . . . .
    #                     . . . . . . 
    #                  i: 0 1 2 3 4 5
    # we have 
    # i     | left        | right         | max_area
    # 0     | -1          | 1             | 2 
    # 1     | -1          | 6             | 6
    # 2     | 1           | 4             | 10
    # 3     | 2           | 4             | 6
    # 4     | 1           | 6             | 8
    # 5     | 4           | 6             | 3
    
    # So the question boils down to how we can efficiently find the left and right border of 
    # the largest rectangle for each `heights[i]`    
    
    max_area = 0
    # We maintain a stack of bar indices out of the numbers from 0 to `len(heights) - 1` with the 
    # following loop invariant:
    #
    # LOOP INVARIANT:
    # ################################################################################################
    # (1)
    # The stack always contains increasing indices of bars with strictly increasing heights, i.e.
    # `stack[0]` < `stack[1]` < ... < `stack[-1]`, and
    # `height[stack[0]]` < `height[stack[1]]` < ... < `height[stack[-1]]`,
    #
    # Moreover
    # (2)
    # for `i` = 1, 2, ..., `len(stack) - 1`, i.e. all but the bottom of the stack,  `stack[i - 1]` 
    # holds the largest index < `stack[i]`, such that `height[stack[i - 1]]` < `height[stack[i]]`, 
    # that is, `stack[i - 1]` holds the index of the most recent bar to the left of `stack[i]` with 
    # a smaller height, i.e. the left border of `stack[i]`
    #
    # As a special case, `stack[0]` has no bar to the left that has a smaller height than `stack[0]`. 
    # This can be thought of as there is an imaginary 0-height bar at index -1, preceding all bars in
    # `heights`.
    ##################################################################################################
    
    stack = []
    heights = heights
    i = 0
    while i < len(heights):
      if not stack or heights[stack[-1]] < heights[i]:
        stack.append(i)
        i += 1
      else:  
        j = stack.pop()
        max_area = max(max_area, (i - 1 - (stack[-1] if stack else -1)) * heights[j])
      
      # We prove that the Loop invariant still holds at the end of each iteration:
      
      # Note in the CURRENT iteration, the loop EITHER pushes the index `i` OR removes the top of the stack
      # 
      # 1) The top of the stack was removed: in this case, the loop invariant still 
      #    holds -- the inequalities and constraints are unchanged except that we just have one less of them.
      # 
      # 2) A new index `i_curr` is pushed to stack: Note that the looping variable `i_curr` is always
      #    incremented after it's pushed to stack, so the element being pushed to stack
      #    will always be greater than those previously pushed to stack. And since a new index is pushed
      #     to stack only if its height > that at the top of the stack, so loop invariant (1) still holds.
      #
      #    To prove loop invariant (2), we need to consider what the loop did to the stack in the PREVIOUS
      #    iteration:
      #     A. The index `i_prev` was pushed to stack, then `i_prev` is incremented, and in the current
      #       iteration, `i_curr` is pushed. In this case, 
      #       the current loop vairable `i_curr` is exactly the very next integer of `i_prev` -- 
      #       `i_curr` = `i_prev` + 1, and we have `height[i_prev]` < `height[i_curr]`, so `i_prev` must be the
      #       largest index < `i_curr` such that `height[i_prev]` < `height[i_curr]`.
      #
      #     B. Some index `i_prev` was popped off the stack, and in the current iteration, `i_curr` is pushed.
      #       Note that we must have `i_prev` < `i_curr` and `heights[i_curr]` <= `heights[i_prev]`
      #
      #       In this case, if there is any bar in `heights` with index `i` in the range `i_prev` + 1, ... 
      #       `i_curr` - 1 (inclusive at both ends), we must have `heights[i]` > `height[i_curr]`. Because if
      #       `heights[i]` <= `heights[i_curr]`, where `i_prev` + 1 <= `i` <= `i_curr` - 1 
      #       we have `heights[i]` <= `heights[i_prev]`, so `i_prev` would have been popped when we see
      #       `i`. 
      #       This means the element immediately below `i_prev` must hold the largest index of the bar with 
      #       height < `heights[i_curr]`.
           
      
    while stack:
      j = stack.pop()
      max_area = max(max_area, (i - 1 - (stack[-1] if stack else -1)) * heights[j])
      
    return max_area 


# Solution 4
# Divide and Conquer, O(n * logn)
class Solution(object):
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """    
    # Divide and conquer: O(n*logn)
    
    # Build segment tree that stores min value in ranges
    st = SegmentTree(0, len(heights) - 1)
    for i, v in enumerate(heights):
      st.insert(st.root, i, v)
 
    return self.largest(heights, st, 0, len(heights) - 1)   
 
  def largest(self, heights, st, start, end):
    if start > end:
      return 0

    #       .
    #    .  .. 
    #   ... ..
    #   ......
    #   ......
    #      ^
    # ^: bar with min height, compute max rectangle area in the left and right subarray divided by ^

    # Find the min value in `heights` from `start` to `end`, inclusive at both ends
    index, min_height = st.query(st.root, start, end)
    # Find the area of the max rectangle in the left subarray
    left = self.largest(heights, st, start, index - 1)
    # Find the area of the max rectangle in the right subarray
    right = self.largest(heights, st, index + 1, end)
    
    # The only max rectangle that spans the left and right subarrays is the one with `height[index]`
    # i.e. `min_height` as the smallest bar, with width `end - start + 1`
    return max(max(left, right), min_height * (end - start + 1))
  
  
class Node(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.key = None
    self.val = None
    self.left = None
    self.right = None


class SegmentTree(object):
  def __init__(self, start, end):
    self.root = Node(start, end)

  def insert(self, node, key, val):
    if key < node.start or key > node.end:
      return

    if node.val is None:
      node.val = val
      node.key = key
    elif node.val > val:
      node.val = val
      node.key = key

    if node.start == node.end:
      return

    mid = (node.end - node.start) // 2 + node.start

    if key <= mid:
      if node.left is None:
        node.left = Node(node.start, mid)
      self.insert(node.left, key, val)
    else:
      if node.right is None:
        node.right = Node(mid + 1, node.end)
      self.insert(node.right, key, val)

  def query(self, node, start, end):
    """Returns the min value (`val`) and its index (`key`) within the `heights` array
    """
    if node is None or end < node.start or start > node.end or start > end:
      return None

    mid = (node.end - node.start) // 2 + node.start

    if start == node.start and end == node.end:
      key, val = node.key, node.val
    elif start <= mid and end <= mid:
      key, val = self.query(node.left, start, end)
    elif start >= mid + 1 and end >= mid + 1:
      key, val = self.query(node.right, start, end)
    else:
      key, val = self._merge(
          self.query(node.left, start, mid),
          self.query(node.right, mid + 1, end))
    return key, val

  def _merge(self, left, right):
    if left is not None and right is not None:
      return left if left[1] < right[1] else right
    elif left is not None and right is None:
      return left
    elif left is None and right is not None:
      return right

    return None

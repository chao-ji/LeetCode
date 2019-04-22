"""55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
# Solution 1
# DP, O(n)
class Solution(object):
  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) <= 1:
      return True

    # `target` initialized to the next index to be reached     
    target = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
      # `i` initialized to the index immediately preceding `target`
      # Now we iteratively tests if `target` is reachable from `i`

      # If yes, we update `target` to the current index `i` -- our next target
      if i + nums[i] >= target:
        target = i
      # Else, we keep `target` unchanged -- we still need to get from `i` to `target`        

    return target == 0

# Solution 2
# Greedy, O(n)
class Solution(object):
  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # Quick observation: if `nums` are all positive, then there is always a path --
    # keep jumping to the very next index until you get to the end.

    # Use the same strategy as Jump Game ii LC45: unless you can jump to the target
    # in a SINGLE STEP, you always want to jump furthest in TWO STEPS.
    i = 0
    while i < len(nums):
      if i + nums[i] >= len(nums) - 1:
        return True
      
      furthest_index = 0
      next_i = i
      for j in range(i + 1, i + 1 + nums[i]):
        if furthest_index < j + nums[j]:
          furthest_index = j + nums[j]
          next_i = j
          
      if next_i > i:
        i = next_i
      else:
        break
    return False    
        
        
    

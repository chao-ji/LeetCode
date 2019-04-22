"""45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
# Solution 1 (TLE)
# Dynamic Programming, O(n^2)
import sys

class Solution(object):
  def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    # `dp[i]` stores the minimum number of steps to reach `nums[i]` from nums[0]

    # `dp[0]` is set to 0 -- it takes 0 steps from 0 to get 0
    dp = [0 for i in range(n)]
    
    for i in range(1, n):
      dp[i] = sys.maxint
      for j in range(i): # `j` is the previous stop
        if j + nums[j] >= i:
          dp[i] = min(dp[j] + 1, dp[i])
    return dp[n - 1]      

# Solution 2 (TLE)
# BFS
class Solution(object):
  def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    queue = [0]
    dist = {0: 0}
    while queue:
      q = queue.pop(0)
      if q < len(nums):
        for i in range(1, nums[q] + 1):
          if q + i not in dist and q + i < len(nums):
            dist[q + i] = dist[q] + 1
            queue.append(q + i)
          
    return dist[len(nums) - 1] 
# Solution 3
# Greedy, O(n)
class Solution(object):
  def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # The rationale is very simple:
    #
    # At any point in the path to the last index, first you want to check if it is 
    # possible to reach your target in a SINGLE STEP, i.e. i + nums[i] >= last index.
    #
    # Otherwise, it means you need at least TWO JUMPS to reach the last index, so you
    # would always want to choose the strategy that allows you to jump the furthest in 
    # TWO STEPS.
    
    # Greedy strategy:
    #
    #
    # .   .   .   .   .   .   .   .   .   .   .   .   .   .
    # i       j           j'  ^               j1'     j1
    # 
    # suppose `i` is where we are at now,
    # `^` is the furthest index reachable from `i` in a single step
    
    # case 1: if the last index is at or to the left of `^`, we are 
    #     just one step away from our goal
    #
    # case 2: Suppose there are indices `j` and `j'` that are reachable
    #     from `i` in a single step, in addition, j1 > j1' where
    #     `j1` is the furthest index reachable from `j`
    #     `j1'` is the furthest index reachable from `j'`
    #
    # If we were to choose `j'` in the optimal solution, then choosing
    # `j` would result in a solution NO WORSE than the one in which we choose `j'`
    
    # Because the next stop from `j'` in the optimal solution (i.e. between
    # `j'` and `j1'`) is also reachable from `j`.
    
    # So in the optimal solution, we need to choose the index between `i` and
    # `^` from where you can jump to the furthest index, i.e.
    #  argmax j + nums[j], over `j` in [i + 1, ^]
    num_steps, i = 0, 0
    while i < len(nums):
      # check if the last index `len(nums)` - 1 is reachable 
      # in a SINGLE STEP
      if i + nums[i] >= len(nums) - 1:
        if i < len(nums) - 1:
          num_steps += 1
        break
      
      # If not, we select the index that allows us to jump furthest in TWO STEPS.
      furthest_index = 0
      for j in range(i + 1, i + 1 + nums[i]):
        if furthest_index < j + nums[j]:
          furthest_index = j + nums[j]
          next_i = j

      i = next_i    
      num_steps += 1
      
    return num_steps  

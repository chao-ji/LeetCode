"""377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
class Solution(object):
  def combinationSum4(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # The idea: 1-D dynamic programming, like LC70, Climb Stairs
    #
    # We're trying to find number of Sequences of jumps that lead to the
    # integer `target`
    #
    
    # dp[i] = number of sequences of positive integers that add up to 
    # `target`, where 0 <= i <= `target`
    
    # When our target is 0, there is none but one way to add to `target`:
    # We have an empty sequence
    
    # To compute `dp[i]`, `i` > 0, we consider what was the last step in
    # the sequence,
    
    # 0       1    ...  i-k  ...      i-3     i-2     i-1     i                 
    # .       .                       .       .       .       .  
    #                                         <- last step=2 ->
    # 
    #                               ...     ...
    #
    #                   <------------- last step=k ----------->
    #
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for i in range(1, target + 1):
      for j in range(len(nums)):
        if i - nums[j] >= 0:
          dp[i] += dp[i - nums[j]]
    return dp[target]      

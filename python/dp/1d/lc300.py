"""300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""
# Solution, regular DP
# time: O(n^2), space: O(n)
class Solution(object):
  def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    
    # straightforward to use DP
    
    # `dp[i]` = length of longest increasing subsequence ending at index `i`
    # `i` = 0, 1, ..., n - 1
    
    # Since solution to each subproblem always includes index `i`, we would
    # want to extend it in the backward direction:
    
    # We compare `nums[i]` with each `nums[j]`, 0 <= j <= i - 1
    
    # If `nums[i]` > `nums[j]`, we would be able to extend `nums[i]` by 
    # `dp[j]`: 
    # length of increasing subsequence ending at index `j`, plus index `i`
    # and the length = `dp[j]` + 1
    
    # All we need to do is to find which `j` maximizes `dp[j]`
    
    #       .      .      .      .      .      .      .
    #       0                                  i-1    i
    #       <================== j =============>
    #   `j` precedes `i`, and we require `nums[j]` < `nums[i]`
    
    n = len(nums)
    
    # Base cases:
    # each element by itself is a increasing subsequence of length 1
    # so `dp[0]` = 1
    dp = [1 for _ in range(n)]
    dp[0] = 1
    
    # `max_len` holds global maximum length of longest increasing subsequence
    max_len = 1
    
    for i in range(1, n):
      # `j` = 0, 1, ..., i - 1
      for j in range(i):
        if nums[j] < nums[i]:
          dp[i] = max(dp[i], dp[j] + 1)
      max_len = max(max_len, dp[i])    
    return max_len

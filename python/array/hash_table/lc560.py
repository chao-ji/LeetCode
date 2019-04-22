"""560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

# Solution, hash map
# time: O(n), space: O(n)
class Solution(object):
  def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # See LC1 Two Sum

    # The idea:
    # 
    # Since we are working with CONTINUOUS subarrays, it would be helpful to convert
    # the original array into cumulative sums, and sums of continuous subarrays become
    # difference in cumulative sums:
    
    
    # k = 10
    # array:
    #           3   1   4   1   5   9   2   6
    #                   ^   ^   ^
    #                   2   3   4
    
    # cum sums:
    #       0   3   4   8   9   14  23  25  31
    #               j=2         i=5                        
    
    # For `cumsums[i]` (`i` >= 1), we ask if there is `cumsums[j]` (`j` < `i`), such
    # that `cumsums[j]` + `k` == `cumsums[i]`.
    
    # If so, then we have `a[j]` + ... `a[i - 1]` == `k`
    
    
    # So the problem reduces to finding two numbers in `cumsums` where the second number
    # minus the first number is `k`. 
    
    # This is similar to the LC1 Two-Sum problem:
    
    # We use a hash map that counts the number of cumulative sums with value `cumsums[i]`
    #
    # We traverse the array `cumsums` starting at index 1, and we ask how many continuous 
    # subarrays ending at index `i` have sum equal to `k`, which should be
    
    # hashmap[cumsums[i] - k], if `cumsums[i] - k` is present in `hashmap`
    
    # cum sums:   k = 10
    #       0   3   4   8   9   14  23  25  31
    #               j=2         i=5     
    
    # 14 - 10 == 4 is previously encountered once, so `count` += 1
    
    
    # build cumulative sums
    cumsums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
      cumsums[i + 1] = cumsums[i] + nums[i]
    
    # initialize memory
    memory = {}
    memory[cumsums[0]] = 1
    # overall count
    count = 0
    
    # for each index `i`, count the number of subarrays with sum `k`, ending at 
    # index `i`
    for i in range(1, len(cumsums)):
      if cumsums[i] - k in memory:
        # update overal count at each index `i`
        count += memory[cumsums[i] - k]
      
      # update the count in `memory`
      memory[cumsums[i]] = memory.get(cumsums[i], 0) + 1
    return count   

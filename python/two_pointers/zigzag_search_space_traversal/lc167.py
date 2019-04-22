"""167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    # The idea: we traverse the triangular search space in zigzag fashion
    
    #      h:   0   1   2   3   4   5   6    
    #                                       l
    #           x   .   .   .   .   .   *   0
    #
    #               x   .   .   .   .   .   1
    #
    #                   x   .   .   .   .   2
    #
    #                       x   .   .   .   3
    #
    #                           x   .   .   4
    #       
    #                               x   .   5
    #                                 
    #                                   x   6  
    
    # The search space consists of all pairs of `i`, `j`, s.t.
    #
    # 0 <= i < j <= n - 1
    
    # initially we put `low` = 0, `high` = `n` - 1
    # unless `nums[low]` + `nums[high]` == `target`
    #
    # if `nums[low]` + `nums[high]` < `target`
    #
    # we can exclude (low, high) in the search space, but we can also
    # rule out (low, high-1), (low, high-2), ... (low, low+1),
    # because these would lead to EVEN SMALLER sum than (low, high), given
    # that the numbers are sorted in ascending order. So we would increment
    # `low`, i.e. eliminate the first row in the triangular search space:
    

    #      h:   0   1   2   3   4   5   6    
    #                                       l
    #           x   *   *   *   *   *   *   0
    #
    #               x   .   .   .   .   *   1
    #
    #                   x   .   .   .   .   2
    #
    #                       x   .   .   .   3
    #
    #                           x   .   .   4
    #       
    #                               x   .   5
    #                                 
    #                                   x   6      
    
    # likewise, if `nums[low]` + `nums[high]` > `target`
    
    # we would eliminate the first column in the triangular search space.
    
    # In each iteration we cross out a row or a column, until we hit the `x`'s
    # where `low` == `high`.
    # By that time, we have exhausted the entire search space.
    
    low, high = 0, len(numbers) - 1
    
    while low < high:
      if numbers[low] + numbers[high] == target:
        return [low + 1, high + 1]
      elif numbers[low] + numbers[high] < target:
        low += 1
      else:
        high -= 1
        
        

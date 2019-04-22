"""75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # maintain 3 pointers `i`, `j` and `k` such that 
    
    # [0, i), stores 0
    # [i, j), stores 1
    # [j, k), stores 2
    # `k` points to the current number 
    
    i = j = 0
    for k in range(len(nums)):
      # nums[:i] stores 0's
      # nums[i:j] stores 1's
      # nums[j:k] sotres 2's
      if nums[k] == 2:
        # 000001111112222222
        #      i     j     k
        # =>
        # 000001111112222222
        #      i     j      k
        
        # `k` will be automatically incremented, do nothing
        pass
      elif nums[k] == 1:
        # 000001111112222221
        #      i     j     k
        # =>
        # 000001111111222222
        #      i      j     k        
        nums[k] = 2
        nums[j] = 1
        j += 1
      else:
        # 000001111112222220
        #      i     j     k
        # =>
        # 000000111111222222
        #      i     j      k
        nums[k] = 2
        nums[j] = 1
        j += 1
        nums[i] = 0
        i += 1

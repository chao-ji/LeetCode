"""88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
class Solution(object):
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # The idea: we start from the END of both arrays 
       
    # Use the additional space in `nums1` as auxiliary memory
    
    # `nums1`, m = 7
    #
    # *   *   *   *   *   *   *   .   .   .   .   .
    # 0                       m-1                 m+n-1
    #
    #                         ^                   ^  
    #                         i                   k
    
    # `nums2`, n = 5
    #
    # *   *   *   *   *
    # 0               n-1
    #
    #                 ^
    #                 j
    
    # `k` takes the larger of `i` and `j`    
    
    i, j = m - 1, n - 1
    k = m + n - 1
    
    # at any time, `k` = `i` + `j` + 1
    while i >= 0 and j >= 0:
      if nums1[i] >= nums2[j]:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1
      else:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    
    # at this point, we need to move numbers remaining in `nums2` to araary `nums1`
    
    # `nums1`, 
    #
    # .   .   .   .   .   *   *   *   *   *   *   *   
    # 0               k           
    #
    # i = -1
    
    # `nums2`, 
    #
    # *   *   *   *   *
    #                 j
    while j >= 0:
      nums1[k] = nums2[j]
      k -= 1
      j -= 1
      
      


"""4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
import sys

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # `a` = `len(nums1)`, `b` = `len(nums2)`
    
    # if `a` + `b` is odd, there are equal number of numbers < and > median
    #     . . . . . m . . . . . 
    
    
    # if `a` + `b` is even, we need to find two numbers `p` and `q`
    #     . . . . . p q . . . . .
    
    
    # the number of numbers < p == the number of numbers > q
    
    if (len(nums1) + len(nums2)) % 2 == 1: 
      return self.findKth(nums1, nums2, (len(nums1) + len(nums2) + 1) // 2)
    else:
      median1 = self.findKth(nums1, nums2, (len(nums1) + len(nums2)) // 2)
      median2 = self.findKth(nums1, nums2, (len(nums1) + len(nums2)) // 2 + 1)
      return (median1 + median2) / 2.0
    
  def findKth(self, nums1, nums2, k):
    """Find the k th largest number in the union of `nums1` and `nums2`"""
    
    # Assumption:
    
    # `nums1` and `nums2` are sorted in ascending order
    # 1 <= `k` <= len(nums1) + len(nums2)
    
    # The idea is simple:
    # We want to find the smallest `k` numbers in the union of two arrays
    # We can distribute the `k` numbers into `nums1` and `nums2` where we select 
    
    # the first `k1` numbers in `nums1` and 
    # the first `k2` numbers in `nums2`, such that
    
    # `k = k1 + k2` and
    # `nums1[k1 - 1] < nums2[k2]`
    # `nums2[k2 - 1] < nums1[k1]`
    
    # * * * * nums1[k1 - 1] < nums1[k1]. . . . . . . . . . . . . 
    #
    # * * * * * * * nums2[k2 - 1] < nums2[k2] . .
    #
    # *: selected numbers
    #
    # The `k` th smallest number is the `max(nums1[k1], nums2[k2])`
    
    # We will use binary search to find `k1` and then `k2` would simply be `k - k1`
    
    
    
    # l = 0, when `nums2` can accomodate all `k` numbers 
    # nums1: . . . . . . . .   
    #
    # nums2: * * * * * * * * * * * * * * . . . . 
    # 
    # or l = k - len(nums2), when `nums1` gets some leftover
    #
    # nums1: * . . . . . . . 
    #
    # nums2: * * * * * * * * * * * * *
        
    # h = k, when `nums1` can accomodate all `k` numbers
    # nums1: * * * * * * * * * . . . . . . 
    #
    # nums2: . . . . . . . . . . . . 
    #
    # or h = len(nums1), when `nums2` gets some leftover
    #
    # nums1: * * * * * * * * 
    #
    # nums2: * . . . . . . . . . . . 
    if not nums1:
      return nums2[k - 1]
    elif not nums2:
      return nums1[k - 1]

    l = max(k - len(nums2), 0)
    h = min(k, len(nums1))
    # At any time
    # 0 <= l <= k1 <= h <= len(nums1)
    
    while True:
      k1 = (l + h) // 2
      k2 = k - k1
      
      l1 = nums1[k1 - 1] if k1 >= 1 else -sys.maxint
      h1 = nums1[k1] if k1 <= len(nums1) - 1 else sys.maxint
      l2 = nums2[k2 - 1] if k2 >= 1 else -sys.maxint
      h2 = nums2[k2] if k2 <= len(nums2) - 1 else sys.maxint
      
      if l1 <= h2 and l2 <= h1:
        return max(l1, l2)
      elif l1 <= h2 and l2 > h1:
        # `k1` is too small
        l = k1 + 1
      elif l1 > h2 and l2 <= h1:
        # `k1` is too large
        h = k1 - 1
      else: # l1 > h2 and l2 > h1:
        # `k1` is too large
        h = k1 - 1

"""120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
# Solution, DP
# time: O(n^2), space(n)
class Solution(object):
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    # The idea: straightforward to use DP
    #
    # prev row i:              0,  1,  2,  ..., i - 1
    # 
    # curr row i + 1:       0,   1,   2,  3,   i - 1,  i
    
    # Given array
    # `prev_min_sum`: sum of min-sum path to each element in prev row
    #
    # we fill array
    # `curr_min_sum`, holding sum of min-sum path to each element in curr row
    
    # For the first element `0`, there is only one path coming from `0` in prev row
    #
    # For the last element `i`, there is only one path coming from `i` - 1 in prev row
    #
    # For internal element, we have two paths `j` - 1 and `j`
    #                 
    #         ...  `j` - 1,    `j` ...
    #                       `j`
    #
    n = len(triangle)  
    # Base case:
    # `i` = 0: previous row has only one element
    prev_min_sum = [triangle[0][0]]
    
    for i in range(1, n):
      # `curr_min_sum` has the same length as the number of elements in
      # `triangle[i]`
      curr_min_sum = [0 for j in range(len(triangle[i]))]
      
      # traverse elements in current row
      for j in range(len(triangle[i])):
        # leftmost element
        if j == 0:
          curr_min_sum[j] = prev_min_sum[0] + triangle[i][0]
        # rightmost element
        elif j == len(triangle[i]) - 1:
          curr_min_sum[j] = prev_min_sum[-1] + triangle[i][-1]
        # internal element  
        else:  
          curr_min_sum[j] = min(prev_min_sum[j - 1], prev_min_sum[j]) + triangle[i][j]
      # current row becomes previous row in the next iteration     
      prev_min_sum = curr_min_sum    
    
    return min(prev_min_sum)      

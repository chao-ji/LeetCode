"""56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
class Solution(object):
  def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals:
      return []
    # We maintain a list of intervals `merged` that contains 
    # NON-OVERLAPPING and SORTED intervals.
    #
    # `merged`:
    # [-------, ------------, ------]
    #
    # The remaining intervals to be added are sorted by the starting coordinate
    
    # And the first interval to be added has starting index > the starting index
    # of the last interval in `merged`:
    #
    #           `i` > `i0`
    
    #   case 1: `i` <= `j0` 
    #
    #   --------------          <== `merged[-1]`
    #   i0           j0
    #
    #        -------------      <== interval to be added
    #        i           j
    #
    # We merged the two intervals with ending coordinate `max(j0, j)`
    
    #   case 2: `i` > `j0` 
    #   --------------          <== `merged[-1]`
    #   i0           j0                      
    #
    #                    ------ <== interval to be added
    #                    i    j    
    # We simple append the new interval, since it does not overlapping with `merged[-1]`
    
    # sort `intervals` in ascending order of lower bonds
    intervals = sorted(intervals, key=lambda interval: interval[0])
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
      # case 1: we update the end coordinate of `merged[-1]`
      if intervals[i][0] <= merged[-1][1]:     
        merged[-1][1] = max(intervals[i][1], merged[-1][1])
      # case 2:, we append the new interval, which is not overlapping 
      else:
        merged.append(intervals[i])
      
    return merged

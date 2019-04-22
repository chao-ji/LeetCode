"""57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
class Solution(object):
  def insert(self, intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    if not intervals:
      return [newInterval]
    
    # Because the intervals are sorted by the starting coordinate
    # 
    # We can use binary search to find the index at which to insert `newInterval`
    
    # Binary Search
    low, high = 0, len(intervals) - 1
    while low <= high:
      mid = (low + high) // 2
      if intervals[mid][0] == newInterval[0]:
        index = mid
        break
      elif intervals[mid][0] < newInterval[0]:
        low = mid + 1
      else:
        high = mid - 1
      index = low  

    # We created a new list `new_intervals` to hold the intervals in which the new 
    # interval is inserted.
      
    # when `index` == 0: 
    #
    # `newInterval` precedes all intervals in `intervals`
    #
    # so `new_intervals` contains only the `newInterval` 
    #
    # Let `new_intervals` = [++++++++++]              
    #                            ^
    #                            newInterval
    
    # when `index` > 0:
    #
    # -----, -----, ..., ----------*, *--------- ..., --------    <== `intervals`
    #                                ^
    #                    index - 1   index
    #
    # Let `new_intervals` = [-----, -----, ..., ----------*]
    #                                          
    # `intervals` = [++++++++++, *--------- ..., --------]

    # Note in either case
    
    # 1. the intervals in `new_intervals` are NON-OVERLAPPING and SORTED. 
    #
    # 2. the intervals in `intervals` are STILL sorted by the starting coordinate.
    
    if index == 0:
      new_intervals = [newInterval]
    else:
      new_intervals = intervals[:index]
      intervals = [newInterval] + intervals[index:]
      
    # The following use the same algorithm as LC56 Merge Intervals 
    for i in range(len(intervals)):
      if intervals[i][0] <= new_intervals[-1][1]:
        new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
      else:
        new_intervals.append(intervals[i])
        
    return new_intervals     

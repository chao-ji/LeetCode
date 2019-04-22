"""149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""
# Solution
# time O(n^2), space: O(n)
class Solution(object):
  def maxPoints(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if not points:
      return 0
    
    # number of maximum collinear points
    max_points = 0
    
    # Intuition:
    # 
    # ANY TWO distinct points are ALWAYS on the same line. Given two distinct
    # points (x1, y1), (x2, y2), we can easily tell if a third point (xi, yi)
    # is on the same line by computing if
    
    # (y1 - y2) / (x1 - x2) == (yi - y2) / (xi - x2),
    # or x1 == x2 == xi
    
    # Define D = {the maximum set of points that lie on the same line}
    
    # To find `D`, we start by picking a pivot point `p`, 
    #
    # Assuming `p` is in `D`,
    # we partition the remaining points `points` - {`p`} into disjoint groups,
    # where each group, together with `p`, are collinear:
    
    # `p`
    #
    # group1: {p_11, p_12, ..., p_1n1}
    # group2: {p_21, p_22, ..., p_2n2}
    # ...         ...
    # groupk: {p_k1, p_k2, ..., p_knk}
    
    # `points` = {`p`} + group1 + group2 + ... + groupk
    
    # If `p` is indeed in `D`, then
    #
    # `D` will be the largest group plus `p` itself. 
    
    # Otherwise, we pick a different point `q`, and repeat.
    #
    # Note we can exclude `p` from the remaining points of `q` -- because `p` has 
    # already been considered as being in `D`. 
    #
    # If `p` were in `D`, `D` would have been found.
    
    for i in range(len(points) - 1):
      # `i` is the pivot point

      # We use dict `collinear` to store the points other than `i` that are in 
      # different groups, where 
      
      # 1. the key is the slope between points `i` and point `j` 
      # 2. the value is the count of points `j` in each group (i.e. with the same slope)
      
      collinear = {}
      
      duplicates = 0  # count of points that are duplicates of point `i`
      count = 0       # size of the largest group
      x1, y1 = points[i]
      
      for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        
        if x1 == x2 and y1 == y2:
          duplicates += 1
          # if point `j` is a duplicate, we can safely skip it
          continue
        
        slope = None if x1 == x2 else 10.0 * (y2 - y1) / (x2 - x1)
        
        collinear[slope] = collinear.get(slope, 0) + 1
        # Each time we update a partition size, 
        # We also update maximum over all partitions:
        count = max(count, collinear[slope])
        
      # At this point, we have found the size of the largest group: `count`, given that 
      # point `i` is the pivot,
      # 
      # Now update `max_points` with `count` + the duplicate of point `i`
      max_points = max(max_points, count + duplicates)
    # return `max_points` plus the pivot itself 
    return max_points + 1

"""134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""
class Solution(object):
  def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    
    # The idea is simple: to be able to complete the circle, you must start somewhere and 
    # be able to reach your next gas station -- the gas left in the tank >= 0 -- until you
    # return to where you started
    
    # Say you start at gas station `i`, then the gas left in the tank at station `i` + 1 
    # would be `gas[i]` - `cost[i]`. If it's possible to get there at all, we must have
    # `gas[i]` - `cost[i]` >= 0
    #
    # So the gas left in the tank at any station is simple the cumulative sum of 
    # `gas[i]` - `cost[i]`
    
    # If you start at station `i`, and have your cumulative sum >= 0 until you get 
    # to station `j`, you can exclude `i` -- you can't even complete part of the circle
    # starting at station `i`
    # 
    # 
    # But you can exclude points in the range [i + 1, j - 1] as well -- the gas left 
    # in the tank would be even fewer if you start in the range [i + 1, j - 1]
    
    

    tank = 0
    next_start = 0
    for i in range(len(gas)):
      tank += (gas[i] - cost[i])
      # exclude points prior to `i` 
      if tank < 0:
        tank = 0
        next_start = i + 1
    
    # if all points in the range [0, len(gas) - 1] are excluded,
    # return -1
    if next_start >= len(gas):
      return -1
    
    # otherwise, we have manged to maitain the cumsum >= 0 until
    # station `len(gas) - 1`, starting at station `next_start`.
    #
    # ......*******
    #       ^
    # ^: `next_start`
    # *: reachable
    # .: yet to be reached
    #
    # Now we need to go back to station `0`, and see if we can reach
    # the starting station `next_start`.
    #
    # ......*******
    # >     ^
    # >: start from the beginning to see if we can complete the other
    # part of the circle
    for i in range(next_start):
      tank += (gas[i] - cost[i])
      if tank < 0:
        return -1
    
    return next_start
    

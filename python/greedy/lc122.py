"""122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# Solution 1, Greedy
class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0
    # The idea:
    
    # Since there is no limit on the number of transactions, we can buy the stock
    # at each index `i`, and sell it at the next index, as long as 
    # `prices[i + 1]` - `prices[i]` > 0 -- there is positive profit. 
    
    max_profit = 0
    for i in range(1, len(prices)):
      max_profit += max(prices[i] - prices[i - 1], 0)
      
    return max_profit         

# Solution 2, Peak and Valley
class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # The idea:
    
    # The only way that we can make maximum profit is that we identify those streaks
    # prices increases, or at least non-decreasing:
    
    #                                               .
    #                                             .      
    #                   .                       .
    #               .                         .
    #           .                           .
    #       .                             .
    #   .                     ...       .
    #   <----streak----->               <--streak--->
    
    # Our transaction would be pairs of valley and peak prices:
    # (valley_0, peak_0), (valley_1, peak_1), ...
    
    # Note these pairs can't overlap -- `peak_0` comes after `valley_0`, `valley_1`
    # comes after `peak_0`
    
    i = 0
    valley = peak = -1
    max_profit = 0
    
    # In each iteration, we identify the next pair of valley and peak
    
    while i < len(prices) - 1:
      # find valley index
      while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
        i += 1
      # at this point `i` == `len(prices)` - 1 or `prices[i]` < `prices[i + 1]`  
      valley = prices[i]
      
      # find peak index
      while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
        i += 1
      # at this point `i` == `len(prices)` - 1 or `prices[i]` > `prices[i + 1]`  
      peak = prices[i]
      
      max_profit += (peak - valley)
      
      # valley-peak pairs can't overlap, so we can simply keep incrementing `i`
      
    return max_profit     

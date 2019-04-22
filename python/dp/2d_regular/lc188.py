"""188. Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""
class Solution(object):
  def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    # the max num of transactions given `prices` of size `n` is
    # at most `n // 2` -- you must sell before buy again. If the num
    # of allowed transactions >= `n // 2`, then there is essentially
    # no limit on the num of transactions,  See LC122
    if k >= n // 2:   
      profit = 0
      for i in range(n - 1):
        profit += max(prices[i + 1] - prices[i], 0)
      return profit  
    
    # The idea: 
    # 
    # We want to maximize the profit on day `j`, 0 <= `j` <= `n` - 1
    #
    # Suppose we are allowed to complete up to `i` transcactions by day `j`
    #
    # Now we have two options:
    #
    # Option1: 
    #   You complete all your transactions BEFORE day `j` -- No selling on day `j`
    #     So your maximum profit is the same as day `j` - 1
    #
    # Option2:
    #   You complete your last transaction on day `j` -- you buy stock on, say,
    #     day `p`, before day `j` and sell on day `j`.  `p` < `j`
    #     So your maximum profix = 
    #
    #         the maximum profix on day `p` + (prices[j] - prices[p])
    #
    #   In this case, you would need to find out which `p` would result in the 
    #   maximum profix
    
    
    # Base cases:
    #
    # when `i`, the maximum number of transactions is 0, 
    #     the profit is always zero -- you can't perform any transactions
    # when `j`, the day by which you complete all your transactions is 0,
    #     the profix is always zero -- you have to both buy and sell on day 0
    #
    
    #       0     1     2     3     4     5     j: daily price
    #
    #   0   0     0     0     0     0     0
    #
    #   1   0
    #
    #   2   0     *     *     *          
    #
    #   3   0                 i,j-1 i,j
    #
    #   4   0
    #
    #   5   0
    #
    #   i:  max number of transactions
    
    # `dp[i][j]` is maximum profit 
    #     when completing at most `i` transactions by day `j`
    # `i` = 0, 1, 2, ..., k           `j` = 0, 1, 2, ..., n - 1     
    
    # Note when computing `dp[i][j]`
    #
    # For option 1, we always have `dp[i][j]` == `d[i][j - 1]`
    #
    # For option 2, we always sell stock on day `j`, so we need to find
    #
    #     dp[i - 1][0] - prices[0] + prices[j]:           buy on day 0
    #     dp[i - 1][1] - prices[1] + prices[j]:           buy on day 1
    #                       ...
    #     dp[i - 1][j - 1] - prices[j - 1] + prices[j]:   buy on day `j` - 1
    
    dp = [[0 for j in range(n)] for i in range(k + 1)]
    for i in range(1, k + 1):
      # In the inner for-loop, as we increment the looping variable `j`, 
      # we keep track of the maximum of 
      #   `dp[i - 1][0] - prices[0]`, ..., `dp[i - 1][j - 1] - prices[j - 1]`
      one_less_transaction = dp[i - 1][0] - prices[0]
      for j in range(1, n):
        one_less_transaction = max(one_less_transaction, dp[i - 1][j - 1] - prices[j - 1])
        dp[i][j] = max(one_less_transaction + prices[j], # option2 
                       dp[i][j - 1]) # option 1: complete all transactions by day `j` - 1
    return dp[k][n - 1]    
        
        

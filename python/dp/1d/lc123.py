"""123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

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
class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0
    
    n = len(prices)
    max_profit = 0
    
    # The idea:
    #
    # We are allowed to complete at most TWO non-overlapping transactions.
    #
    # In the first pass, we scan the `prices` from left to right, use an 
    # array to record the maximum profit with one transaction completed by far.
    #
    # and compute the max profit with ONE transaction by day `i` for each `i`.
    
    # In the second pass, we scan the `prices` from right to left. We keep
    # track of max price seen so far (i.e. `max_price`), and we always 
    # buy on day `i` (current index) and sell with price `max_price`, and 
    #
    # we combine this with the profit `p[i]` made in the first pass.
    
    
    #     .     .     .     .     .     .     .     .       .     .     .     .
    #     <-- max profit w/ 1 trans by day `i` ----->                   ^
    #                                               p[i]                max_price
    #                                               i                 
    #
    # profit = p[i] - prices[i] + max_price
    #
    # Do linear search to find which `i` results in max profit
    

    
    min_price = prices[0]
    # `profit[i]`: max profix with one transaction completed by day `i`
    # `i` = 0, 1, 2, ..., `n` - 1
    profit = [0 for i in range(n)]
    
    # first pass
    for i in range(1, n):
      min_price = min(min_price, prices[i])
      # `min_price`: minimum price seen so far
      profit[i] = max(
        # option1: transaction completed before day `i` 
        profit[i - 1], 
        # option2: transaction completed on day `i`, i.e., sell on day `i`
        prices[i] - min_price)  
    
    # second pass
    max_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
      # `max_price`: max price seen so far, in backward direction
      max_price = max(max_price, prices[i])
      max_profit = max(max_profit,
                       (max_price - prices[i] + # second transaction 
                        profit[i]               # first transaction
                       ))
      
    return max_profit  

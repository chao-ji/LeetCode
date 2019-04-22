"""121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

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
    # The idea: The naive solution would be enumerating the pairs of buying
    # and selling prices: `prices[i]` and `prices[j]`, 0 <=i < j <= n - 1
    # and find the maximum of `prices[j]` - `prices[i]` 
    
    #
    # We can define a set of subproblems parameterized by each index `i`
    # 0 <= i <= n - 1
    
    # subproblem[i] = max profix with one transaction in which you must sell on
    # day `i`
    
    # Since we MUST SELL at index `i`, to compute `subproblem[i]`, we must keep
    # track of the minimum price up until index `i`
    
    if not prices:
      return 0
    
    # `low` keeps track of the minimum value up to the current index `i`, 
    # initialized to the first price `prices[0]`
    low = prices[0]
    
    # `max_profix` is the global max profit achievable when selling at ANY index
    max_profit = 0
    for i in range(1, len(prices)):
      # maintain the loop invariant that `low` is always the minimum value 
      # up to the current index `i`
      low = min(low, prices[i])
      
      max_profit = max(max_profit, 
                       prices[i] - low  # the solution to `subproblem[i]`
                                        # must sell at index `i`
                      )
      
    return max_profit          

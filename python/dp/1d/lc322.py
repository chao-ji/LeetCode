"""322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
# Solution, DP
# time: O(n*k), space: O(n), `n`: target amount, `k` number of coins
class Solution(object):
  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount == 0:
      return 0
    
    # Since there is no limit on the number of coins, we don't need to
    # keep track of the number of coins used so far, just focus on the
    # target AMOUNT.
    
    
    # 0       1    ...  i-k  ...      i-3     i-2     i-1     i                 
    # .       .                       .       .       .       .  
    #                                         <--- denom=2 --->
    # 
    #                               ...     ...
    #
    #                   <------------- denom=k --------------->

    
    # `dp[i]` = the minimum number of coins need to the make change for
    # target amount `i`,  0 <= i <= `amount`
    
    # `dp[i]` is like the number of "jumps" to get from 0 to `i`, where
    # the "length" of each jump must be a coin denomination.
    
    # Given target amount `i`, 
    #
    # We need to find which coin denomination `k` results in the minimim
    # number of coins: 
    # 
    # which `k` minimizes `dp[dp[i] - k]`
    
    dp = [-1 for i in range(amount + 1)]
    dp[0] = 0
    
    for i in range(1, amount + 1):
      dp[i] = float('inf')
      # `flag`: whether is possible to make change for `i`
      flag = False
      
      for j in range(len(coins)):
        if (i >= coins[j] and         # coin denomination <= target amount `i`
            dp[i - coins[j]] >= 0):   # it's possible to make change for 
                                      # `i - coins[j]`
          dp[i] = min(dp[i], dp[i - coins[j]] + 1)
          flag = True
      
      # if not possible to make change from `i`
      if not flag:
        dp[i] = -1
    return dp[-1]    
    

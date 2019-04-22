"""96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution(object):
  def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    # The idea:
    
    # We always have to put 1 node at the root, and then we're left
    # with `n` - 1 nodes.
    
    # We can choose to put 0, 1, ..., up to `n` - 1 nodes in the left 
    # subtree, and put the remaining nodes in the right subtree.
    
    # `dp[i]` = number unique trees with `i` nodes, 0 <= i <= n,
    # 
    # We have overlapping subproblems, so use `dp` to keep track of 
    # solutions to subproblems

    dp = [0 for _ in range(n + 1)]
    dp[0] = dp[1] = 1
 
    for i in range(2, n + 1):
      # `j` = 0, 1, ... i - 1,  num of nodes in the left subtree
      # `i` - ` - `j`           num of nodes in the right subtree
      for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j]
        
    return dp[n]    

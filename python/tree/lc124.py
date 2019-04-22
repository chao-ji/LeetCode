"""124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # Intuition:
    
    # RECURSION should be the first choice for tree related problems
    
    # For each node, we need to compute the max-sum path that go through
    # each node, which is the following with maximum sum: 
    # 1. the node itself, 
    # 2. node extended to somewhere in the left subtree,
    # 3. node extended to somewhere in the right subtree,
    # 4. node extended in both directions into left and right subtree.
    
    
    # By definition, the max-sum path may be
    #   1.  completely in the left subtree
    #   2.  completely in the right subtree
    #   3.  go through the root 
    
    # Suppose we are at a non-empty node `node`, and if we let the 
    # recursive function return the max-sum path ANYWHERE within 
    # the tree rooted at `node`
    
    # it would be difficult to handle the third case:
    #
    # The max-sum path may be the one that go through the node `node`.
    #
    #                     10 <- node
    #                    /  \
    #                   2    10
    #                  / \    \
    #                20   1   -25
    #                         /  \
    #                        3    4
    
    # The recursive call on left subtree returns 23 (20+2+1)
    # The recursive call on right subtree returns 10 (10)
    #
    # However, the max-sum path is 20-2-10-10, where sum is 42
    
    
    
    
    # So it would make sense to put some CONSTRAINT on what the recursive
    # function should return:
    
    # We ask the recursive function to return the max-sum path that START
    # (or END, since the path is undirected) at the node `node`:
    
    """
    def func(node):
      # returns the max-sum path that starts at `node`
    
      if left subtree is non-empty:
        left = func(node.left)
      else:
        left = 0
      `left`: sum of max-sum path starting or ending at `root.left`
    
      if right subtree is non-empty:
        right = func(node.right)
      else:
        right = 0
      `right`: sum of max-sum path starting or ending at `root.right`  
    
      # Note that this point, we have everything we need to compute the
      # sum of max-sum path STARING at `node`, it must be the max of
      
      # 1. the node itself, node.val
      # 2. the node extended somewhere in the left subtree, node.val + left
      # 3. the node extended somewhere in the right subtree, node.val + right
      
      # However, the above happen to be enough to compute the max-sum path that
      # GO THROUGH the node `node`, it must be the max of 1, 2, 3, and
      
      # 4. the node extended in both directions, node.val + left + right
      
      # Before we return, we update the max of 1, 2, 3, 4 with a global variable 
      # `max_sum` that stores the max-sum path any there in the three:
      
      # max_sum = max(max_sum, max of 1, 2, 3, 4)
    
    return max(node.val, node.val + left, node.val + right) 
    """
    if not root:
      return 0
    
    max_sum = [-float("inf")]
    self.maxPathSumRoot(root, max_sum)
    return max_sum[0]    
    
  def maxPathSumRoot(self, root, max_sum):
    if root.left:
      left = self.maxPathSumRoot(root.left, max_sum)
    else:
      left = 0
      
    if root.right:
      right = self.maxPathSumRoot(root.right, max_sum)
    else:
      right = 0
    
    start_at_root = max(root.val, root.val + max(left, right))
    max_sum[0] = max(max_sum[0], max(start_at_root, root.val + left + right))
    
    return start_at_root

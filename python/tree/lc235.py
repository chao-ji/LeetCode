"""235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""
# Solution 1, Recursive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # The idea:
    #   We can take advantage of the properties of BST to
    #   navigate our search
    
    # Given root node `root`, the recursive function will return
    # 1. None, if neither of `p` nor `q` is present in the tree rooted at `root`
    # 2. `p` or `q` if `root` == `p` or `q`, which is also the LCA if both of
    #   them are present in the tree rooted at `root`
    # 3. LCA of `p` and `q`
    
    # Base case: case 1 and case 2
    if root is None or root == p or root == q:
      return root
    
    # if both `p` and `q` hold values < `root.val`, we can navigate to
    #   the left tree
    if p.val < root.val and q.val < root.val:
      return self.lowestCommonAncestor(root.left, p, q)
    # if both `p` and `q` hold values > `root.val`, we can navigate to
    #   the right tree
    elif p.val > root.val and q.val > root.val:
      return self.lowestCommonAncestor(root.right, p, q)
    
    # `p` and `q` are distributed in different subtrees of `root`, then
    # `root` must be the LCA
    return root   

# Solution 2, iterative
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root:
      return root
    # The idea:
    # 
    # We use the same strategy as the recursive solution.
    # but instead of recur to one of the the subtrees using the BST property,
    # we iteratively move `node` to one of its child.  
    
    node = root
    
    while node:
      if (node == p or node == q or 
          p.val < node.val < q.val or 
          q.val < node.val < p.val):
        return node
      
      if p.val < node.val and q.val < node.val:
        node = node.left
      else:
        node = node.right 

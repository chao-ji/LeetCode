"""236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

                3
              /   \
            5       1
          /  \    /   \
         6    2  0     8
             / \
            7   4
 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
# Solution 1, Recursive
# find the presence of either or both `p` and `q`

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
    # The idea: use the definition of Common Ancestor
    
    # Note the root node will always be the common ancestor of `p` and `q`.
    # However, it may not be the lowest when both `p` and `q` are in the same
    # subtree of root:
    
    #             root                       root
    #            /    \                     /    \
    #         l_tree  r_tree    or      l_tree   r_tree
    #         |p,q |                             |p,q |
    
    # So the problem is reduced to find the presence of `p` and/or `q` in 
    # the left subtree and in the right subtree.
    
    # Given a root node `root`,
    # the recursive function returns the following:
    
    # 1. None, if neither `p` nor `q` is present in the tree rooted at `root`.
    # 2. `p` or `q` if either of them is found in the tree rooted at `root`. 
    #   Note: if both nodes are in this tree, then `p`(or `q`) must also be
    #   the LCA of `p` and `q`.
    
    # 3. LCA of `p` and `q` if both of them are present in the tree
    
    
    
    # Base case: 
    # 1. root is None, we have empty tree, `p` and `q` can't be present in
    #   empty tree
    # 2. root is either `p` or `q`, we have found the LCA of `p` and `q`
    # 
    if root is None or root == p or root == q:
      return root
    
    # we recur to the left subtree
    left = self.lowestCommonAncestor(root.left, p, q)
    # we recur to the right subtree
    right = self.lowestCommonAncestor(root.right, p, q)

    # `right` is None, then LCA must be `left`
    if left is not None and right is None:
      return left
    # `left` is None, then LCA must be `right`
    elif left is None and right is not None:
      return right
    # both `left` and `right` are None, then neither `p` nor `q` is present in the tree 
    elif left is None and right is None:
      return None
    
    # both `left` and `right` are not None, then `p` and `q` must be distributed in
    # different subrees of `root`, so `root` must be the LCA
    return root
    
    



# Solution 2, Recursive
# find the root-to-node paths

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
    # The idea: find the root-to-node paths
    
    # Suppose we have the paths from the root to the given nodes
    # root, ..., p
    # root, ..., q
    
    # Then by definition, the LCA would be the last node the the common prefix
    # of the two paths.
    
    # All we need to to is to find the paths from the root to given node:
  
    # It's straightforward to use backtrack to find the LCA.
    final_paths = []
    self.findPath(p, [root], final_paths)
    self.findPath(q, [root], final_paths)
    
    # Reverse the paths, and return the first node 
    # where the two paths agree
    for n1, n2 in reversed(zip(*final_paths)):
      if n1 == n2:
        return n1
  
  def findPath(self, node, path, final_path):
    if path[-1] != node:
      if path[-1].left:
        path.append(path[-1].left)
        self.findPath(node, path, final_path)
        path.pop()
      
      if path[-1].right:
        path.append(path[-1].right)
        self.findPath(node, path, final_path)
        path.pop()
      
      # BACKTRACK
      return 
    
    # BACKTRACK
    final_path.append(list(path))
      
      
      
      

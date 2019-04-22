"""94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    inorder, stack = [], []
    node = root
    
    # The idea:
    
    # The first node to be visited is the last node in the ALL-LEFT path
    # starting from the root. 
    
    # So we need to go all the way to the left child of each node. As we move,
    # we must also keep track of the nodes along the path, by pushing them to
    # the stack
    
    # As long as we hit a None in the all-left path, we know there is no left
    # subtree for the parent node, so we rely on the stack that we maintained,
    # we pop the stack, which must be a node without left child, so we visit it,
    # and move to its right child. 
    
    while node or stack:
      if node:
        stack.append(node)
        node = node.left
      else:
        node = stack.pop()
        inorder.append(node.val)
        node = node.right
    return inorder    
        

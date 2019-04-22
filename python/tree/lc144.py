"""144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
      return []
    # The idea:
    
    # Iterative preorder traversal is the EASIEST to think about among 
    # all three traversal orders:
    
    # After we visit the root node, we need to traverse the left subtree in preorder,
    # and then traverse the right subtree in preorder.
    
    # To traverse a tree in preoder, we need to keep track of its root node.
    
    # We push the right child, then the left child onto the stack, and we
    # maintain the LOOP INVARIANT:
    
    # Nodes in the tree rooted at the node, which is at the top of the stack will 
    # always be visited before those in the tree rooted at node below
    # the top of the stack.
    
    stack = [root]
    preorder = []
    
    while stack:
      # At the beginning of each loop,
      # subtree rooted at `node` has never been explored before,
      # we will first need to visit the node at the root, then explore the 
      # left tree, then right tree 
      #
      # To do so, we first push the right child (if not empty), followed by
      # left child (if not empty). This way we guarantee that all nodes in
      # the left subtree are visited before we move to the right subtree.
      node = stack.pop()
      preorder.append(node.val)
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)
        
    return preorder    

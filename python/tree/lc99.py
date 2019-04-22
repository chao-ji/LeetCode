"""99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

# Solution 1
# Use array to store inorder traversal, then find the first and second node to swap values
# Space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def recoverTree(self, root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    nodes = self.inorder(root)

    first, second = None, None
    for i in range(len(nodes) - 1):
      if nodes[i + 1].val < nodes[i].val:
        first = nodes[i]
        break
    for i in range(len(nodes) - 1, 0, -1):
      if nodes[i - 1].val > nodes[i].val:
        second = nodes[i]
        break

    swap = first.val
    first.val = second.val
    second.val = swap
        
  def inorder(self, root):
    if not root:
      return []
    
    nodes = []
    nodes.extend(self.inorder(root.left))
    nodes.append(root)
    nodes.extend(self.inorder(root.right))
    return nodes

# Solution 2
# detect 1 or 2 inversions as we do in-order traversal
# Space O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def recoverTree(self, root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    # Intuition: do an in-order traversal, and look for inversions
    
    # a valid BST would produce strictly increasing sequence if
    # traversed in-order:
        
    #                         .
    #                     .
    #                 .
    #             .
    #         .
    #     .
    
    # If two nodes are swapped, we may have one inversion
    
    #                         .
    #                     .
    #             .
    #                 .
    #         .
    #     . 
    #             ^   ^
    #             nodes to be swapped
    #
    # When the swapped values are next to each other in the in-order sequence
    
    # Or we may have two inversions
    #             .            
    #                     .
    #                 .
    #                         .    
    #         .
    #     . 
    #             ^           ^  
    #             nodes to be swapped
    #
    # When the swapped values are not next to each other in the in-order sequence
    
    # As we can see,
    # in either case, whenever we see the first inversion: 
    #       last value > current value
    # 
    # The "last value" is always one of the nodes to be swapped, and the 
    # "current value" MAY (or may not) be the other node to be swapped.
    
    # We may or may not see the second inversion. But if we DO see the second 
    # inversion: last value > current value
    #
    # The "current value" will be the second node to be swapped.
    
    # `nodes[0]`: the last value
    # `nodes[1]`: the first node to be swapped
    # `nodes[2]`: the second node to be swapped
    nodes = [None, None, None]
    self.inorder(root, nodes)

    swap = nodes[1].val
    nodes[1].val = nodes[2].val
    nodes[2].val = swap
    
  def inorder(self, root, nodes):
    if not root:
      return 
    
    self.inorder(root.left, nodes)

    if nodes[0]:
      if root.val < nodes[0].val:
        if not nodes[1]:
          nodes[1] = nodes[0]
          nodes[2] = root
        else: 
          nodes[2] = root
    
    nodes[0] = root
    
    self.inorder(root.right, nodes)

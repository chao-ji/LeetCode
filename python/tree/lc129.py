"""129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""
# Solution 1, Recusion preorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    #     4
    #    / \
    #   9   0
    #  / \
    # 5   1
    
    # Intuition:
    
    # We want to find all the root-to-leaf paths:
    
    # Here we have three paths:
    # 4->9->5,    495
    # 4->9->1,    491
    # 4->0,       40
    # and compute the sum of the numbers represented by the paths
    
    # We could naively solve the problem by enumerating all the root-to-leaf
    # paths using tree traversal and then take the sum. However, this would 
    # require us to store some nodes repeatedly -- 4 and 9 are shared between
    # the paths: 4->9->5, 4->9->1, which may not be good enough.
    
    
    
    # Suppose we are at some non-empty node `node`, and we want to find the sum of 
    # all root-to-leaf paths that GO THROUGH this node `node`. They can be divided 
    # into those with leaf node in the left subtree and those with leaf node in the
    # right subtree:
    
    # So what we want is 
    
    # sum({root-> ... ->node --> left paths}) + sum({root-> ... ->node --> right paths})
    
    #                     left paths
    #                   /
    # root-> ... ->node
    #                   \ 
    #                     right paths
    
    # Of course, the left and right subtree might be empty (i.e. None), in this case
    # we would have to compute one of the two sums. In case both of them are empty, then
    # `node` itself is a leaf node, so we only need to compute the number represented by
    # the path: root-> ... ->node. But this number should have been computed BEFORE we arrive
    # at this node `node`
    
    
    
    
    # Given non-empty node `node`, and the number `val` represented by the path 
    # root-> ... ->node. We want to compute the sum of all the root-to-leaf paths
    # that GO THROUGH `node`.
    
    # Here is the recursion
    
    # if node.left is not None:
    #   left_val = func(node.left, val*10 + node.left.val)
    # else:
    #   left_val = 0
    # if node.right is not None:
    #   right_val = func(node.right, val*10 + node.right.val)
    # else:
    #   right_val = 0
    #
    # If both node.left and node.right are empty, then all we need to do is to
    # return val, because `node` itself is leaf node, and there is only one path.
    
    
    if not root:
      return 0
    
    return self.recursion(root, root.val)
    
  def recursion(self, node, val):
    """
    Args:
      node: the node (non-empty) we are at
      val: the number represented by the root-to-`node` path. Including this node
  
    Returns the sum of all root-to-leaf paths that GO THROUGH `node`.
    """
    
    # Base case: `node` itself is leaf node
    if not node.left and not node.right:
      return val
    
    if node.left:
      left_val = self.recursion(node.left, val * 10 + node.left.val)
    else:
      left_val = 0
    
    if node.right:
      right_val = self.recursion(node.right, val * 10 + node.right.val)
    else:
      right_val = 0
   
    return left_val + right_val


# Solution 2, 
# naively enumerating all root-to-leaf paths, and take the sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return 0
    
    nums = self.listOfNums(root)
    sum_nums = 0
    for n in nums:
      sum_nums += int(n)
    return sum_nums  
    
  def listOfNums(self, root):  
    if not root.left and not root.right:
      return [str(root.val)]
    
    left = None
    if root.left is not None:
      left = self.listOfNums(root.left)
      left = [str(root.val) + s for s in left]
        
    right = None    
    if root.right is not None:
      right = self.listOfNums(root.right)
      right = [str(root.val) + s for s in right]
      
    if left and right:
      return left + right
    if left and not right:
      return left
    if not left and right:
      return right
    return []

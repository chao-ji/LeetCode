"""116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example:
    1
   / \
  2   3
 / \ / \
4  5 6  7

output
    1->None
   / \
  2-->3->None
 / \ / \
4->5>6->7->None


Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
"""

# Solution, recursive
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
  def connect(self, root):
    """
    :type root: Node
    :rtype: Node
    """
    if not root:
      return None
    
    # Intuition: use RECURSION
    
    # If `root` is empty, return None
    
    # Otherwise, since the tree rooted at `root` is a complete binary tree,
    
    #                root
    #               /    \
    #          l_tree     r_tree
    
    # the left subtree and right subtree are structurally identical
    
    # We recursively call the function on `root.left` and `root.right`, then
    # nodes in both subtrees would have their `next` pointers populated.
    
    # All we need to do is to set the `next` pointers in the all-right path 
    # in the left subtree to the corresponding nodes in the all-left path in
    # the right subtree.
    
    # We place two pointers `p` and `q` at the left child and right child, and
    # move them along the all-right and all-left paths:
    
    
    #                       root
    #                      /     \
    #                     p       q
    #                   /-->\   /-->\  
    #                  .---->. .---->.
    
    # After adding `next` pointers using `p` and `q`:
    
    #                       root
    #                      /     \
    #                     p------>q
    #                   /-->\-->/-->\  
    #                  .---->.>.---->.
    
    
    _ = self.connect(root.left)
    _ = self.connect(root.right)
    p, q = root.left, root.right
    while p and q:
      p.next = q
      p = p.right
      q = q.left
      
    return root  
      

"""117. Populating Next Right Pointers in Each Node II

[200~Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

      1
     / \
    2   3
   / \   \
  4   5   7

output

      1
     / \
    2-->3
   / \   \
  4-->5-->7
"""

# Solution 1
# Implicit level order traversal
# using O(1) memory
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
    # Intuition: Use level order traversal
    #
    
    # Because the binary tree is not necessarily complete, we can't use
    # the recursive approach as in LC 116
    
    #                         1
    #                      /     \
    #                     2       3
    #                   /   \      \  
    #                  4     5      7      
    #                 /             /
    #                8              9
    
    # The all-right path in the left subtree ends at 5, so the `next` pointer
    # of 8 can't be properly set.
    
    
    
    
    # We take a different approach:
    # If we list the nodes in level-order traversal, we have
    
    #     [1]
    #     [2, 3]
    #     [4, 5, 7]
    #     [8, 9]
    
    # We can see that the `next` pointer should be set to the immediate successor:
    #    
    #     [1]
    #     [2->3]
    #     [4->5->7]
    #     [8->9]
    
    
    
    
    # We start by placing a pointer `curr_level_node` at root node, i.e.
    # the first node of the first level. 

    # And we create a dummy node `next_level_head`, and use a second pointer
    # `next_level_node` to add the `next` connections in the next level.
    
    
    
    #  curr_level_node ---------> 1                     current level
    #                          /     \ 
    # [next_level_head]       2       3                 next level
    #         ^             /   \      \  
    #   next_level_node    4     5      7      
    #                     /             /
    #                    8              9
    
    
    
    # At the start of each iteration, we maintain the loop invariant that 
    
    # 1. `curr_level_node` points to the first node of the current level, 
    # 2. the current level's `next` pointers have already been set, so you can
    #     move `curr_level_node` to its next node `curr_level_node.next`.
    #
    # 3. `next_level_node` points to the dummy node `next_level_head`
    
    #                               [ ]
    #                                ^
    #                         curr_level_node          
    #                          /           \
    #           [ ]          left           right
    #            ^
    #     next_level_node
    
    # If `curr_level_node` has a left child, we connect `next_level_node.next` to 
    # `curr_level_node.left`, and move `next_level_node` to its next node:
    
    #                               [ ]
    #                                ^
    #                         curr_level_node          
    #                          /           \
    #           [ ]--------->left           right
    #                         ^
    #                   next_level_node
    
    # Similarly, if `curr_level_node` has a right child, we have
    
    #                               [ ]
    #                                ^
    #                         curr_level_node          
    #                          /           \
    #           [ ]--------->left-------->right
    #                                       ^
    #                                 next_level_node
    
    # Then we move `curr_level_node` to its next node, until it reaches the end
    # of the current level. 
    
    # Finally we restore `curr_level_node` to `next_level_head.next`: 
    
    #                               [ ]
    #
    #
    #                          /           \
    #           [ ]--------->left-------->right
    #            ^             ^               
    #     next_level_head   curr_level_node
    
    curr_level_node = root
    while curr_level_node:
      # create the dummy node
      next_level_head = Node(-1, None, None, None)
      # `next_level_node` initially points to the dummy node
      next_level_node = next_level_head
      
      while curr_level_node:
        # Add `next` pointers in the next level
        if curr_level_node.left:
          next_level_node.next = curr_level_node.left
          next_level_node = next_level_node.next
        if curr_level_node.right:
          next_level_node.next = curr_level_node.right
          next_level_node = next_level_node.next
          
        # `next` pointers in current level have already been set, so we can
        # move `curr_level_node` to the next node
        curr_level_node = curr_level_node.next
        
      # Now "next level" becomes "current level", 
      # restore `curr_level_node` using the dummy node `next_level_head`
      curr_level_node = next_level_head.next
      del next_level_head
    return root  
       
# Solution 2 
# Explicit level order traversal
# using extra memory
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

    level = [root]
    next_level = []
    while level:
      for i in range(len(level) - 1):
        level[i].next = level[i + 1]

      for node in level:
        if node.left:
          next_level.append(node.left)
        if node.right:
          next_level.append(node.right)

      level = next_level
      next_level = []

    return root
 

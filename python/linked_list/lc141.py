"""141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # KEY Idea:
    
    # Place two pointers `p` and `q` at the head of the linked list.
    # Move `p` twice as fast as `q`. If `p` eventually reaches `None`,
    # then there is no cycle. 
        
    # However, if there is indeed a cycle, the fast pointer `p` would 
    # revisit some node for the SECOND TIME. 
    
    # The slow pointer `q` would also reach this node eventually.  
    # From that point on, the distance between `p` and `q` would DECREASE 
    # by one in each iteration, until `p` eventually overtakes `q`.

    p = q = head
    
    # proceed as long as `p` is not None
    while p:
      # step both `p` and `q`
      p = p.next
      q = q.next
      
      # step `p` again, so it moves twice as fast
      if p:
        p = p.next
        
        # after `q` moves one step, and `p` moves two steps 
        # detect if they meet as the same node
        if p == q:
          return True
        
    return False    

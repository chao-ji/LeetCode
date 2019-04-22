"""142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # explanation 
    # https://leetcode.com/problems/linked-list-cycle-ii/discuss/249727/Python-Two(Three)-Pointers
    if not head:
      return None
    
        
    # util the fast pointer `p` reaches the first node of the cycle for the
    # second time
    
    
    # -----l------+-------------+
    # ^           |             |
    # head        |             |
    #             |            p.q
    #             |             |
    #             |             |
    #             +------c------+
    
    # Suppose `l` >= 0 is the number of nodes outside of the cycle, and
    # `c` >= 1 is the number of nodes inside the cycle.
    
    # By LC 141, `p` and `q` would eventually meet somewhere inside the 
    # cycle. Say, it's the `d` th node from the start of the cycle. 
    # Here 0 <= d < c
    
    # Then it would take the slow pointer `l` + `d` steps to get there, 
    # in which `d` steps were traveled within the cycle.
    
    # Accordingly, it would take the fast pointer `2(l + d)` steps to get
    # there, in which `2(l + d) - l` steps were traveled within the cycle
    
    # Since they meet at the `d` th node in the cycel, we must have
    #
    # d = (2(l + d) - l) % c
    #
    # which means:
    #
    # 2(l + d) - l = c * k + d,  for some k >= 1
    #
    # So
    #
    # d = c * k - l
    
    # If we place the slow pointer back to `head`, start of the linked list,
    # and keep the fater pointer where it is, and let them move the the same
    # speed, 
    
    # It would take the slow pointer `l` steps to get to the start of the 
    # cycle;
    # The fast pointer must have traveled the same distance, which is `l` steps
    # from the `d` th node in the cycle, which is `l + d` th node in the cycle
    
    # Because `l + d` = `c * k`, after traveling `l` steps, the faster pointer
    # must be at the 0 th node from the start of the cycle, which is where they
    # meet.
    
    
    p = q = head
    while p:
      p = p.next
      q = q.next
      if p:
        p = p.next
        if p == q:
          break
    
    # If `p` is None, then there is no cycle
    if not p:
      return None
    
    # move `q` back to the start
    q = head
    # move `p` and `q` at the same speed
    while q != p:
      p = p.next
      q = q.next
      
    return q  

"""92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseBetween(self, head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    # KEY Insight:
    #
    # To handle corner cases: place a dummy node that points to the head
    # of list
    
    #  [] ========> [] ====> ... ====> []
    #  dummy        head
    #  p
    #  q
    
    # Since 1 <= m <= n <= length of list
    #
    # First we move `p` to point to `m` - 1, move `q` to point to `n`:
    # and `r` points to `q.next`
    
    # We reset `q.next` to None, to disconnect from the remaining of linked list
    
    # Then we do reverse(p.next), and set `p.next` = `reverse(p.next)`
    
    # Finally, we move `p` to the end of `reversed(p.next)`, and set `p.next` = r,
    # i.e. the remaining of list (could be None).
    
    # [] ======> [] ==> ... => [] => [] ===> ... ===> [] ===> some node of None
    # dummy      head          m-1   m                n
    #                                |                |
    #                          p     |                q       r
    #                                <================>
    #                                  to be reversed
    p = q = dummy = ListNode(0)
    dummy.next = head
    
    for _ in range(m - 1):
      p = p.next
      
    for _ in range(n):
      q = q.next
      
    r = q.next
    q.next = None
    
    p.next = self.reverse(p.next)
  
    while p.next:
      p = p.next
    p.next = r  
    
    return dummy.next
  
  def reverse(self, head):
    if not head or not head.next:
      return head
    
    prev = None
    curr = head
    next = head.next
    
    while curr.next:
      curr.next = prev
      prev = curr
      curr = next
      next = next.next
      
    curr.next = prev    
    
    return curr

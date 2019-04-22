"""25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    # Nothing needs to be done if length of list <= 1
    if not head or not head:
      return head
    
    # KEY Insight:
    # Use recursion
    
    # Intuition
    
    # We have a linked list that can be partitioned into a number of k-groups
    # The last group has k' nodes where k' is `list_len % k`, i.e. < k
    
    # We can find the first k nodes and then recursively reverse the remaining part
    # in k-groups: 
    
    # <== k ==> | <== k ==> ... <== k ==> <== k' ==>
    #
    # < left  >   <             right              >
    
    # turns to 
    
    # <= rev => | <= rev => ... <= rev => <== k' ==> 
    
    # Base case:
    #
    # First, we need to check if length of the linked list >= `k`.
    # We should be able to move a pointer `curr` from `head` exactly `k` - 1 steps, 
    # without being terminated by `None`, if length of list >= `k`:
    #
    # [0], ..., [k - 1]
    #
    # head      curr
    #
    # Whenever the remaining linked list has < `k` nodes, i.e. the last k'-group 
    # we should return the linked list unchanged. 
    
    # Recurrence:
    #
    # If linked list has > k nodes, first reverse the left part, then recursively 
    # reverse the right part in k-groups:
    
    # [0], ..., [k - 1], [k], ...,   [list_len - 1]
    #
    # head      curr     curr.next
    #
    # <---- left ----->  <------- right ---------->
    
    # <-reversed left->  <-k-group reversed right >
    
    # Base case
    curr = head
    for i in range(k - 1):
      curr = curr.next
      # We got terminated by `None`, which means length of list < `k`,
      # return linked list unchanged
      if not curr:
        return head
    
    
    right = self.reverseKGroup(curr.next, k)
    # then disconnect `curr` from the right part
    curr.next = None

    # Note: when reversing the left part:
    #
    # [0], ..., [k - 1],
    # head      
    
    # `head` becomes the tail:
    
    # [k - 1], ..., [0],
    # left          head
    left = self.reverse(head)

    # We connects the left and right part, by setting `head.next`
    head.next = right
    return left
  
  def reverse(self, head):
    if not head or not head.next:
      return head
    
    prev = None
    curr = head
    next = curr.next
    
    while curr.next:
      curr.next = prev
      prev = curr
      curr = next
      next = next.next
      
    curr.next = prev
    return curr

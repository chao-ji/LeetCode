"""86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    ##############
    # KEY Insight:
    # Use two pointers `lt` and `ge`, initially pointing to dummy nodes
    
    # Get another pointer `node`, initially pointing to `head` of linked list
        
    # initially, input linked list:
    # [] =====> [] ======> ... =======> []
    # head
    # node
    
    # disconnect `node` from the remaining of linked list:
    #
    # [] =====> None,      [] =======> ... =======> []
    # node                 next
  
    # In each iteration,
    # Either `lt` or `ge` grows by incorporating `node`
  
    # reset `node` to the next node:
    #
    #                      [] =======> ... =======> []
    #                      next
    #                      node
  
    # Eventually, the input linked list in partition into
    
    # [] ======> [] ===> ... ===> []
    # dummy_lt   a                lt
    #
    # [] ======> [] ===> ... ===> []
    # dummy_ge   b                ge
    
    # joins the two partitions: `lt.next` = `dummy_ge`
    #
    # [] ======> [] ===> ... ===> [] ===> [] ===> ... ===> []
    # dummy_lt   a                lt      b                ge
    
    lt = dummy_lt = ListNode(0)
    ge = dummy_ge = ListNode(0)
    
    node = head
    while node:
      # take note of the next node of `node`: 
      next = node.next
      # disconnect node from the remaining of linked list
      node.next = None
      
      # grow either `lt` or `ge`
      if node.val < x:
        lt.next = node
        lt = lt.next
      else:
        ge.next = node
        ge = ge.next
   
      # `node` points to the next node
      node = next
      
    # joins the two parts  
    lt.next = dummy_ge.next
    
    return dummy_lt.next

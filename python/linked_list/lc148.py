"""148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # merge-sort
    # See LC 21 merge two lists
    
    # Nothing needs to be done for linked list with <= 1 nodes
    if not head or not head.next:
      return head
    
    # Use turtle-rabbit two pointers to find the mid-point
    turtle = head
    rabbit = head.next
    
    while rabbit.next:
      rabbit = rabbit.next
      turtle = turtle.next
      if rabbit.next:
        rabbit = rabbit.next
            
    #   []------> ... ------> []--------->[]----------> ... -------->[]
    #   head                  turtle      turtle.next                 
    #   <=========lower========>          <===========upper===========>  
    #                         ^
    #                         mid-point
    
    # step 1:
    # recurisvely sort `upper`:
    #
    # upper: []----------> ... -------->[]---->None
    
    # step 2:
    # disconnect `lower` from `upper`
    #
    #   []------> ... ------> []--->None  []----------> ... -------->[]
    #   head                  turtle      turtle.next                 
    #   <=========lower========>          <===========upper===========>  
    
    # step 3:
    # recursively sort `lower`:
    #
    # lower: []------> ... ------> []--->None  
    
    # step 4:
    # merged the two sorted list `lower` and `upper`
    
    upper = self.sortList(turtle.next)    
    turtle.next = None
    lower = self.sortList(head)
    
    merged = self.mergeTwoLists(lower, upper)
    return merged
    
  def mergeTwoLists(self, l1, l2):
    if not l1:
      return l2
    elif not l2:
      return l1
    
    # `dummy.next` points to the start of a merged list (initially empty)
    #
    # `node` points the end of merged list (initially empty)
    
    
    # [] =======> [] =====> ... ====> [] ======> None
    # dummy                           node
    
    # [] ===> .... ===> [] ===> ... ===>[] ===> None
    #                   l1
    #
    # [] ===> .... ===> [] ===> ... ===>[] ===> None
    #                   l2    
    node = dummy = ListNode(0)
    
    while l1 and l2:
      # `l1` and `l2` points to the head of the two linked lists
      # We pick whichever is smaller, and step the corresponding pointer, `l1` or `l2`
      
      if l1.val < l2.val:
        node.next = l1
        l1 = l1.next
      else:
        node.next = l2
        l2 = l2.next
        
      # We always step `node`    
      node = node.next
      
    if l1:
      node.next = l1
    if l2:
      node.next = l2
      
    return dummy.next  

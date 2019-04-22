"""143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    # Nothing needs to be done if length of linked list <= 1
    if not head or not head.next:
      return head
    
    # Examples:
    # Given 1->2->3->4, reorder it to 1->4->2->3.
    #
    # Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
    
    ##############
    # KEY insight:
    ##############
    #
    # 1. split list into two equal-sized halves, 
    # 2. reverse the second half
    # 3. alternatively merge the two havles (i.e. first, second, first, ...)
    
    # Example1:
    # from 1->2->3->4     to       1->2, 3->4
    # reverse second half:         1->2, 4->3
    # alternatively merge: 1->4->2->3
    
    # Example2:
    # from 1->2->3->4->5  to        1->2->3,  4->5
    # reverse second half:          1->2->3,  5->4
    # alternatively merge: 1->5->2->4->3
    
    # find the mid point of the list: `turtle`
    turtle = head
    rabbit = head.next
    while rabbit:
      rabbit = rabbit.next
      turtle = turtle.next
      if rabbit:
        rabbit = rabbit.next
  
    # reverse the second half pointed to by `turtle.next`  
    right = self.reverse(turtle.next)
    # disconnect first half from second half
    turtle.next = None
    # alternatively merge the first half `gead` and the second half `right`
    return self.alternativeMerge(head, right)
    
  def alternativeMerge(self, left, right):
    # See LC 21 merge two lists
    
    # `dummy.next` points to the start of a merged list (initially empty)
    node = dummy = ListNode(0)
    l, r = left, right
    # toggle: 
    # when True, take node from `left`
    # when False, take node frmo `right`
    toggle = True
    
    while l and r:
      if toggle:
        node.next = l
        l = l.next
      else:
        node.next = r
        r = r.next
      # flip `toggle`
      toggle = not toggle
      # step node
      node = node.next
    
    # deal with whichever of the two lists, `left` or `right`, is non-empty
    node.next = l if l else r
    return dummy.next  
    
  def reverse(self, head):
    # iteratively reverse linked list
    if not head or not head.next:
      return head
    
    prev = None
    curr = head
    next = head.next
    
    while next:
      curr.next = prev
      prev = curr
      curr = next
      next = next.next
    curr.next = prev
    
    return curr

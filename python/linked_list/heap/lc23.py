"""23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution1, use min-heap
class Solution(object):
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists:
      return None
    # We have `k` linked lists
    
    # a11 < a12 < a13 < ... a1n1
    # a21 < a22 < a21 < ... a2n2
    #             ...
    # ak1 < ak2 < ak3 < ... aknk
    
    # The smallest number must be the minimum of a11, a21, ..., ak1
    # Say it's a11.
    
    # What will be the next smallest number?
    
    # It can't be `a13`, ..., `a1n1`, because we have `a12` smaller than them.
    # It can't be `a22`, ..., `a2nk`, because we have `a21` smaller than them.
    # ...
    # It can't be `ak2`, ..., `aknk`, because we have `ak1` smaller than them.
    
    # So again, the next smallest number must be the minimum of a12, a21, ..., ak1
    
    
    
    
    # We know how to merge two sorted lists: LC 21 Merge Two Sorted Lists
    
    # We can use the same approach: 
    # 1. scan the first node of all remainling non-empty linked lists, 
    # and find which one is the smallest
    # 2. remove that from the original linked list and add to the new,
    #   growing linked list
    # 3. repeat step 1 and 2
    
    # However, this would require us to scan all linked list over and over
    # again.
    
    # KEY Idea:
    
    # When we scan the first node of all linked lists, if we put them in 
    # min-heap (keyed on the node's value), we can easily extract the node
    # with minimum value in time O(log k), and insert its successor in the original
    # linked list that it came from
    
    # Initialize the growing linked list
    
    # `dummy.next` always points to the start of the growing list, initially empty
    # `curr` always points to the last node of the growling list, initially empty
    curr = dummy = ListNode(0)

    
    # initialize `heap` with 2-tuples (node's key, node) using the first 
    # node (i.e. curr) of all linked lists
    heap = [(node.val, node) for node in lists if node]
    heapq.heapify(heap)
    
    while heap:
      # Extract the node with minimum value from heap
      _, node = heapq.heappop(heap)
      
      # take note of the successor of `node`
      next = node.next
      # disconnect it from the rest of the linked list it's from
      node.next = None
      
      # add to the growing linked list
      curr.next = node
      curr = curr.next
      
      # insert the successor of the popped node, if it's non-empty
      if next:
        heapq.heappush(heap, (next.val, next))
             
    return dummy.next

# Solution2, divide & conquer
# time: O(N*logk), N = total number of nodes, k = number of lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    # KEY Insight: divide and conquer
    
    # If the number of lists is 2, we already know how to merge two
    # sorted lists. See LC 21 Merge Two Sorted Lists.
    
    # We can split the `lists in two halves:
    
    # list_1, list_2, ... list_m
    #
    # list_m+1, list_m+2, ..., list_k
    
    # And recursively merge the lists in the first half and second half.
    #
    # Let `left` and `right` be the outcomes of the two recursion.
    #
    # Since they are already sorted, we can simply merge them into a single
    # sorted list.
    
    
    # Time complexity:
    #
    # The height of the recursion is O(log k), and in each level
    # of recursion, the number of nodes to be visited is at most O(N) over
    # all merges, where `N` is the total number of nodes
    
    # In total: we have O(N*logk)
    
    
    # Base case:
    # when the number of lists <= 1
    if len(lists) == 0:
      return None
    elif len(lists) == 1:
      return lists[0]
 
    size = len(lists)
    left = self.mergeKLists(lists[:size//2])
    right = self.mergeKLists(lists[size//2:])
    
    merged = node = ListNode(0)
      
    l1 = left
    l2 = right
    while l1 and l2:
      if l1.val < l2.val:
        node.next = l1
        l1 = l1.next
      else:
        node.next = l2
        l2 = l2.next
      node = node.next
        
    if l1:
      node.next = l1
    if l2:
      node.next = l2
    return merged.next 

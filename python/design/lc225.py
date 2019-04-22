"""225. Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""
class MyStack(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.queue1 = []
    self.queue2 = []
        
    # The idea: use two queues
    
    # When an item is PUSHED, we always ENQUEUE it to `queue1`
    
    
    # When an item is POPPED, we DEQUEUE all but the last element in `queue1`.
    # The DEQUEUED items will be ENQUEUED to `queue2`.
    # Then we DEQUEUE the last element in `queue1` as the POPPED item,
    # Finally we swapped `queue2` and `queue1`, so `queue1` has one less item,
    # and `queue2` is still empty
    
    
    # POP: 
    #  
    # queue1: [1, 2, 3]
    # queue2: []
    
    # DEQUEUE all but the last item in `queue1`
    # queue1: [3]
    # queue2: [1, 2]
    
    # DEQUEUE the last item in `queue1`
    # queue1: []
    # queue2: [1, 2]
    
    # Swap `queue1` and `queue2`
    # queue1: [1, 2]
    # queue2: []
    
    # Analysis: PUSH always takes O(1) time.
    # Every time an item is POPPED, we need to traverse all items in `queue1`, which takes
    # O(n)
    
  def push(self, x):
    """
    Push element x onto stack.
    :type x: int
    :rtype: None
    """
    self.queue1.append(x)
        

  def pop(self):
    """
    Removes the element on top of the stack and returns that element.
    :rtype: int
    """
    self.top()
    val = self.queue1.pop(0)
        
    swap = self.queue1
    self.queue1 = self.queue2
    self.queue2 = swap
      
    return val  

  def top(self):
    """
    Get the top element.
    :rtype: int
    """
    while len(self.queue1) > 1:
      self.queue2.append(self.queue1.pop(0))

    return self.queue1[0]
    
    
  def empty(self):
    """
    Returns whether the stack is empty.
    :rtype: bool
    """
    return len(self.queue1) == 0  and len(self.queue2) == 0   


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
class MyQueue(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.stack_in = []
    self.stack_out = []
    
    # The idea: use two stacks:

    
    # Whenever an item is ENQUEUED, we PUSH to the stack `stack_in`.
    
    # ENQUEUE item
    #
    # stack_in:  <= item
    # stack_out:
    
    
    # Whenever an item is DEQUEUED, we check if `stack_out` is empty or not:
    # 1. if `stack_out` is not empty, we simply POP an item from `stack_out`
    # 2. if `stack_out` is empty, we POP all items in `stack_in` out of 
    #    `stack_in`, and PUSH them to `stack_out` in the order they were popped
    #     from `stack_in`.
    
    # DEQUEUE item, when `stack_out` is empty
  
    # stack_in: [1, 2, 3)
    # stack_out: [)
    
    # stack_in: [)
    # stack_out: [3, 2, 1)
    
    # stack_in: [)
    # stack_out: [3, 2) ==> 1
    
    # Analysis:
    # ENQUEUE operation is always O(1)
    
    # DEQUEUE operation may take O(n) in worst case, `n` being the number of items
    # in `stack_in`. But since every item is only moved from `stack_in` to `stack_out`
    # once, so the average time complexity should be O(1).
    
  def push(self, x):
    """
    Push element x to the back of queue.
    :type x: int
    :rtype: None
    """
    self.stack_in.append(x)
        
  def pop(self):
    """
    Removes the element from in front of queue and returns that element.
    :rtype: int
    """
    if not self.stack_out:
      while self.stack_in:
        self.stack_out.append(self.stack_in.pop())
    return self.stack_out.pop()
        
  def peek(self):
    """
    Get the front element.
    :rtype: int
    """
    if not self.stack_out:
      while self.stack_in:
        self.stack_out.append(self.stack_in.pop())
    return self.stack_out[-1]
    
  def empty(self):
    """
    Returns whether the queue is empty.
    :rtype: bool
    """
    return not (self.stack_in or self.stack_out)   
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

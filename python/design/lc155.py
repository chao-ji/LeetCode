"""155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack(object):

  def __init__(self):
    """
    initialize your data structure here.
    """
    # `stack` is the just the stack implemented as a python list holding
    # the elements
    #
    #
    # we could implement another stack `min` of the same size as `stack`,
    # holding the min value of elements that are currently on the stack
    #
    # for example
    #
    # `stack` = [2,3,2,2,1,2,2]
    # `min` =   [2,2,2,2,1,1,1]
    # 
    # BUT, we could save space by collapsing identical and contiguous numbers in
    # `min`, so `min` is turned into [(2, 4), (1, 3)]
    # where the first element in a tuple is the number and the second element
    # is the number of times they are repeated.
    
    self.stack = []
    self.min = []

  def push(self, x):
    """
    :type x: int
    :rtype: None
    """
    self.stack.append(x)
    # when `min` is empty or `x` is smaller than all elements pushed to stack
    # so far, add a new tuple to `min`
    if not self.min or x < self.min[-1][0]:
      self.min.append([x, 1])
    # otherwise, increment the count of the element at the top.  
    else:
      self.min[-1][1] += 1  
      
  def pop(self):
    """
    :rtype: None
    """
    assert self.stack
    self.stack.pop()
    
    # if the count at the top > 1, decrement the count
    if self.min[-1][1] > 1:
      self.min[-1][1] -= 1
    # if there is only one element (i.e. count == 1), pop the tuple  
    else:
      self.min.pop()
    
  def top(self):
    """
    :rtype: int
    """
    assert self.stack
    return self.stack[-1]    

  def getMin(self):
    """
    :rtype: int
    """
    assert self.min
    return self.min[-1][0]    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
import math

class Solution(object):
  def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    # The idea:
    
    # In Reverse Polish Notation, the operator always FOLLOWS the operands (i.e. numbers)
    
    # We scan `tokens` from left to right. Whenever we see a streak of three elements:
    # [num], [num], [op],
    # we replace them the result [num] of this operation [num] [op] [num]
    
    # The resulting number may become the operand of operator yet to be seen in `tokens`
    # So we push the resulting number (and any number) onto the stack,
    #
    # And when we see an operator, we pop the top two elements from the stack, which 
    # are suppposed to the be corresponding operands:
    
    # Algorithm:
    
    # for each token in the postfix expression:
    #
    #   if token is an operator:
    #     operand_2 ← pop from the stack
    #     operand_1 ← pop from the stack
    #     result ← evaluate token with operand_1 and operand_2
    #     push result back onto the stack
    #   else if token is an operand:
    #     push token onto the stack
    #
    # result ← pop from the stack
    
    stack = []
    
    for i in range(len(tokens)):
      # Push number onto stack
      if tokens[i] not in '+-*/':
        stack.append(tokens[i])
      # Evaluate operator and push result onto stack  
      else:
        op2 = stack.pop()
        op1 = stack.pop()
        if tokens[i] == '+':
          stack.append(int(op1) + int(op2))
        elif tokens[i] == '-':
          stack.append(int(op1) - int(op2))
        elif tokens[i] == '*':
          stack.append(int(op1) * int(op2))
        else:
          raw = float(op1) / float(op2)
          # division truncates toward 0
          if raw >= 0:
            stack.append(int(math.floor(raw)))
          else:
            stack.append(int(math.ceil(raw)))
        
    return stack.pop()

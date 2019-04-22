"""12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"

Example 3:

Input: 9
Output: "IX"

Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
class Solution(object):
  def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    # The idea: 
    #
    # Roman Numerals has 7 symbols
    
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    
    # which can be divided into (I, V), (X, L), (C, D), (M) 
    # four groups, and each group pertains to a digit.
    
    # Because `num` is in range [1, 3999], which has at most four digits
    
    # We can consider the Roman representation of each digit individually,
    # 
    # Example, `num` = d4 d3 d2 d1
    #
    # Note d4 can be 1, 2, or 3
    
    # If any of the digit is 0, we can safely skip it
    
    # if 1 <= `d` <= 3, the Roman representation would simply be
    #   (I|X|C) * `d`
    
    # if `d` == 5, the Roman representation would simply be 
    #   V, L, D
    
    # The TRICKY part is when `d` == 4, 6, 7, 8 and 9
    #
    # We know that we `d` == 4, we need to place a smaller numeral
    # BEFORE a larger one, e.g.
    # 4 = IV, 40 = XL, 400 = CD
    
    # And when `d` = 6, 7, 8, we need to place a smaller numeral 
    # AFTER a larger one, e.g.
    # 6 = VI, 60 = LX, 600 = DC
    
    # And when `d` = 9, we need to look at digit on the left (i.e
    # the next group of Roman numerals)
    #
    # 9 = IV, 90 = XC, 900 = CM
    
    
    # `digits` store digit values from least significant to most
    # siginificant order
    digits = [] 
    while num > 0:
      mod = num % 10
      num = num // 10
      digits.append(mod)
      
    roman = ""
    roman_chars = [('I', 'V'), # 0th digit 
                   ('X', 'L'), # 1st digit
                   ('C', 'D'), # 2nd digit
                   ('M', None)]# 3rd digit
    
    for i, d in enumerate(digits):
      # i = 0, 1, 2, 3
      # d = digit at position `i`
      
      if d == 0: # 0's can be ignored safely 
        pass
      elif 1 <= d <= 3: # Just count the ones, tens, or hundreds
        roman = roman_chars[i][0] * d + roman
      elif d == 4: # subtract one, ten, or hundred from 5, 50 or 500
        roman = roman_chars[i][0] + roman_chars[i][1] + roman
      elif d == 5: # 5, 50, 500
        roman = roman_chars[i][1] + roman
      elif 6 <= d <= 8: # add ones, tens, or hundreds to 5, 50, 500
        roman = roman_chars[i][1] + roman_chars[i][0] * (d - 5) + roman
      elif d == 9: # subtract one, ten, hundred from ten, hundred, thousand
        roman = roman_chars[i][0] + roman_chars[i + 1][0] + roman
    return roman    

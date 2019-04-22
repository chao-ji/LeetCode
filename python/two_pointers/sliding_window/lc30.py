"""30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""
from collections import Counter

class Solution(object):
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
        
    if not s or not words:
      return []
    
    # Use the same strategy as LC 76 Minimum Window Substring
    #
    # The DIFFERENCE is that we need to find all valid windows, rather than
    # finding the minimum length window.

    words_counter = Counter(words)
    
    word_len = len(words[0])
    total_word_len = word_len * len(words)
    
    i = 0
    indices = []
    while i + total_word_len - 1 < len(s):
      # We maintain `win_counter` and `filled_counts` to keep track of the validity of 
      # the current window, staring at `i`
      #
      # It's always invalid unless `filled_counts` reaches `len(words_counter)`, i.e. 
      # contains all the words in `words`
      filled_counts = 0
      win_counter = {}

      # Expand the window by appending a "word" one at a time
      for j in range(len(words)):
        word = s[i + j * word_len : i + (j + 1) * word_len]
      
        # update the two variables `win_counter` and `filled_counts` when a new word
        # is added to current window
        win_counter[word] = win_counter.get(word, 0) + 1
        if win_counter[word] == words_counter[word]:
          filled_counts += 1
        
        # current window is INVALID, terminate 
        if word not in words_counter or win_counter[word] > words_counter[word]:
          break
                
      # At this point, we have examined the entire current window starting at `i`
      # Add to result if it is valid.
      if filled_counts == len(words_counter):
        indices.append(i)
        
      i += 1
    return indices  

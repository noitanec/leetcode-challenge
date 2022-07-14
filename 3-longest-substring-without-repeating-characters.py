"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        ls = ""
        for i in range(len(s)):
            seq = ""
            for j in range(i, len(s)):
                if s[j] not in seq:
                    seq += s[j]
                else:
                    if len(seq) > len(ls):
                        ls = seq
                    break
            if len(seq) > len(ls):
                ls = seq
        return len(ls)
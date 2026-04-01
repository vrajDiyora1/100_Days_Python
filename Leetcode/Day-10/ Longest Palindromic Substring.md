## Day 1: T Longest Palindromic Substring

#### Purpose
> Given a string s, return the longest palindromic substring in s.


#### Step by Step
```
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
```
#### Code
```python
    class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
    
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        for i in range(len(s)):
            p1 = expand(i, i)
            
            p2 = expand(i, i+1)
            
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
        
        return res

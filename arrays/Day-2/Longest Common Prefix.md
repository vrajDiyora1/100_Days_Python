## Day 1: [Longest Common Prefix] 

#### Purpose
>Write a function to find the longest common prefix string amongst an array of strings.



#### Problem Statement
> If there is no common prefix, return an empty string "".



#### Step by Step
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

#### Code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for x in range(len(strs[0])):
            char = strs[0][x]
            for y in range(1,len(strs)):
                if x == len(strs[y]) or strs[y][x]!=char:
                    return strs[0][:x]
        return strs[0]
 ...

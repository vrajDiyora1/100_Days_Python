
## Day 5: Search Insert Position

#### Problem Statement
> Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

> You must write an algorithm with O(log n) runtime complexity.




#### Step by Step
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

#### Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i!=j and nums[i] + nums[j] ==target):
                    return[i,j]
        return[]
        
 ...

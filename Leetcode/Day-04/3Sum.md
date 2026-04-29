## Day 4: 3Sum

#### Purpose
> We need to find all unique triplets in the array that sum to 0.

#### Problem Statement
> Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

> Notice that the solution set must not contain duplicate triplets.


#### Step by Step
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

#### Code
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        op = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            y = i + 1
            z = len(nums)-1
            
            while y < z:
                total = nums[i] + nums[y] + nums[z]

                if total > 0:
                    z-=1
                elif total < 0:
                    y+= 1
                else:
                    op.append([nums[i],nums[y],nums[z]])
                    y+=1

                    while y < z and nums[y] == nums[y-1]:
                        y+=1
        return op
 ...

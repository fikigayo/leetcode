from typing import List

nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(0, len(nums)-1, 1):
            for j in range(i+1,len(nums), 1):
                if(nums[i]+nums[j]==target):
                    arr.append(i)
                    arr.append(j)
        return arr
        

print(Solution().twoSum(nums,target))
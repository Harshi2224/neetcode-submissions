class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetSum={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in targetSum:
                return[targetSum[diff],i]
            targetSum[n]=i
        return
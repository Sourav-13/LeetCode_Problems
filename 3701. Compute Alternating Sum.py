class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        oddCount, evenCount =0, 0
        for i in range(len(nums)):
            if (i%2==0):
                evenCount +=nums[i]
            else:
                oddCount +=nums[i]
        return evenCount - oddCount
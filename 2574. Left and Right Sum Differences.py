class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ansSum = []
        leftSum = 0
        rightSum = sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i]
            ansSum.append(abs(leftSum - rightSum))
            leftSum += nums[i]
        return ansSum
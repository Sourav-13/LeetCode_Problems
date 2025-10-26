class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        countOp = 0

        for num in nums:
            if (num+1)%3 == 0 or (num-1)%3 == 0:
                countOp += 1
        return countOp
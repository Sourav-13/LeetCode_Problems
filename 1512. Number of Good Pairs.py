class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if(i<j):
                    if(nums[i]==nums[j]):
                        count += 1
        return count
        
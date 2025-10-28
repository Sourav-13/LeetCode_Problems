class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        total = 0
        for i, num in enumerate(nums):
                for num2 in nums[i+1:]:
                    if num + num2 < target:
                        total +=1
        return total
    
#better
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        summ = 0
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[j] >= target-nums[i]:
                j -= 1
            else:
                summ += (j-i)
                i += 1
        return summ
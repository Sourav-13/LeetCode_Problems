class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        total = 0
        for i in range(len(nums)):
            if (nums[i] == nums[i+1]):
                res.append(nums[i])
                total += 1
            if total == 2:
                break
        return res
    

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set()
        count = 0
        res = []
        for num in nums:
            if num in nums_set:
                count += 1
                res.append(num)
            if count == 2:
                break
            nums_set.add(num)
        return res
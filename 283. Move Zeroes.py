#Worst
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == 0:
                    if nums[j] ==0:
                        continue
                    else:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                continue
            
#best
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                
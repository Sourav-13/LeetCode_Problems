class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        l = int(len(nums)/2)
        for i in range(l):
            ans.append(nums[i])
            ans.append(nums[n])
            n += 1
        return ans

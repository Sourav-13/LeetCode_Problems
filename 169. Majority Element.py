from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counter = Counter(nums)
        return max(num_counter, key=num_counter.get)

#0ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        return sort_nums[len(nums)//2]
        
#best
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        count = 0
        candidate = None
        
        for num in nums:
            # If count is 0, we set the current number
            # as our new candidate for majority element.
            if count == 0:
                candidate = num
            
            # If the current number matches the candidate,
            # it gets a "vote".
            if num == candidate:
                count += 1
            # If it's a different number, it "cancels" a vote.
            else:
                count -= 1
                
        # Since the problem guarantees a majority element always
        # exists, we can just return the final candidate.
        return candidate
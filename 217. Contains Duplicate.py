class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = Counter(nums)
        return max(x.values()) > 1
    
    
#best
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # 1. Convert the list to a set.
        #    e.g., [1, 2, 3, 1] becomes {1, 2, 3}
        num_set = set(nums)
        
        # 2. Compare the lengths.
        #    len([1, 2, 3, 1]) is 4
        #    len({1, 2, 3}) is 3
        #    Since 4 != 3, we return True.
        
        return len(num_set) != len(nums)
    
    
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create an empty set to store numbers we have "seen"
        seen = set()
        
        for num in nums:
            # Check if we've already seen this number
            if num in seen:
                # If yes, we found a duplicate
                return True
            
            # If no, add it to our set of seen numbers
            seen.add(num)
            
        # If we get through the whole loop, no duplicates were found
        return False
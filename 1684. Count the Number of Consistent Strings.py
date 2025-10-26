#submitted
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for word in words:
            for ch in word:
                if ch not in allowed:
                    break  
            else:
                count += 1

        return count
    
    
#another way
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)  # O(len(allowed)) time
        count = 0

        for word in words:
            if all(ch in allowed_set for ch in word):
                count += 1

        return count

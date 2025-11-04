#not accepted - time limit exceeded
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_list = []
        used = set()

        for i, i_val in enumerate(strs):
            if i in used:
                continue
            temp_list = [i_val]
            for j, j_val in enumerate(strs):
                if i != j and Counter(i_val) == Counter(j_val):
                    temp_list.append(j_val)
                    used.add(j)
            used.add(i)
            ans_list.append(temp_list)
        return ans_list


#best
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Use defaultdict to automatically initialize new keys with an empty list
        anagram_groups = defaultdict(list)
        
        # Get the ASCII value of 'a' to use as an offset
        offset = ord('a')
        
        for s in strs:
            # Create a character count array (list) for the current string
            count = [0] * 26
            
            for char in s:
                # Increment the count for this character
                count[ord(char) - offset] += 1
            
            # Convert the count list to a tuple so it can be used
            # as a dictionary key.
            # e.g., "eat" -> (1, 0, 0, 0, 1, 0, ..., 1, 0, ...)
            key = tuple(count)
            
            # Append the original string to the list for this key
            anagram_groups[key].append(s)
            
        # Return the values of the dictionary (which are the lists of anagrams)
        return list(anagram_groups.values())
    

#better

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # The sorted string is the key.
            # "eat", "tea", and "ate" all become "aet".
            key = "".join(sorted(s))
            
            anagram_groups[key].append(s)
            
        return list(anagram_groups.values())
    
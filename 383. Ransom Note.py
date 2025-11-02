class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(magazine) < len(ransomNote)):
            return False
            
        ran_dict = defaultdict(int)
        mag_dict = defaultdict(int)

        for i in range (len(magazine)):
            mag_dict[magazine[i]] += 1
            if (i < len(ransomNote)):
                ran_dict[ransomNote[i]] += 1
            
            
        for key, value in ran_dict.items():
            print(value, mag_dict[key])
            if (value > mag_dict[key]):
                return False
            
        return True
            
            
        
#best    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True
    
    
    
#Gemini
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1. Count the frequency of each character in the ransom note.
        #    e.g., "aab" -> {'a': 2, 'b': 1}
        note_counts = Counter(ransomNote)
        
        # 2. Count the frequency of each character in the magazine.
        #    e.g., "aabbc" -> {'a': 2, 'b': 2, 'c': 1}
        magazine_counts = Counter(magazine)
        
        # 3. Iterate through the characters required by the ransom note.
        for char, count_needed in note_counts.items():
            # Check if the magazine has enough of that character.
            # If the count in the magazine is less than the count needed,
            # we can't build the note.
            if magazine_counts[char] < count_needed:
                return False
                
        # 4. If we get through the whole loop, the magazine has 
        #    enough of every required character.
        return True
    
    
    
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        
        # Subtract the note's char counts from the magazine's.
        # If any count in the result is positive, it means
        # the note needed more of a char than the magazine had.
        # e.g., Counter('aab') - Counter('ab') = Counter({'a': 1})
        difference = note_counts - magazine_counts
        
        # 'difference' will only contain positive remaining counts.
        # If it's empty, it means the magazine had enough of everything.
        return not difference
# submitted 
class Solution:
    def maxFreqSum(self, s: str) -> int:
        countList = [0] * 128   
        for c in s:
            countList[ord(c)] += 1 
            
        vowMax, conMax = 0, 0
        for i in range(128):
            if countList[i] > 0:
                if i == ord("a") or i == ord("e") or i == ord("i") or i == ord("o") or i == ord("u"):
                    vowMax = countList[i] if vowMax < countList[i] else vowMax
                else:
                    conMax = countList[i] if conMax < countList[i] else conMax
        return vowMax + conMax




# optimized
class Solution:
    def maxFreqSum(self, s: str) -> int:
        char_count = [0] * 128
        
        for c in s:
            char_count[ord(c)] += 1

        vowels = set("aeiou")
        vowMax, conMax = 0, 0
        
        for c in s: 
            idx = ord(c)
            if c in vowels:
                vowMax = max(vowMax, char_count[idx])
            else:
                conMax = max(conMax, char_count[idx])
        
        return vowMax + conMax

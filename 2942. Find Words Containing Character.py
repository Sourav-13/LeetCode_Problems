class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        i=0
        for w in words:
            if x in w:
                ans.append(i)
            i += 1
        return ans
    
    
    
    #Better run time ->
        """class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i,word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans
        
        """
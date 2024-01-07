class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        wordCount = []
        for s in sentences:
            wordCount.append( s.count(' ') )
        return max(wordCount) + 1       


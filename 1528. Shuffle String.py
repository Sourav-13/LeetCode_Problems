class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newS = list(s)
        for i, ind in enumerate(indices):
            newS[ind] = s[i]
        return ''.join(newS)

